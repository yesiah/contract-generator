import sys
import enum
import pathlib
from PySide6 import QtCore, QtWidgets

import field_widget
from string import Formatter
import pdf

class Field(enum.Enum):
    StartDate = 1,
    EndDate = 2,
    PartyAName = 3,
    PartyARepresentative = 4,
    PartyARegisteredAddress = 5,
    PartyBName = 6,
    PartyBRepresentative = 7,
    PartyBRegisteredAddress = 8,
    SignatureDate = 9,
    PaymentMethod = 10,
    Currency = 11

def token2keywidget(x):
    return {
        "start_date": (Field.StartDate, field_widget.start_date_widgets()),
        "end_date": (Field.EndDate, field_widget.end_date_widgets()),
        "party_a_name": (Field.PartyAName, field_widget.party_a_name_widgets()),
        "party_a_representative": (Field.PartyARepresentative, field_widget.party_a_representative_widgets()),
        "party_a_registered_address": (Field.PartyARegisteredAddress, field_widget.party_a_registered_address_widgets()),
        "party_b_name": (Field.PartyBName, field_widget.party_b_name_widgets()),
        "party_b_representative": (Field.PartyBRepresentative, field_widget.party_b_representative_widgets()),
        "party_b_registered_address": (Field.PartyBRegisteredAddress, field_widget.party_b_registered_address_widgets()),
        "signature_date": (Field.SignatureDate, field_widget.signature_date_widgets()),
        "payment_method": (Field.PaymentMethod, field_widget.signature_date_widgets())
    }.get(x)

def zh_tw_locale():
    return QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.TraditionalChineseScript, QtCore.QLocale.Taiwan)

def zh_tw_date_format():
    return "yyyy 年 MM 月 dd 日"

def en_us_locale():
    return QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates)

def en_us_date_format():
    return "MMMM dd, yyyy"

def ja_jp_locale():
    return QtCore.QLocale(QtCore.QLocale.Japanese, QtCore.QLocale.Japan)

def ja_jp_date_format():
    return "yyyy 年 MM 月 dd 日"

def ko_kr_locale():
    return QtCore.QLocale(QtCore.QLocale.Korean, QtCore.QLocale.SouthKorea)

def ko_kr_date_format():
    return "yyyy 년 MM 월 dd 일"

def sel_locale(x):
    return {
        "繁體中文": zh_tw_locale(), 
        "English": en_us_locale(), 
        "日本語": ja_jp_locale(),
        "한국어": ko_kr_locale()
    }.get(x, en_us_locale())  

def sel_date_format(x):
    return {
        "繁體中文": zh_tw_date_format(), 
        "English": en_us_date_format(), 
        "日本語": ja_jp_date_format(),
        "한국어": ko_kr_date_format()
    }.get(x, en_us_date_format())  

def sel_locale_and_date_format(x):
    return (sel_locale(x), sel_date_format(x))

def pop_up_done_message():
    done_message_box = QtWidgets.QMessageBox(text="Done!")
    done_message_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
    done_message_box.exec_()

def parse_fields(template_path):
    with open(template_path, 'rb') as f:
        txt = f.read().decode('UTF-8')
        return set(fname for _, fname, _, _ in Formatter().parse(txt) if fname)

def texts_pass_one(template_path, party_a_name, party_b_name, start_date, signature_date):
    with open(template_path, 'rb') as template_file:
        txt = template_file.read().decode('UTF-8')
        txt = txt.format(party_a_name=party_a_name, party_b_name=party_b_name, start_date=start_date, signature_date=signature_date)
        return txt

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contract generator")

        # Language
        self.lang = QtWidgets.QLabel("Language")
        self.lang_selector = QtWidgets.QComboBox()
        self.lang_selector.addItems(["繁體中文", "English", "日本語", "한국어"])

        # Link elements
        self.layout = QtWidgets.QGridLayout(self)
        self.layout.addWidget(self.lang, 0, 0)
        self.layout.addWidget(self.lang_selector, 0, 1)

        self.layout.setRowMinimumHeight(1, 15)

        dynamic_fields = sorted(parse_fields("/Users/yhh/projects/kkday-auto-pdf/contract-templates/cht/中文契約範本.txt"))
        row = 2
        self.widget_dict = dict(map(token2keywidget, dynamic_fields))
        for widgets in self.widget_dict.values():
            col = 0
            for widget in widgets:
                self.layout.addWidget(widget, row, col)
                col = col + 1
            row = row + 1

        self.execute_button = QtWidgets.QPushButton("Execute")
        self.execute_button.clicked.connect(self.on_execute)
        self.layout.addWidget(self.execute_button, row, 0, 1, 2)

    def show_done(self):
        pop_up_done_message()

    def generate_text(self):
        party_a_name = self.widget_dict[Field.PartyAName][1].currentText()
        party_b_name = self.widget_dict[Field.PartyBName][1].text()
        curr_locale, date_fmt = sel_locale_and_date_format(self.lang_selector.currentText())
        start_date = curr_locale.toString(self.widget_dict[Field.StartDate][1].date(), date_fmt)
        signature_date = curr_locale.toString(self.widget_dict[Field.SignatureDate][1].date(), date_fmt)

        root_path = pathlib.Path(__file__).parent.absolute()
        template_path = root_path / "contract-templates/cht/中文契約範本.txt"
        txt = texts_pass_one(template_path, party_a_name, party_b_name, start_date, signature_date)
        return txt

    @QtCore.Slot()
    def on_execute(self):
        txt = self.generate_text()
        pdf.generate(txt)
        self.show_done()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
