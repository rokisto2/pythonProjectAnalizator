# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 918)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1300, 918))
        self.label.setPixmap(QPixmap(u":/fon/resurce/2.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 338, 916))
        self.label_2.setStyleSheet(u"/* Rectangle 2 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 916px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"background: #009158;\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 177, 338, 80))
        self.pushButton.setTabletTracking(False)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"/* Rectangle 4 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 80px;\n"
"left: 0px;\n"
"top: 177px;\n"
"\n"
"background: #007743;\n"
"\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/fon/resurce/\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 803, 338, 121))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/fon/resurce/\u041d\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0443.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(0, 253, 0, 0))
        self.pushButton_3.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/fon/resurce/\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0438\u0306_\u043f\u0440\u043e\u0435\u043a\u0442_\u041c\u043e\u043d\u0442\u0430\u0436\u043d\u0430\u044f_\u043e\u0431\u043b\u0430\u0441\u0442\u044c_1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(40, 40))
        self.pushButton_3.setFlat(True)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(479, 767, 700, 98))
        self.pushButton_9.setStyleSheet(u"/* Button */\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: 479px;\n"
"top: 767px;\n"
"\n"
"\n"
"\n"
"/* Rectangle 1 */\n"
"\n"
"box-sizing: border-box;\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: calc(50% - 700px/2 + 171.5px);\n"
"top: 767px;\n"
"\n"
"background: #009158;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 13px;\n"
"\n"
"\n"
"/* \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c */\n"
"\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 44px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 80, 871, 71))
        self.label_3.setStyleSheet(u"font-family: 'Inter';\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_3.setWordWrap(True)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(370, 170, 411, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 220, 841, 81))
        self.label_4.setStyleSheet(u"font-family: 'Inter';\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_4.setWordWrap(True)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(370, 320, 411, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(370, 380, 921, 61))
        self.label_5.setStyleSheet(u"font-family: 'Inter';\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"")
        self.label_5.setLineWidth(1)
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(370, 470, 411, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 121, 121))
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_6.setPixmap(QPixmap(u":/fon/resurce/\u041b\u043e\u0433\u043e.svg"))
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(150, 50, 141, 81))
        self.label_7.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(370, 30, 0, 0))
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_8.setWordWrap(True)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(370, 140, 0, 0))
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_9.setWordWrap(True)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(370, 240, 0, 0))
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_10.setWordWrap(True)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(370, 340, 0, 0))
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_11.setWordWrap(True)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(370, 440, 0, 0))
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_12.setWordWrap(True)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(370, 540, 0, 0))
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_13.setWordWrap(True)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(370, 640, 0, 0))
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 25px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;")
        self.label_14.setWordWrap(True)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(0, 340, 0, 0))
        self.pushButton_4.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(40, 40))
        self.pushButton_4.setFlat(True)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(0, 420, 0, 0))
        self.pushButton_5.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.pushButton_5.setIcon(icon2)
        self.pushButton_5.setIconSize(QSize(40, 40))
        self.pushButton_5.setFlat(True)
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(0, 510, 0, 0))
        self.pushButton_6.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(40, 40))
        self.pushButton_6.setFlat(True)
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(0, 610, 0, 0))
        self.pushButton_7.setStyleSheet(u"/* Rectangle 6 */\n"
"\n"
"position: absolute;\n"
"width: 338px;\n"
"height: 104px;\n"
"left: 0px;\n"
"top: 810px;\n"
"\n"
"background: #009158;\n"
"/* \u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 330px;\n"
"height: 74px;\n"
"left: 8px;\n"
"top: 818px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 27px;\n"
"line-height: 33px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"\n"
"")
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(40, 40))
        self.pushButton_7.setFlat(True)
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(480, 770, 700, 98))
        self.pushButton_10.setStyleSheet(u"/* Button */\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: 479px;\n"
"top: 767px;\n"
"\n"
"\n"
"\n"
"/* Rectangle 1 */\n"
"\n"
"box-sizing: border-box;\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: calc(50% - 700px/2 + 171.5px);\n"
"top: 767px;\n"
"\n"
"background: #009158;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 13px;\n"
"\n"
"\n"
"/* \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c */\n"
"\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 44px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(480, 770, 700, 98))
        self.pushButton_11.setStyleSheet(u"/* Button */\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: 479px;\n"
"top: 767px;\n"
"\n"
"\n"
"\n"
"/* Rectangle 1 */\n"
"\n"
"box-sizing: border-box;\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: calc(50% - 700px/2 + 171.5px);\n"
"top: 767px;\n"
"\n"
"background: #009158;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25), 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 13px;\n"
"\n"
"\n"
"/* \u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c */\n"
"\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 695px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 44px;\n"
"line-height: 53px;\n"
"text-align: center;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_9.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.label_5.raise_()
        self.lineEdit_3.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_8.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()

        self.retranslateUi(MainWindow)

        self.pushButton_2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u044f\u0437\u0430\u0442\u044c\u0441\u044f \u0441 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u0447\u0438\u043a\u0430\u043c\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0441\u0435\u043d \u0432\u044b\u0448\u0435 2,5 \u043c\u0435\u0442\u0440\u043e\u0432 \u0432 \u0432\u044b\u0441\u043e\u0442\u0443", None))
        self.lineEdit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0432\u044b\u0441\u043e\u0442\u0430 \u0441\u043e\u0441\u0435\u043d \u0432\u044b\u0448\u0435 2,5 \u043c\u0435\u0442\u0440\u043e\u0432", None))
        self.lineEdit_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u0438\u0439 \u043e\u0431\u0445\u0432\u0430\u0442 \u0441\u0442\u0432\u043e\u043b\u0430 \u0441\u043e\u0441\u0435\u043d \u0432\u044b\u0448\u0435 2,5 \u043c\u0435\u0442\u0440\u043e\u0432 (\u043d\u0430 \u0432\u044b\u0441\u043e\u0442\u0435 1,3 \u043c\u0435\u0442\u0440\u0430 \u043e\u0442 \u0448\u0435\u0439\u043a\u0438 \u043a\u043e\u0440\u043d\u044f)", None))
        self.lineEdit_3.setText("")
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0443\u0434\u0440\u043e 1.0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433\u043e\u0432\u044b\u0439 \u0443\u0449\u0435\u0440\u0431 \u0440\u0430\u0441\u0442\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0449\u0435\u0440\u0431 \u0434\u0440\u0435\u0432\u0435\u0441\u043d\u044b\u043c \u043d\u0430\u0441\u0430\u0436\u0434\u0435\u043d\u0438\u044f\u043c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0449\u0435\u0440\u0431 \u043f\u043e\u0434\u0440\u043e\u0441\u0442\u0443 \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0449\u0435\u0440\u0431 \u0441\u0430\u0436\u0435\u043d\u0446\u0430\u043c \u0440\u0430\u0441\u0442\u0435\u043d\u0438\u0439", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0434\u043b\u044f \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0441\u0442\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 \u043d\u0430 \u0442\u0435\u0440\u0440\u0438\u0442\u043e\u0440\u0438\u0438", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043c\u0435\u0441\u0442 \u043f\u0440\u043e\u0438\u0437\u0440\u0430\u0441\u0442\u0430\u043d\u0438\u044f \u043b\u0438\u0448\u0430\u0439\u043d\u0438\u043a\u043e\u0432\u044b\u0445 \u0444\u043e\u0440\u043c \n"
"\u0440\u0430\u0441\u0442\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u0434\u043b\u044f \u0440\u0435\u043a\u0443\u043b\u044c\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u043d\u044b\u0445 \u0437\u0435\u043c\u0435\u043b\u044c", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b\u0435\u0435", None))
    # retranslateUi

