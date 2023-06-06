# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1300, 916)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setStyleSheet(u"/* Frame 1 */\n"
"\n"
"position: relative;\n"
"width: 1314px;\n"
"height: 916px;\n"
"\n"
"background: #000000;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(341, 97, 631, 68))
        self.label.setStyleSheet(u"/* \u041f\u0440\u043e\u0441\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f */\n"
"\n"
"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"position: absolute;\n"
"width: 631px;\n"
"height: 68px;\n"
"left: 341px;\n"
"top: 97px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 44px;\n"
"line-height: 53px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(82, 185, 1150, 566))
        self.label_2.setStyleSheet(u"/* \u041a\u0430\u043a \u0432 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u043e\u043c \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0438. */\n"
"background-color: rgba(255, 255, 255, 0);\n"
"position: absolute;\n"
"width: 1150px;\n"
"height: 566px;\n"
"left: 82px;\n"
"top: 183px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 29px;\n"
"line-height: 35px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(307, 767, 700, 98))
        self.pushButton.setStyleSheet(u"/* Button */\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: 307px;\n"
"top: 767px;\n"
"\n"
"\n"
"\n"
"/* Rectangle 1 */\n"
"\n"
"position: absolute;\n"
"width: 700px;\n"
"height: 98px;\n"
"left: 307px;\n"
"top: 767px;\n"
"\n"
"background: #009158;\n"
"border-radius: 13px;\n"
"\n"
"\n"
"/* \u041f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u0442\u044c! */\n"
"\n"
"position: absolute;\n"
"width: 353px;\n"
"height: 46px;\n"
"left: 524px;\n"
"top: 791px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 44px;\n"
"line-height: 53px;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 1301, 916))
        self.label_3.setPixmap(QPixmap(u":/fon/resurce/1.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0432 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u043e\u043d\u043d\u043e\u043c \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0438.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u0442\u044c!", None))
        self.label_3.setText("")
    # retranslateUi

