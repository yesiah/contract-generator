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
        MainWindow.resize(794, 680)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 769, 732))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 7, 1, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_9, 8, 0, 1, 1)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 12, 0, 1, 1)

        self.dateEdit = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateEdit, 10, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.dateEdit_3 = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateEdit_3, 13, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_8, 7, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)

        self.gridLayout_3.addWidget(self.dateEdit_2, 11, 1, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 6, 0, 1, 1)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 11, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_10, 13, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 3, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setLayoutDirection(Qt.LeftToRight)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 10, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 4, 1, 1, 3)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 8, 1, 1, 3)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_9, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 1, 2, 1, 1)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 1, 1, 1, 1)

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

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_9, 0, 8, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_2.addWidget(self.comboBox_4, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 131, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)


        self.gridLayout_2.addWidget(self.groupBox, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 0, 1, 1, 3)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 2, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 1, 1, 3)

        self.label_18 = QLabel(self.scrollAreaWidgetContents)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 3, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 3, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 4, 2, 1, 1)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 2, 2, 1, 1)

        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 3, 3, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 4, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 4, 1, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 20, 391, 41))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton_3 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_3.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_3.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_3.addWidget(self.radioButton_6)


        self.gridLayout.addWidget(self.groupBox_2, 5, 0, 1, 3)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout.addWidget(self.lineEdit_12, 4, 3, 1, 1)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout.addWidget(self.lineEdit_13, 5, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Contract Generator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Representative ---", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Party B Registered Address", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Name ---", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Select a language ---", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Party B Representative", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Party A Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Party B Name", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Party A Name ---", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Party A Representative", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Signature Date", None))
        self.comboBox_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Party A Representative ---", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Party A Registered Address", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party A Registered Address ---", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  --- Party B Registered Address ---", None))
        self.comboBox_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Currency ---", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Payment Method", None))
        self.comboBox_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"--- Payment Method ---", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Cross Border Payment", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Branch Code", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Country of the Bank<br/>Receiving the Payment</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bank Account", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bank Code", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Name of the Bank", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Swift Code", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Name of the Branch", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Other Code", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"CNAPS", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"SKN CODE", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"BSB NUMBER", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"IBAN CODE", None))
    # retranslateUi

