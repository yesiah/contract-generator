import os
import sys
import pathlib

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QDate

from contract_generator_model import Ui_MainWindow

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

            template_path = "templates/contract_templates/" + {
                u"\u7e41\u9ad4\u4e2d\u6587": "cht",
                u"English": "en",
                u"\u65e5\u672c\u8a9e": "ja",
                u"\ud55c\uad6d\uc5b4": "ko"
            }.get(self.ui.lang_selector.currentText())

            path = os.walk(template_path)
            for _, _, files in path:
                for f in files:
                    p = pathlib.Path(f)
                    if p.suffix == ".txt":
                        self.ui.contract_template_selector.addItem(p.stem)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())