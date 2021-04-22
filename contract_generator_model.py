# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contract_generator.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 682)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 600, 171, 41))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 771, 581))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 810))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 9, 0, 1, 1)

        self.party_a_representative_selector = QComboBox(self.scrollAreaWidgetContents)
        self.party_a_representative_selector.setObjectName(u"party_a_representative_selector")
        self.party_a_representative_selector.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_a_representative_selector, 7, 1, 1, 1)

        self.party_a_registered_address_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.party_a_registered_address_edit.setObjectName(u"party_a_registered_address_edit")
        self.party_a_registered_address_edit.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_a_registered_address_edit, 8, 1, 1, 3)

        self.party_b_name_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.party_b_name_edit.setObjectName(u"party_b_name_edit")
        self.party_b_name_edit.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_b_name_edit, 10, 1, 1, 1)

        self.party_a_representative_label = QLabel(self.scrollAreaWidgetContents)
        self.party_a_representative_label.setObjectName(u"party_a_representative_label")
        self.party_a_representative_label.setEnabled(False)
        self.party_a_representative_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_a_representative_label, 7, 0, 1, 1)

        self.start_date_selector = QDateEdit(self.scrollAreaWidgetContents)
        self.start_date_selector.setObjectName(u"start_date_selector")
        self.start_date_selector.setEnabled(False)
        self.start_date_selector.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.start_date_selector.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.start_date_selector, 14, 1, 1, 1)

        self.party_b_representative_label = QLabel(self.scrollAreaWidgetContents)
        self.party_b_representative_label.setObjectName(u"party_b_representative_label")
        self.party_b_representative_label.setEnabled(False)
        self.party_b_representative_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_b_representative_label, 11, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 13, 0, 1, 1)

        self.party_b_name_label = QLabel(self.scrollAreaWidgetContents)
        self.party_b_name_label.setObjectName(u"party_b_name_label")
        self.party_b_name_label.setEnabled(False)
        self.party_b_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_b_name_label, 10, 0, 1, 1)

        self.party_a_registered_address_label = QLabel(self.scrollAreaWidgetContents)
        self.party_a_registered_address_label.setObjectName(u"party_a_registered_address_label")
        self.party_a_registered_address_label.setEnabled(False)
        self.party_a_registered_address_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_a_registered_address_label, 8, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 5, 1, 1, 1)

        self.end_date_label = QLabel(self.scrollAreaWidgetContents)
        self.end_date_label.setObjectName(u"end_date_label")
        self.end_date_label.setEnabled(False)
        self.end_date_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.end_date_label, 15, 0, 1, 1)

        self.party_a_name_selector = QComboBox(self.scrollAreaWidgetContents)
        self.party_a_name_selector.setObjectName(u"party_a_name_selector")
        self.party_a_name_selector.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_a_name_selector, 6, 1, 1, 1)

        self.contract_template_selector = QComboBox(self.scrollAreaWidgetContents)
        self.contract_template_selector.setObjectName(u"contract_template_selector")
        self.contract_template_selector.setEnabled(False)

        self.gridLayout_3.addWidget(self.contract_template_selector, 4, 1, 1, 1)

        self.signature_date_label = QLabel(self.scrollAreaWidgetContents)
        self.signature_date_label.setObjectName(u"signature_date_label")
        self.signature_date_label.setEnabled(False)
        self.signature_date_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.signature_date_label, 17, 0, 1, 1)

        self.party_b_representative_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.party_b_representative_edit.setObjectName(u"party_b_representative_edit")
        self.party_b_representative_edit.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_b_representative_edit, 11, 1, 1, 1)

        self.start_date_label = QLabel(self.scrollAreaWidgetContents)
        self.start_date_label.setObjectName(u"start_date_label")
        self.start_date_label.setEnabled(False)
        self.start_date_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.start_date_label, 14, 0, 1, 1)

        self.party_a_name_label = QLabel(self.scrollAreaWidgetContents)
        self.party_a_name_label.setObjectName(u"party_a_name_label")
        self.party_a_name_label.setEnabled(False)
        self.party_a_name_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_a_name_label, 6, 0, 1, 1)

        self.end_date_selector = QDateEdit(self.scrollAreaWidgetContents)
        self.end_date_selector.setObjectName(u"end_date_selector")
        self.end_date_selector.setEnabled(False)
        self.end_date_selector.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.end_date_selector, 15, 1, 1, 1)

        self.party_b_registered_address_label = QLabel(self.scrollAreaWidgetContents)
        self.party_b_registered_address_label.setObjectName(u"party_b_registered_address_label")
        self.party_b_registered_address_label.setEnabled(False)
        self.party_b_registered_address_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.party_b_registered_address_label, 12, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 16, 0, 1, 1)

        self.party_b_registered_address_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.party_b_registered_address_edit.setObjectName(u"party_b_registered_address_edit")
        self.party_b_registered_address_edit.setEnabled(False)

        self.gridLayout_3.addWidget(self.party_b_registered_address_edit, 12, 1, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.signature_date_selector = QDateEdit(self.scrollAreaWidgetContents)
        self.signature_date_selector.setObjectName(u"signature_date_selector")
        self.signature_date_selector.setEnabled(False)
        self.signature_date_selector.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.signature_date_selector, 17, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 1, 0, 1, 1)

        self.lang_label = QLabel(self.scrollAreaWidgetContents)
        self.lang_label.setObjectName(u"lang_label")
        self.lang_label.setLayoutDirection(Qt.LeftToRight)
        self.lang_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lang_label, 2, 0, 1, 1)

        self.lang_selector = QComboBox(self.scrollAreaWidgetContents)
        self.lang_selector.addItem("")
        self.lang_selector.addItem("")
        self.lang_selector.addItem("")
        self.lang_selector.addItem("")
        self.lang_selector.setObjectName(u"lang_selector")

        self.gridLayout_3.addWidget(self.lang_selector, 2, 1, 1, 1)

        self.contract_template_label = QLabel(self.scrollAreaWidgetContents)
        self.contract_template_label.setObjectName(u"contract_template_label")
        self.contract_template_label.setEnabled(False)
        self.contract_template_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.contract_template_label, 4, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.currency_selector = QComboBox(self.scrollAreaWidgetContents)
        self.currency_selector.setObjectName(u"currency_selector")
        self.currency_selector.setEnabled(False)

        self.gridLayout_2.addWidget(self.currency_selector, 1, 2, 1, 1)

        self.currency_label = QLabel(self.scrollAreaWidgetContents)
        self.currency_label.setObjectName(u"currency_label")
        self.currency_label.setEnabled(False)
        self.currency_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.currency_label, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 0, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 0, 5, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 0, 6, 1, 1)

        self.payment_method_label = QLabel(self.scrollAreaWidgetContents)
        self.payment_method_label.setObjectName(u"payment_method_label")
        self.payment_method_label.setEnabled(False)

        self.gridLayout_2.addWidget(self.payment_method_label, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 8, 1, 1)

        self.payment_method_selector = QComboBox(self.scrollAreaWidgetContents)
        self.payment_method_selector.setObjectName(u"payment_method_selector")
        self.payment_method_selector.setEnabled(False)

        self.gridLayout_2.addWidget(self.payment_method_selector, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.cross_boader_payment_group = QGroupBox(self.scrollAreaWidgetContents)
        self.cross_boader_payment_group.setObjectName(u"cross_boader_payment_group")
        self.cross_boader_payment_group.setEnabled(False)
        self.cross_boader_payment_group.setMinimumSize(QSize(0, 50))
        self.horizontalLayoutWidget_2 = QWidget(self.cross_boader_payment_group)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 131, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cross_border_payment_yes = QRadioButton(self.horizontalLayoutWidget_2)
        self.cross_border_payment_yes.setObjectName(u"cross_border_payment_yes")

        self.horizontalLayout.addWidget(self.cross_border_payment_yes)

        self.cross_border_payment_no = QRadioButton(self.horizontalLayoutWidget_2)
        self.cross_border_payment_no.setObjectName(u"cross_border_payment_no")

        self.horizontalLayout.addWidget(self.cross_border_payment_no)


        self.gridLayout_2.addWidget(self.cross_boader_payment_group, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bank_account_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.bank_account_edit.setObjectName(u"bank_account_edit")
        self.bank_account_edit.setEnabled(False)

        self.gridLayout.addWidget(self.bank_account_edit, 0, 1, 1, 3)

        self.account_name_label = QLabel(self.scrollAreaWidgetContents)
        self.account_name_label.setObjectName(u"account_name_label")
        self.account_name_label.setEnabled(False)

        self.gridLayout.addWidget(self.account_name_label, 1, 0, 1, 1)

        self.bank_code_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.bank_code_edit.setObjectName(u"bank_code_edit")
        self.bank_code_edit.setEnabled(False)

        self.gridLayout.addWidget(self.bank_code_edit, 2, 3, 1, 1)

        self.name_of_the_bank_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.name_of_the_bank_edit.setObjectName(u"name_of_the_bank_edit")
        self.name_of_the_bank_edit.setEnabled(False)

        self.gridLayout.addWidget(self.name_of_the_bank_edit, 2, 1, 1, 1)

        self.account_name_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.account_name_edit.setObjectName(u"account_name_edit")
        self.account_name_edit.setEnabled(False)

        self.gridLayout.addWidget(self.account_name_edit, 1, 1, 1, 3)

        self.branch_code_label = QLabel(self.scrollAreaWidgetContents)
        self.branch_code_label.setObjectName(u"branch_code_label")
        self.branch_code_label.setEnabled(False)

        self.gridLayout.addWidget(self.branch_code_label, 3, 2, 1, 1)

        self.name_of_the_branch_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.name_of_the_branch_edit.setObjectName(u"name_of_the_branch_edit")
        self.name_of_the_branch_edit.setEnabled(False)

        self.gridLayout.addWidget(self.name_of_the_branch_edit, 3, 1, 1, 1)

        self.country_of_the_bank_receiving_the_payment_label = QLabel(self.scrollAreaWidgetContents)
        self.country_of_the_bank_receiving_the_payment_label.setObjectName(u"country_of_the_bank_receiving_the_payment_label")
        self.country_of_the_bank_receiving_the_payment_label.setEnabled(False)

        self.gridLayout.addWidget(self.country_of_the_bank_receiving_the_payment_label, 4, 2, 1, 1)

        self.bank_account_label = QLabel(self.scrollAreaWidgetContents)
        self.bank_account_label.setObjectName(u"bank_account_label")
        self.bank_account_label.setEnabled(False)

        self.gridLayout.addWidget(self.bank_account_label, 0, 0, 1, 1)

        self.bank_code_label = QLabel(self.scrollAreaWidgetContents)
        self.bank_code_label.setObjectName(u"bank_code_label")
        self.bank_code_label.setEnabled(False)

        self.gridLayout.addWidget(self.bank_code_label, 2, 2, 1, 1)

        self.name_of_the_bank_label = QLabel(self.scrollAreaWidgetContents)
        self.name_of_the_bank_label.setObjectName(u"name_of_the_bank_label")
        self.name_of_the_bank_label.setEnabled(False)

        self.gridLayout.addWidget(self.name_of_the_bank_label, 2, 0, 1, 1)

        self.branch_code_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.branch_code_edit.setObjectName(u"branch_code_edit")
        self.branch_code_edit.setEnabled(False)

        self.gridLayout.addWidget(self.branch_code_edit, 3, 3, 1, 1)

        self.swift_code_label = QLabel(self.scrollAreaWidgetContents)
        self.swift_code_label.setObjectName(u"swift_code_label")
        self.swift_code_label.setEnabled(False)

        self.gridLayout.addWidget(self.swift_code_label, 4, 0, 1, 1)

        self.swift_code_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.swift_code_edit.setObjectName(u"swift_code_edit")
        self.swift_code_edit.setEnabled(False)

        self.gridLayout.addWidget(self.swift_code_edit, 4, 1, 1, 1)

        self.name_of_the_branch_label = QLabel(self.scrollAreaWidgetContents)
        self.name_of_the_branch_label.setObjectName(u"name_of_the_branch_label")
        self.name_of_the_branch_label.setEnabled(False)

        self.gridLayout.addWidget(self.name_of_the_branch_label, 3, 0, 1, 1)

        self.other_code_group = QGroupBox(self.scrollAreaWidgetContents)
        self.other_code_group.setObjectName(u"other_code_group")
        self.other_code_group.setEnabled(False)
        self.other_code_group.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(12)
        self.other_code_group.setFont(font)
        self.horizontalLayoutWidget_3 = QWidget(self.other_code_group)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setEnabled(False)
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 20, 391, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.other_code_cnaps = QRadioButton(self.horizontalLayoutWidget_3)
        self.other_code_cnaps.setObjectName(u"other_code_cnaps")

        self.horizontalLayout_3.addWidget(self.other_code_cnaps)

        self.other_code_skn_code = QRadioButton(self.horizontalLayoutWidget_3)
        self.other_code_skn_code.setObjectName(u"other_code_skn_code")
        self.other_code_skn_code.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.other_code_skn_code)

        self.other_code_bsb_number = QRadioButton(self.horizontalLayoutWidget_3)
        self.other_code_bsb_number.setObjectName(u"other_code_bsb_number")
        self.other_code_bsb_number.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.other_code_bsb_number)

        self.other_code_iban_code = QRadioButton(self.horizontalLayoutWidget_3)
        self.other_code_iban_code.setObjectName(u"other_code_iban_code")
        self.other_code_iban_code.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.other_code_iban_code)


        self.gridLayout.addWidget(self.other_code_group, 5, 0, 1, 3)

        self.country_of_the_bank_receiving_the_payment_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.country_of_the_bank_receiving_the_payment_edit.setObjectName(u"country_of_the_bank_receiving_the_payment_edit")
        self.country_of_the_bank_receiving_the_payment_edit.setEnabled(False)

        self.gridLayout.addWidget(self.country_of_the_bank_receiving_the_payment_edit, 4, 3, 1, 1)

        self.other_code_edit = QLineEdit(self.scrollAreaWidgetContents)
        self.other_code_edit.setObjectName(u"other_code_edit")
        self.other_code_edit.setEnabled(False)

        self.gridLayout.addWidget(self.other_code_edit, 5, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 791, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.lang_selector.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Contract Generator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.party_a_representative_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Party A Representative ---", None))
        self.party_a_registered_address_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party A Registered Address ---", None))
        self.party_b_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Name ---", None))
        self.party_a_representative_label.setText(QCoreApplication.translate("MainWindow", u"Party A Representative", None))
        self.party_b_representative_label.setText(QCoreApplication.translate("MainWindow", u"Party B Representative", None))
        self.party_b_name_label.setText(QCoreApplication.translate("MainWindow", u"Party B Name", None))
        self.party_a_registered_address_label.setText(QCoreApplication.translate("MainWindow", u"Party A Registered Address", None))
        self.end_date_label.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.party_a_name_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Party A Name ---", None))
        self.contract_template_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Select a Contract Template ---", None))
        self.signature_date_label.setText(QCoreApplication.translate("MainWindow", u"Signature Date", None))
        self.party_b_representative_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Representative ---", None))
        self.start_date_label.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.party_a_name_label.setText(QCoreApplication.translate("MainWindow", u"Party A Name", None))
        self.party_b_registered_address_label.setText(QCoreApplication.translate("MainWindow", u"Party B Registered Address", None))
        self.party_b_registered_address_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Registered Address ---", None))
        self.lang_label.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.lang_selector.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7e41\u9ad4\u4e2d\u6587", None))
        self.lang_selector.setItemText(1, QCoreApplication.translate("MainWindow", u"English", None))
        self.lang_selector.setItemText(2, QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e", None))
        self.lang_selector.setItemText(3, QCoreApplication.translate("MainWindow", u"\ud55c\uad6d\uc5b4", None))

        self.lang_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Select a Language ---", None))
        self.contract_template_label.setText(QCoreApplication.translate("MainWindow", u"Contract Template", None))
        self.currency_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Currency ---", None))
        self.currency_label.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.payment_method_label.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None))
        self.payment_method_selector.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Payment Method ---", None))
        self.cross_boader_payment_group.setTitle(QCoreApplication.translate("MainWindow", u"Cross Border Payment", None))
        self.cross_border_payment_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.cross_border_payment_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.bank_account_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Bank Account ---", None))
        self.account_name_label.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.bank_code_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Bank Code ---", None))
        self.name_of_the_bank_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Name of the Bank ---", None))
        self.account_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Account Name ---", None))
        self.branch_code_label.setText(QCoreApplication.translate("MainWindow", u"Branch Code", None))
        self.name_of_the_branch_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Name of the Branch ---", None))
        self.country_of_the_bank_receiving_the_payment_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Country of the Bank<br/>Receiving the Payment</p></body></html>", None))
        self.bank_account_label.setText(QCoreApplication.translate("MainWindow", u"Bank Account", None))
        self.bank_code_label.setText(QCoreApplication.translate("MainWindow", u"Bank Code", None))
        self.name_of_the_bank_label.setText(QCoreApplication.translate("MainWindow", u"Name of the Bank", None))
        self.branch_code_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Branch Code ---", None))
        self.swift_code_label.setText(QCoreApplication.translate("MainWindow", u"Swift Code", None))
        self.swift_code_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Swift Code (optional) --- ", None))
        self.name_of_the_branch_label.setText(QCoreApplication.translate("MainWindow", u"Name of the Branch", None))
        self.other_code_group.setTitle(QCoreApplication.translate("MainWindow", u"Other Code", None))
        self.other_code_cnaps.setText(QCoreApplication.translate("MainWindow", u"CNAPS", None))
        self.other_code_skn_code.setText(QCoreApplication.translate("MainWindow", u"SKN CODE", None))
        self.other_code_bsb_number.setText(QCoreApplication.translate("MainWindow", u"BSB NUMBER", None))
        self.other_code_iban_code.setText(QCoreApplication.translate("MainWindow", u"IBAN CODE", None))
        self.country_of_the_bank_receiving_the_payment_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Country of the Bank Receiving the Payment ---", None))
        self.other_code_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Other Code (optional) ---", None))
    # retranslateUi

