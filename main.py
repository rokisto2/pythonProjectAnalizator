import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow
from start_window import Ui_MainWindow
from text_resource import labelINfo
from connector import Data
from main_window import Ui_MainWindow as Ui_MainWindow_main
import Calc


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.len = None
        self.ui_main = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.self_UI()
        self.k = 0
        self.analis = Calc.Сalculator()
        self.db = Data()
        self.db.create_query()

    def self_UI(self):
        self.ui.label.setText("Просто текстовая аннотация")
        self.ui.label_2.setText(labelINfo.info1)
        self.ui.pushButton.clicked.connect(self.pussh_start_button)

    def pussh_start_button(self):
        self.ui_main = Ui_MainWindow_main()
        self.ui_main.setupUi(self)
        self.self_UI_mainWindow()
        self.ui = None
        self.len = len(labelINfo.question1)

    def self_UI_mainWindow(self):
        self.ui_main.pushButton_9.clicked.connect(self.pussh_next_button)

    def pussh_next_button(self):
        print(self.k)


        if self.k < self.len - 1:
            self.ui_main.label_3.setText(labelINfo.question1[self.k+1])
            self.ui_main.label_4.setText(labelINfo.question2[self.k+1])
            self.ui_main.label_5.setText(labelINfo.question3[self.k+1])



        if self.k == 0:

            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addSosna(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 1:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addLarches(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 2:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addPixt(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 3:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addDub(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 4:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addBuk(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 5:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addBerez(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 6:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addLip(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 7:
            try:
                count = float(self.ui_main.lineEdit.text())
            except:
                count = 0
            try:
                height = float(self.ui_main.lineEdit_2.text())
            except:
                height = 0
            try:
                girth = float(self.ui_main.lineEdit_3.text())
            except:
                girth = 0
            self.analis.addTopol(count, height, girth)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")

        if self.k == 8:
            try:
                count1 = float(self.ui_main.lineEdit.text())
            except:
                count1 = 0
            try:
                count2 = float(self.ui_main.lineEdit_2.text())
            except:
                count2 = 0
            try:
                count3 = float(self.ui_main.lineEdit_3.text())
            except:
                count3 = 0
            self.analis.addOtherTrees25(count1)
            self.analis.addOtherTrees125(count2)
            self.analis.addOtherTrees(count3)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")
            self.ui_main.pushButton_9.setText("Рассчитать")

        if self.k == 9:
            try:
                count1 = float(self.ui_main.lineEdit.text())
            except:
                count1 = 0
            try:
                count2 = float(self.ui_main.lineEdit_2.text())
            except:
                count2 = 0
            try:
                count3 = float(self.ui_main.lineEdit_3.text())
            except:
                count3 = 0
            self.analis.addLichen(count1)
            self.analis.addTree(count2)
            self.analis.addSoil(count3)
            self.ui_main.lineEdit.setText("")
            self.ui_main.lineEdit_2.setText("")
            self.ui_main.lineEdit_3.setText("")


        if self.k == self.len-1:
            self.analis.calculate()
            self.ans = self.analis.get_project()
            self.ui_main.lineEdit.setFixedSize(QSize(0, 0))
            self.ui_main.lineEdit_2.setFixedSize(QSize(0, 0))
            self.ui_main.lineEdit_3.setFixedSize(QSize(0, 0))
            self.ui_main.label_3.setFixedSize(QSize(0, 0))
            self.ui_main.label_4.setFixedSize(QSize(0, 0))
            self.ui_main.label_5.setFixedSize(QSize(0, 0))

            self.ui_main.label_8.setFixedSize(QSize(891, 111))
            self.ui_main.label_9.setFixedSize(QSize(891, 111))
            self.ui_main.label_10.setFixedSize(QSize(891, 111))
            self.ui_main.label_11.setFixedSize(QSize(891, 111))
            self.ui_main.label_12.setFixedSize(QSize(891, 111))
            self.ui_main.label_13.setFixedSize(QSize(891, 111))
            self.ui_main.label_14.setFixedSize(QSize(891, 111))
            self.ui_main.label_8.setText(f"Итоговый ущерб растительности: {self.ans[0]} ₽")
            self.ui_main.label_9.setText(f"Ущерб древесным насаждениям: {self.ans[1]} ₽")
            self.ui_main.label_10.setText(f"Ущерб подросту растений: {self.ans[2]} ₽")
            self.ui_main.label_11.setText(f"Ущерб саженцам растений: {self.ans[3]} ₽")
            self.ui_main.label_12.setText(f"Необходимо для восстановления растительности на территории: {self.ans[4]} ₽")
            self.ui_main.label_13.setText(f"Восстановление мест произрастания лишайниковых форм растительности: {self.ans[5]} ₽")
            self.ui_main.label_14.setText(f"Необходимо для рекультивации нарушенных земель: {self.ans[6]} ₽")
            self.ui_main.pushButton_9.setText(f"Сохранить")
        self.k += 1
        if self.ui_main.pushButton_9.text() == "Сохранить":
            self.db.add_project(self.ans)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
