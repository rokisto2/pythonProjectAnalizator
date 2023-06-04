import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from start_window import Ui_MainWindow
from text_resource import  labelINfo

class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.self_UI()

    def self_UI(self):
        self.ui.label.setText("Просто текстовая аннотация")
        self.ui.label_2.setText(labelINfo.info1)
        self.ui.pushButton.clicked.connect(self.pussh_start_button)

    def pussh_start_button(self):
        print(1)
        app.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())

#Arrial regular