from PySide6 import QtCore, QtWidgets

## 必填 Entries
# start_date :合約起始日 (date)
# end_date：合約到期日 (date, but >= start_date)
# party_a_name: 甲方名稱 (combo box)
# party_a_representative (combo box, filtered by party_a_name)
# party_a_registered_address 甲方公司登記地址 (rich edit)
# party_b_name: 乙方名稱 (rich edit)
# party_b_representative (rich edit)
# party_b_registered_address 乙方公司登記地址 (rich edit)
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

def create_label(x):
    return QtWidgets.QLabel(x)

def create_popup_date_edit():
    date_edit = QtWidgets.QDateEdit(calendarPopup=True)
    date_edit.setDate(QtCore.QDate.currentDate())
    return date_edit

def create_combo_box():
    return QtWidgets.QComboBox()

def create_line_edit(x):
    line_edit = QtWidgets.QLineEdit()
    line_edit.setPlaceholderText(x)
    return line_edit

################################################

def start_date_widgets():
    label = create_label("Start Date")
    control = create_popup_date_edit()
    return [label, control]

def end_date_widgets():
    label = create_label("End Date")
    control = create_popup_date_edit()
    return [label, control]

party_a_name_list = ["Apple", "Google", "Microsoft"]

def party_a_name_widgets():
    label = create_label("Party A Name")
    control = create_combo_box()
    control.addItems(party_a_name_list)
    control.setCurrentIndex(-1)
    control.setPlaceholderText("--- Please select Party A Name ---")
    return [label, control]

def party_a_representative_widgets():
    label = create_label("Party A Representative")
    control = create_combo_box()
    return [label, control]

def party_a_registered_address_widgets():
    label = create_label("Party A Registered Address")
    control = create_line_edit("Party A Registered Address")
    return [label, control]

def party_b_name_widgets():
    label = create_label("Party B Name")
    control = create_line_edit("Party B Name")
    return [label, control]

def party_b_representative_widgets():
    label = create_label("Party B Representative")
    control = create_line_edit("Party B Representative")
    return [label, control]

def party_b_registered_address_widgets():
    label = create_label("Party B Registered Address")
    control = create_line_edit("Party B Registered Address")
    return [label, control]

def signature_date_widgets():
    label = create_label("Signature Date")
    control = create_popup_date_edit()
    return [label, control]

payment_method_list = ["逐筆結", "預存款", "雙週結"]

def payment_method_widgets():
    label = create_label("Payment Method")
    control = create_combo_box()
    control.addItems(payment_method_list)
    control.setPlaceholderText("--- Please select a payment method ---")
    control.setCurrentIndex(-1)
    return [label, control]

# currency (combo box 十幾種)
#   is_cross_border_payment (Yes/No radio button, always follow currency)
# def currency_widgets():
#     label = create_label("Currency")
#     control = create_combo_box()
#     return [label, control]

# def is_cross_border_payment_widgets():
#     label = create_label("Cross Border Payment")
#     yes_button = QtWidgets.QRadioButton("Yes")
#     no_button = QtWidgets.QRadioButton("No")
#     return [label, yes_button, no_button]
