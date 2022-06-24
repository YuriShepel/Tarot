# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_tarotlIYVPs.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
import main_win_taro_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(570, 548)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(508, 412))
        icon = QIcon()
        icon.addFile(u":/mainTaroWin/pic/main_taro_pic/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_main_arcans = QPushButton(self.centralwidget)
        self.button_main_arcans.setObjectName(u"button_main_arcans")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_main_arcans.sizePolicy().hasHeightForWidth())
        self.button_main_arcans.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        font.setBold(True)
        self.button_main_arcans.setFont(font)
        self.button_main_arcans.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_main_arcans.setLayoutDirection(Qt.LeftToRight)
        self.button_main_arcans.setAutoFillBackground(False)
        self.button_main_arcans.setStyleSheet(u"QPushButton{\n"
"padding-right: 20px;\n"
"padding-left: 20px;\n"
"background-color: #00a8ff;\n"
"border-radius: 30px;\n"
"border: 1px solid rgba(105, 118, 132, 255)\n"
"}\n"
" QPushButton:pressed {\n"
"     background-color: #3742fa;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/res.qrc", QSize(), QIcon.Normal, QIcon.Off)
        self.button_main_arcans.setIcon(icon1)

        self.verticalLayout.addWidget(self.button_main_arcans)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(27)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 40, 6, -1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setLocale(QLocale(QLocale.Russian, QLocale.Ukraine))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 23)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignBottom)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(37)
        self.gridLayout.setContentsMargins(-1, -1, -1, 17)
        self.button_swords = QToolButton(self.centralwidget)
        self.button_swords.setObjectName(u"button_swords")
        self.button_swords.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_swords.setStyleSheet(u"QToolButton {\n"
"  border: medium none;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/mainTaroWin/pic/main_taro_pic/swords.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_swords.setIcon(icon2)
        self.button_swords.setIconSize(QSize(145, 57))
        self.button_swords.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.button_swords, 0, 0, 1, 1)

        self.button_cups = QToolButton(self.centralwidget)
        self.button_cups.setObjectName(u"button_cups")
        self.button_cups.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_cups.setStyleSheet(u"QToolButton {\n"
"  border: none;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/mainTaroWin/pic/main_taro_pic/cups.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_cups.setIcon(icon3)
        self.button_cups.setIconSize(QSize(145, 57))

        self.gridLayout.addWidget(self.button_cups, 0, 1, 1, 1)

        self.button_pentacles = QToolButton(self.centralwidget)
        self.button_pentacles.setObjectName(u"button_pentacles")
        self.button_pentacles.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_pentacles.setStyleSheet(u"QToolButton {\n"
"  border: medium none;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/mainTaroWin/pic/main_taro_pic/pentacles.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pentacles.setIcon(icon4)
        self.button_pentacles.setIconSize(QSize(145, 57))

        self.gridLayout.addWidget(self.button_pentacles, 1, 0, 1, 1)

        self.button_wands_2 = QToolButton(self.centralwidget)
        self.button_wands_2.setObjectName(u"button_wands_2")
        self.button_wands_2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_wands_2.sizePolicy().hasHeightForWidth())
        self.button_wands_2.setSizePolicy(sizePolicy2)
        self.button_wands_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_wands_2.setStyleSheet(u"QToolButton {\n"
"  border: medium none;\n"
"}\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/mainTaroWin/pic/main_taro_pic/wands.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_wands_2.setIcon(icon5)
        self.button_wands_2.setIconSize(QSize(145, 57))

        self.gridLayout.addWidget(self.button_wands_2, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(27)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 12, 6, -1)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLocale(QLocale(QLocale.Russian, QLocale.Ukraine))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.Day_card = QPushButton(self.centralwidget)
        self.Day_card.setObjectName(u"Day_card")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.Day_card.setFont(font2)
        self.Day_card.setStyleSheet(u"QPushButton{\n"
"padding-right: 20px;\n"
"padding-left: 20px;\n"
"padding-top: 20px;\n"
"padding-bottom: 20px;\n"
"background-color: #00a8ff;\n"
"border-radius: 30px;\n"
"border: 1px solid rgba(105, 118, 132, 255)\n"
"}\n"
" QPushButton:pressed {\n"
"     background-color: #3742fa;\n"
"}")

        self.verticalLayout.addWidget(self.Day_card)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u043a\u0430\u043d\u044b \u0442\u0430\u0440\u043e", None))
        self.button_main_arcans.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0422\u0410\u0420\u0428\u0418\u0415 \u0410\u0420\u041a\u0410\u041d\u042b \u0422\u0410\u0420\u041e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u041c\u041b\u0410\u0414\u0428\u0418\u0415 \u0410\u0420\u041a\u0410\u041d\u042b</p></body></html>", None))
        self.button_swords.setText("")
#if QT_CONFIG(shortcut)
        self.button_swords.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.button_cups.setText("")
        self.button_pentacles.setText("")
        self.button_wands_2.setText("")
        self.Day_card.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u0442\u0430 \u0434\u043d\u044f", None))
    # retranslateUi

