import os
import sys
import pathlib

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QDate

from contract_generator_model import Ui_MainWindow

def get_contract_template_path(lang):
    return "templates/contract_templates/" + {
        u"\u7e41\u9ad4\u4e2d\u6587": "cht",
        u"English": "en",
        u"\u65e5\u672c\u8a9e": "ja",
        u"\ud55c\uad6d\uc5b4": "ko"
    }.get(lang, "cht")

def get_payment_method_template_path(lang):
    return "templates/payment_method_templates/" + {
        u"\u7e41\u9ad4\u4e2d\u6587": "cht",
        u"English": "en",
        u"\u65e5\u672c\u8a9e": "ja",
        u"\ud55c\uad6d\uc5b4": "ko"
    }.get(lang, "cht")


from string import Formatter
def parse_fields(template_path):
    if os.path.exists(template_path):
        with open(template_path, 'rb') as f:
            txt = f.read().decode('UTF-8')
            return set(fname for _, fname, _, _ in Formatter().parse(txt) if fname)
    
    return []

def enable_controls(control_list):
    for control in control_list:
        control.setEnabled(True)

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

            template_path = get_contract_template_path(self.ui.lang_selector.currentText())
            path = os.walk(template_path)
            for _, _, files in path:
                for f in files:
                    p = pathlib.Path(f)
                    if p.suffix == ".template":
                        self.ui.contract_template_selector.addItem(p.stem)
    
    def on_contract_template_selector_changed(self):
        template_path = os.path.join(get_contract_template_path(self.ui.lang_selector.currentText()), self.ui.contract_template_selector.currentText() + ".template")
        fields = parse_fields(template_path)
        self.enable_fields(fields)

        if self.ui.payment_method_selector.isEnabled():
            self.ui.payment_method_selector.clear()
            payment_method_template_path = get_payment_method_template_path(self.ui.lang_selector.currentText())
            for _, _, files in os.walk(payment_method_template_path):
                for f in files:
                    p = pathlib.Path(f)
                    if p.suffix == ".template":
                        self.ui.payment_method_selector.addItem(p.stem)

    def on_payment_method_selector_changed(self):
        template_path = os.path.join(get_payment_method_template_path(self.ui.lang_selector.currentText()), self.ui.payment_method_selector.currentText() + ".template")
        fields = parse_fields(template_path)
        self.enable_fields(fields)

    def enable_fields(self, fields):
        for field in fields:
            enable_controls(self.field2control(field))
    
    def field2control(self, field):
        return {
            "start_date": [self.ui.start_date_label, self.ui.start_date_selector],
            "end_date": [self.ui.end_date_label, self.ui.end_date_selector],
            "party_a_name": [self.ui.party_a_name_label, self.ui.party_a_name_selector],
            "party_a_representative": [self.ui.party_a_representative_label, self.ui.party_a_representative_selector],
            "party_a_registered_address": [self.ui.party_a_registered_address_label, self.ui.party_a_registered_address_edit],
            "party_b_name": [self.ui.party_b_name_label, self.ui.party_b_name_edit],
            "party_b_representative": [self.ui.party_b_representative_label, self.ui.party_b_representative_edit],
            "party_b_registered_address": [self.ui.party_b_registered_address_label, self.ui.party_b_registered_address_edit],
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())