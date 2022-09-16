# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pass.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(553, 389)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Slider = QSlider(self.centralwidget)
        self.Slider.setObjectName(u"Slider")
        self.Slider.setGeometry(QRect(50, 210, 221, 22))
        self.Slider.setMinimum(8)
        self.Slider.setMaximum(24)
        self.Slider.setOrientation(Qt.Horizontal)
        self.Password = QLabel(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(50, 80, 221, 61))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(330, 70, 171, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Lowercase = QCheckBox(self.verticalLayoutWidget)
        self.Lowercase.setObjectName(u"Lowercase")

        self.verticalLayout.addWidget(self.Lowercase)

        self.Uppercase = QCheckBox(self.verticalLayoutWidget)
        self.Uppercase.setObjectName(u"Uppercase")

        self.verticalLayout.addWidget(self.Uppercase)

        self.Numbers = QCheckBox(self.verticalLayoutWidget)
        self.Numbers.setObjectName(u"Numbers")

        self.verticalLayout.addWidget(self.Numbers)

        self.Symbols = QCheckBox(self.verticalLayoutWidget)
        self.Symbols.setObjectName(u"Symbols")

        self.verticalLayout.addWidget(self.Symbols)

        self.Slider_amount = QLabel(self.centralwidget)
        self.Slider_amount.setObjectName(u"Slider_amount")
        self.Slider_amount.setGeometry(QRect(160, 190, 81, 21))
        self.Copy = QPushButton(self.centralwidget)
        self.Copy.setObjectName(u"Copy")
        self.Copy.setGeometry(QRect(380, 300, 75, 23))
        self.Refresh = QPushButton(self.centralwidget)
        self.Refresh.setObjectName(u"Refresh")
        self.Refresh.setGeometry(QRect(120, 300, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 553, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Password.setText(QCoreApplication.translate("MainWindow", u"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", None))
        self.Lowercase.setText(QCoreApplication.translate("MainWindow", u"Lowercase", None))
        self.Uppercase.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.Numbers.setText(QCoreApplication.translate("MainWindow", u"Numbers", None))
        self.Symbols.setText(QCoreApplication.translate("MainWindow", u"Symbols", None))
        self.Slider_amount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Copy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.Refresh.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
    # retranslateUi

