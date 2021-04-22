import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QDate

from contract_generator_model import Ui_MainWindow

from templates.contract_templates.cht import cht_contract_template

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
            self.ui.contract_template_selector.addItems(cht_contract_template.templates.keys())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())