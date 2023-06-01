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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(737, 509)
        MainWindow.setStyleSheet(u"\n"
"position: relative;\n"
"width: 737px;\n"
"height: 484px;\n"
"\n"
"background: #000000;\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(171, 431, 395, 54))
        self.pushButton.setStyleSheet(u"/* button */\n"
"\n"
"position: absolute;\n"
"width: 395px;\n"
"height: 54px;\n"
"left: 171px;\n"
"top: 431px;\n"
"\n"
"\n"
"\n"
"/* Rectangle 3 */\n"
"\n"
"position: absolute;\n"
"width: 395px;\n"
"height: 52px;\n"
"left: 171px;\n"
"top: 433px;\n"
"\n"
"background: #24BAFF;\n"
"border-radius: 8px;\n"
"\n"
"\n"
"/* \u041f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u0442\u044c! */\n"
"\n"
"position: absolute;\n"
"width: 392px;\n"
"height: 53px;\n"
"left: 174px;\n"
"top: 431px;\n"
"\n"
"font-family: 'Inder';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 51px;\n"
"/* or 212% */\n"
"text-align: center;\n"
"letter-spacing: 0.02em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(195, 56, 348, 28))
        self.label.setStyleSheet(u"/* \u041f\u0440\u043e\u0441\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f */\n"
"\n"
"position: absolute;\n"
"width: 348px;\n"
"height: 62px;\n"
"left: 195px;\n"
"top: 56px;\n"
"\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 24px;\n"
"line-height: 29px;\n"
"/* or 121% */\n"
"text-align: center;\n"
"letter-spacing: 0.01em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"")
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(76, 114, 622, 305))
        self.label_2.setStyleSheet(u"/* \u041a\u0430\u043a \u0432 \u043b\u0438\u0446\u0438\u043d\u0437\u0438\u043e\u043d\u043d\u043e\u043c \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0438\u0438 */\n"
"\n"
"position: absolute;\n"
"width: 622px;\n"
"height: 305px;\n"
"left: 76px;\n"
"top: 114px;\n"
"\n"
"font-family: 'Italianno';\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"font-size: 17px;\n"
"line-height: 4px;\n"
"/* or 24% */\n"
"letter-spacing: 0.01em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"opacity: 0.76;\n"
"")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0441\u0442\u0443\u043f\u0438\u0442\u044c!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u043e \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u0430\u044f \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u044f\n"
"", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043a \u0432 \u043b\u0438\u0446\u0438\u043d\u0437\u0438\u043e\u043d\u043d\u043e\u043c \u0441\u043e\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0438\u0438", None))
    # retranslateUi

