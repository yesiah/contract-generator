import sys
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())