## 必填 Entries
# start_date :合約起始日 (date)
# end_date：合約到期日 (date, but >= start_date)
# party_a_name: 甲方名稱 (combo box)
# party_a_representative (combo box, filtered by party_a_name)
# party_a_registered_address 甲方公司登記地址 (rich edit)
# party_a_contact_address (optional rich edit)
# party_b_name: 乙方名稱 (rich edit)
# party_b_representative (rich edit)
# party_b_registered_address 乙方公司登記地址 (rich edit)
# party_b_contact_address (optional rich edit)
# signature_date (date)
# payment_method (combo box)
# currency (combo box 十幾種)
#   is_cross_border_payment (Yes/No checkbox, always follow currency)

## Optional rich edit
## 1-7 must be either all empty of all-filled
## if 1-7 is empty, remove 8 and 9
# 1. bank_account 銀行帳號
# 2. account_name 戶名
# 3. name_of_the_bank 銀行名稱
# 4. bank_code 銀行代碼
# 5. name_of_the_branch 分行名稱
# 6. branch_code 分行代碼
# 7. country_of_the_bank_receiving_the_payment 收款行國別
# swift_code SWIFT CODE
# other_code  □CNAPS □SKN CODE □BSB NUMBER □IBAN CODE

import os
import sys
import pathlib
import ast

from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PySide6.QtCore import QFile, QDate, QLocale

from contract_generator_model import Ui_MainWindow

"""
IBM 3 character code
"""
def lang2code(name):
    return {
        u"\u7e41\u9ad4\u4e2d\u6587": "cht",
        u"English": "enu",
        u"\u65e5\u672c\u8a9e": "jpn",
        u"\ud55c\uad6d\uc5b4": "kor"
    }.get(name, "cht")

def get_contract_template_dir(lang):
    return "templates/contract_templates/" + lang2code(lang)

def get_payment_method_template_dir(lang):
    return "templates/payment_method_templates/" + lang2code(lang)

def get_party_a_template_dir(lang):
    return "templates/party_a_template/" + lang2code(lang)

from string import Formatter
def read_utf8(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read().decode('UTF-8')

def parse_fields(txt):
    if txt:
        return [fname for _, fname, _, _ in Formatter().parse(txt) if fname]

def read_fields(path):
    txt = read_utf8(path)
    return parse_fields(txt)

def enable_controls(control_list):
    for control in control_list:
        control.setEnabled(True)

def zh_tw_locale():
    return QLocale(QLocale.Chinese, QLocale.TraditionalChineseScript, QLocale.Taiwan)

def zh_tw_date_format():
    return "yyyy 年 MM 月 dd 日"

def en_us_locale():
    return QLocale(QLocale.English, QLocale.UnitedStates)

def en_us_date_format():
    return "MMMM dd, yyyy"

def ja_jp_locale():
    return QLocale(QLocale.Japanese, QLocale.Japan)

def ja_jp_date_format():
    return "yyyy 年 MM 月 dd 日"

def ko_kr_locale():
    return QLocale(QLocale.Korean, QLocale.SouthKorea)

def ko_kr_date_format():
    return "yyyy 년 MM 월 dd 일"

def select_locale(x):
    return {
        "繁體中文": zh_tw_locale(), 
        "English": en_us_locale(), 
        "日本語": ja_jp_locale(),
        "한국어": ko_kr_locale()
    }.get(x, en_us_locale())  

def select_date_format(x):
    return {
        "繁體中文": zh_tw_date_format(), 
        "English": en_us_date_format(), 
        "日本語": ja_jp_date_format(),
        "한국어": ko_kr_date_format()
    }.get(x, en_us_date_format())  

def select_locale_and_date_format(x):
    return (select_locale(x), select_date_format(x))

def to_date_str(lang, qdate):
    curr_locale, date_fmt = select_locale_and_date_format(lang)
    return curr_locale.toString(qdate, date_fmt)

"""
Step1: Select language
Step2: Select contract template
(Step3: Select payment method)
Step4: Fill in the table
Step5: Execute
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init()

    def init(self):
        self.init_date_controls()
    
    def init_date_controls(self):
        today = QDate.currentDate()
        self.ui.start_date_selector.setDate(today)
        self.ui.end_date_selector.setDate(today)
        self.ui.signature_date_selector.setDate(today)
    
    def on_language_selector_changed(self):
        # Disable all other controls
        # Enable template selector
        self.ui.contract_template_label.setEnabled(self.ui.lang_selector.currentIndex() != -1)
        self.ui.contract_template_selector.setEnabled(self.ui.lang_selector.currentIndex() != -1)
        # Add template names to the selector
        if self.ui.contract_template_selector.isEnabled():
            self.ui.contract_template_selector.clear()

            template_dir = get_contract_template_dir(self.ui.lang_selector.currentText())
            for _, _, files in os.walk(template_dir):
                for f in files:
                    p = pathlib.Path(f)
                    if p.suffix == ".template":
                        self.ui.contract_template_selector.addItem(p.stem)
    
    def get_contract_template_path(self):
        return os.path.join(get_contract_template_dir(self.ui.lang_selector.currentText()), self.ui.contract_template_selector.currentText() + ".template")
    
    def on_contract_template_selector_changed(self):
        template_path = self.get_contract_template_path()
        fields = read_fields(template_path)
        enable_controls(self.fields2controls(fields))

        if self.ui.party_a_name_selector.isEnabled():
            self.party_a_template = self.load_party_a_template()
            if self.party_a_template:
                self.ui.party_a_name_selector.clear()
                self.ui.party_a_name_selector.setCurrentIndex(-1)
                self.ui.party_a_representative_selector.clear()
                self.ui.party_a_representative_selector.setCurrentIndex(-1)

                self.ui.party_a_name_selector.addItems(self.party_a_template.keys())

        if self.ui.payment_method_selector.isEnabled():
            self.ui.payment_method_selector.clear()
            payment_method_template_dir = get_payment_method_template_dir(self.ui.lang_selector.currentText())
            for _, _, files in os.walk(payment_method_template_dir):
                for f in files:
                    p = pathlib.Path(f)
                    if p.suffix == ".template":
                        self.ui.payment_method_selector.addItem(p.stem)
    
    def load_party_a_template(self):
        template_dir = get_party_a_template_dir(self.ui.lang_selector.currentText())
        for _, _, files in os.walk(template_dir):
            templates = [pathlib.Path(x) for x in files if pathlib.Path(x).suffix == ".template"]
            if templates:
                with open(os.path.join(template_dir, templates[0]), 'rb') as f:
                    txt = f.read().decode('UTF-8')
                    return ast.literal_eval(txt)
        
        return {}
    
    def on_party_a_name_selector_changed(self):
        if self.party_a_template:
            self.ui.party_a_representative_selector.clear()
            self.ui.party_a_representative_selector.setCurrentIndex(-1)
            self.ui.party_a_representative_label.setEnabled(True)
            self.ui.party_a_representative_selector.setEnabled(True)
            self.ui.party_a_representative_selector.addItems(self.party_a_template[self.ui.party_a_name_selector.currentText()])
    
    def get_payment_method_template_path(self):
        return os.path.join(get_payment_method_template_dir(self.ui.lang_selector.currentText()), self.ui.payment_method_selector.currentText() + ".template")

    def on_payment_method_selector_changed(self):
        template_path = self.get_payment_method_template_path()
        fields = read_fields(template_path)
        enable_controls(self.fields2controls(fields))
    
    def check_mandatory_fields(self):
        self.ui.execute_button.setEnabled(False)
        if self.ui.lang_selector.currentIndex() == -1 or self.ui.contract_template_selector.currentIndex() == -1:
            return

        if self.ui.start_date_selector.isEnabled() and self.ui.end_date_selector.isEnabled() and (self.ui.end_date_selector.date() < self.ui.start_date_selector.data()):
            return
        
        if self.ui.party_a_name_selector.isEnabled() and self.ui.party_a_name_selector.currentIndex() == -1:
            return
        
        if self.ui.party_a_representative_selector.isEnabled() and self.ui.party_a_representative_selector.currentIndex() == -1:
            return
    
        if self.ui.party_a_registered_address_edit.isEnabled() and self.ui.party_a_registered_address_edit.text() == "":
            return

        if self.ui.party_b_name_edit.isEnabled() and self.ui.party_b_name_edit.text() == "":
            return

        if self.ui.party_b_representative_edit.isEnabled() and self.ui.party_b_representative_edit.text() == "":
            return

        if self.ui.party_b_registered_address_edit.isEnabled() and self.ui.party_b_registered_address_edit.text() == "":
            return

        if self.ui.payment_method_selector.isEnabled() and self.ui.payment_method_selector.currentIndex() == -1:
            return

        if self.ui.currency_selector.isEnabled() and self.ui.currency_selector.currentIndex() == -1:
            return

        if self.ui.bank_account_edit.isEnabled() and self.ui.bank_account_edit.text() == "":
            return

        if self.ui.account_name_edit.isEnabled() and self.ui.account_name_edit.text() == "":
            return

        if self.ui.name_of_the_bank_edit.isEnabled() and self.ui.name_of_the_bank_edit.text() == "":
            return

        if self.ui.bank_code_edit.isEnabled() and self.ui.bank_code_edit.text() == "":
            return

        if self.ui.name_of_the_branch_edit.isEnabled() and self.ui.name_of_the_branch_edit.text() == "":
            return

        if self.ui.branch_code_edit.isEnabled() and self.ui.branch_code_edit.text() == "":
            return

        if self.ui.country_of_the_bank_receiving_the_payment_edit.isEnabled() and self.ui.country_of_the_bank_receiving_the_payment_edit.text() == "":
            return
        
        if self.ui.other_code_edit.isEnabled() and self.ui.other_code_edit == "":
            button_group = QButtonGroup()
            button_group.addButton(self.ui.other_code_cnaps)
            button_group.addButton(self.ui.other_code_skn_code)
            button_group.addButton(self.ui.other_code_bsb_number)
            button_group.addButton(self.ui.other_code_iban_code)
            if button_group.checkedId == -1:
                return

        self.ui.execute_button.setEnabled(True)

    def fields2controls(self, fields):
        controls = []
        for field in fields:
            controls.extend(self.field2control(field))
        
        return controls

    def field2control(self, field):
        return {
            "start_date": [self.ui.start_date_label, self.ui.start_date_selector],
            "end_date": [self.ui.end_date_label, self.ui.end_date_selector],
            "party_a_name": [self.ui.party_a_name_label, self.ui.party_a_name_selector],
            "party_a_representative": [self.ui.party_a_representative_label, self.ui.party_a_representative_selector],
            "party_a_registered_address": [self.ui.party_a_registered_address_label, self.ui.party_a_registered_address_edit,
                                           self.ui.party_a_contact_address_label, self.ui.party_a_contact_address_edit],
            "party_b_name": [self.ui.party_b_name_label, self.ui.party_b_name_edit],
            "party_b_representative": [self.ui.party_b_representative_label, self.ui.party_b_representative_edit],
            "party_b_registered_address": [self.ui.party_b_registered_address_label, self.ui.party_b_registered_address_edit,
                                           self.ui.party_b_contact_address_label, self.ui.party_b_contact_address_edit],
            "signature_date": [self.ui.signature_date_label, self.ui.signature_date_selector],
            "payment_method": [self.ui.payment_method_label, self.ui.payment_method_selector],
            "currency": [self.ui.currency_label, self.ui.currency_selector, self.ui.cross_boader_payment_group, self.ui.cross_border_payment_yes, self.ui.cross_border_payment_no],
            "bank_account": [self.ui.bank_account_label, self.ui.bank_account_edit],
            "account_name": [self.ui.account_name_label, self.ui.account_name_edit],
            "name_of_the_bank": [self.ui.name_of_the_bank_label, self.ui.name_of_the_bank_edit],
            "bank_code": [self.ui.bank_code_label, self.ui.bank_code_edit],
            "name_of_the_branch": [self.ui.name_of_the_branch_label, self.ui.name_of_the_branch_edit],
            "branch_code": [self.ui.branch_code_label, self.ui.branch_code_edit],
            "country_of_the_bank_receiving_the_payment": [self.ui.country_of_the_bank_receiving_the_payment_label, self.ui.country_of_the_bank_receiving_the_payment_edit],
            "swift_code": [self.ui.swift_code_label, self.ui.swift_code_edit],
            "other_code": [self.ui.other_code_group, 
                           self.ui.other_code_cnaps,
                           self.ui.other_code_skn_code,
                           self.ui.other_code_bsb_number,
                           self.ui.other_code_iban_code,
                           self.ui.other_code_edit]
        }.get(field)
    
    def get_start_date_str(self):
        return to_date_str(self.ui.lang_selector.currentText(), self.ui.start_date_selector.date())
    
    def get_end_date_str(self):
        return to_date_str(self.ui.lang_selector.currentText(), self.ui.end_date_selector.date())
    
    def get_party_a_name(self):
        return self.ui.party_a_name_selector.currentText()
    
    def get_party_a_representative(self):
        return self.ui.party_a_representative_selector.currentText()

    def get_party_a_registered_address(self):
        return self.ui.party_a_registered_address_edit.text()
    
    def get_party_a_contact_address(self):
        return self.ui.party_a_contact_address_edit.text()
    
    def get_party_b_name(self):
        return self.ui.party_b_name_edit.text()
    
    def get_party_b_representative(self):
        return self.ui.party_b_representative_edit.text()
    
    def get_party_b_registered_address(self):
        return self.ui.party_b_registered_address_edit.text()
    
    def get_party_b_contact_address(self):
        return self.ui.party_b_contact_address_edit.text()
    
    def get_signature_date(self):
        return to_date_str(self.ui.lang_selector.currentText(), self.ui.signature_date_selector.date())
    
    def get_payment_method(self):
        return "dummy"
    
    def get_currency(self):
        # currency (combo box 十幾種)
        #   is_cross_border_payment (Yes/No checkbox, always follow currency)
        self.ui.currency_selector.currentText()
        button_group = QButtonGroup()
        button_group.addButton(self.ui.cross_border_payment_yes)
        button_group.addButton(self.ui.cross_border_payment_no)
        button_group.checkedButton().text()
        return "dummy currency + cross border payment"
    
    def get_bank_account(self):
        return self.ui.bank_account_edit.text()
    
    def get_account_name(self):
        return self.ui.account_name_edit.text()
    
    def get_name_of_the_bank(self):
        return self.ui.name_of_the_bank_edit.text()
    
    def get_bank_code(self):
        return self.ui.bank_code_edit.text()
    
    def get_name_of_the_branch(self):
        return self.ui.name_of_the_branch_edit.text()
    
    def get_branch_code(self):
        return self.ui.branch_code_edit.text()
    
    def get_country_of_the_bank_receiving_the_payment(self):
        return self.ui.country_of_the_bank_receiving_the_payment_edit.text()
    
    def get_swift_code(self):
        return self.ui.swift_code_edit.text()
    
    def get_other_code(self):
        # other_code  □CNAPS □SKN CODE □BSB NUMBER □IBAN CODE
        # button_group = QButtonGroup()
        # button_group.addButton(self.ui.other_code_cnaps)
        # button_group.addButton(self.ui.other_code_skn_code)
        # button_group.addButton(self.ui.other_code_bsb_number)
        # button_group.addButton(self.ui.other_code_iban_code)
        # button_group.checkedButton().text()
        # self.ui.other_code_edit.text()
        return "other code + optional edit"
    
    def get_field_value(self, field):
        return {
            "start_date": self.get_start_date_str(),
            "end_date": self.get_end_date_str(),
            "party_a_name": self.get_party_a_name(),
            "party_a_representative": self.get_party_a_representative(),
            "party_a_registered_address": self.get_party_a_registered_address(),
            "party_a_contact_address": self.get_party_a_contact_address(),
            "party_b_name": self.get_party_b_name(),
            "party_b_representative": self.get_party_b_representative(),
            "party_b_registered_address": self.get_party_b_registered_address(),
            "party_b_contact_address": self.get_party_b_contact_address(),
            "signature_date": self.get_signature_date(),
            "payment_method": self.get_payment_method(),
            "bank_account": self.get_bank_account(),
            "account_name": self.get_account_name(),
            "name_of_the_bank": self.get_name_of_the_bank(),
            "bank_code": self.get_bank_code(),
            "name_of_the_branch": self.get_name_of_the_branch(),
            "branch_code": self.get_branch_code(),
            "country_of_the_bank_receiving_the_payment": self.get_country_of_the_bank_receiving_the_payment(),
            "swift_code": self.get_swift_code(),
            "other_code": self.get_other_code()
        }.get(field, None)
    
    def get_field_values(self, field_names):
        return list(map(self.get_field_value, field_names))
    
    def read_contract_template(self):
        template_path = self.get_contract_template_path()
        print(template_path)
        return read_utf8(template_path)
    
    def get_markdown(self):
        template = self.read_contract_template()
        field_names = parse_fields(template)
        field_values = self.get_field_values(field_names)
        d = dict(zip(field_names, field_values))
        return template.format(**d)

    def on_execute(self):
        md = self.get_markdown()
        print(md)
    
    def get_payment_method_md(self):
        # if payment method active:
        #     payment_method_md = load_payment_method_template()
        #     payment_method_fields = parse_fields(payment_method_md)
        #     payment_method_values = get_field_values(payment_method_fields)
        #     payment_method_dict = dict(zip(payment_method_fields, payment_method_values))
        #     return payment_method_md.format(**payment_method_dict)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())