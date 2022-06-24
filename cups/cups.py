# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CupsqNLQza.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)
import main_cups_rc

class Ui_CupsWindow(object):
    def setupUi(self, CupsWindow):
        if not CupsWindow.objectName():
            CupsWindow.setObjectName(u"CupsWindow")
        CupsWindow.resize(691, 812)
        icon = QIcon()
        icon.addFile(u":/cups/pic/cups/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        CupsWindow.setWindowIcon(icon)
        CupsWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(CupsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_back_to_menu = QPushButton(self.centralwidget)
        self.button_back_to_menu.setObjectName(u"button_back_to_menu")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.button_back_to_menu.setFont(font)
        self.button_back_to_menu.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_back_to_menu.setToolTipDuration(0)
        self.button_back_to_menu.setLayoutDirection(Qt.LeftToRight)
        self.button_back_to_menu.setStyleSheet(u"QPushButton{\n"
"	padding-top: 20px;\n"
"	padding-bottom: 20px;\n"
"	padding-right: 20px;\n"
"	padding-left: 20px;\n"
"	background-color:  #00a8ff;\n"
"	border-radius: 30px;\n"
"	border: 1px solid rgba(105, 118, 132, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"     background-color: #3742fa;\n"
"}\n"
"\n"
"")
        self.button_back_to_menu.setIconSize(QSize(20, 21))
        self.button_back_to_menu.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.button_back_to_menu)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_nine_cup = QToolButton(self.centralwidget)
        self.button_nine_cup.setObjectName(u"button_nine_cup")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.button_nine_cup.setFont(font1)
        self.button_nine_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_nine_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_nine_cup.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/cups/pic/cups/devyatka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_nine_cup.setIcon(icon1)
        self.button_nine_cup.setIconSize(QSize(117, 200))
        self.button_nine_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_nine_cup, 1, 1, 1, 1)

        self.button_four_cup = QToolButton(self.centralwidget)
        self.button_four_cup.setObjectName(u"button_four_cup")
        self.button_four_cup.setFont(font1)
        self.button_four_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_four_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_four_cup.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/cups/pic/cups/chetverka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_four_cup.setIcon(icon2)
        self.button_four_cup.setIconSize(QSize(117, 200))
        self.button_four_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_four_cup, 2, 1, 1, 1)

        self.button_two_cup = QToolButton(self.centralwidget)
        self.button_two_cup.setObjectName(u"button_two_cup")
        self.button_two_cup.setFont(font1)
        self.button_two_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_two_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_two_cup.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/cups/pic/cups/dvoika-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_two_cup.setIcon(icon3)
        self.button_two_cup.setIconSize(QSize(117, 200))
        self.button_two_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_two_cup, 2, 3, 1, 1)

        self.button_ten_cup = QToolButton(self.centralwidget)
        self.button_ten_cup.setObjectName(u"button_ten_cup")
        self.button_ten_cup.setFont(font1)
        self.button_ten_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ten_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_ten_cup.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/cups/pic/cups/desyatka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ten_cup.setIcon(icon4)
        self.button_ten_cup.setIconSize(QSize(117, 200))
        self.button_ten_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_ten_cup, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_queen_cup = QToolButton(self.centralwidget)
        self.button_queen_cup.setObjectName(u"button_queen_cup")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(10)
        self.button_queen_cup.setFont(font2)
        self.button_queen_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_queen_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_queen_cup.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/cups/pic/cups/koroleva-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_queen_cup.setIcon(icon5)
        self.button_queen_cup.setIconSize(QSize(117, 200))
        self.button_queen_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_queen_cup, 1, 2, 1, 1)

        self.button_king_cup = QToolButton(self.centralwidget)
        self.button_king_cup.setObjectName(u"button_king_cup")
        self.button_king_cup.setFont(font1)
        self.button_king_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_king_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_king_cup.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/cups/pic/cups/korol-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_king_cup.setIcon(icon6)
        self.button_king_cup.setIconSize(QSize(117, 200))
        self.button_king_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_king_cup, 1, 1, 1, 1)

        self.button_knight_cup = QToolButton(self.centralwidget)
        self.button_knight_cup.setObjectName(u"button_knight_cup")
        self.button_knight_cup.setFont(font1)
        self.button_knight_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_knight_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_knight_cup.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/cups/pic/cups/rycar-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_knight_cup.setIcon(icon7)
        self.button_knight_cup.setIconSize(QSize(117, 200))
        self.button_knight_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_knight_cup, 1, 3, 1, 1)

        self.button_ace_cup = QToolButton(self.centralwidget)
        self.button_ace_cup.setObjectName(u"button_ace_cup")
        self.button_ace_cup.setFont(font1)
        self.button_ace_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ace_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_ace_cup.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/cups/pic/cups/tuz-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ace_cup.setIcon(icon8)
        self.button_ace_cup.setIconSize(QSize(117, 200))
        self.button_ace_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_ace_cup, 1, 0, 1, 1)

        self.button_page_cup = QToolButton(self.centralwidget)
        self.button_page_cup.setObjectName(u"button_page_cup")
        self.button_page_cup.setFont(font1)
        self.button_page_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_page_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_page_cup.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/cups/pic/cups/pazh-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_cup.setIcon(icon9)
        self.button_page_cup.setIconSize(QSize(117, 200))
        self.button_page_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_page_cup, 1, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 5)

        self.button_three_cup = QToolButton(self.centralwidget)
        self.button_three_cup.setObjectName(u"button_three_cup")
        self.button_three_cup.setFont(font1)
        self.button_three_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_three_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_three_cup.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/cups/pic/cups/troika-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_three_cup.setIcon(icon10)
        self.button_three_cup.setIconSize(QSize(117, 200))
        self.button_three_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_three_cup, 2, 2, 1, 1, Qt.AlignHCenter)

        self.button_seven_cup = QToolButton(self.centralwidget)
        self.button_seven_cup.setObjectName(u"button_seven_cup")
        self.button_seven_cup.setFont(font1)
        self.button_seven_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_seven_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_seven_cup.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/cups/pic/cups/semerka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_seven_cup.setIcon(icon11)
        self.button_seven_cup.setIconSize(QSize(117, 200))
        self.button_seven_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_seven_cup, 1, 3, 1, 1)

        self.button_six_cup = QToolButton(self.centralwidget)
        self.button_six_cup.setObjectName(u"button_six_cup")
        self.button_six_cup.setFont(font1)
        self.button_six_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_six_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_six_cup.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/cups/pic/cups/shesterka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_six_cup.setIcon(icon12)
        self.button_six_cup.setIconSize(QSize(117, 200))
        self.button_six_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_six_cup, 1, 4, 1, 1)

        self.button_eight_cup = QToolButton(self.centralwidget)
        self.button_eight_cup.setObjectName(u"button_eight_cup")
        self.button_eight_cup.setFont(font1)
        self.button_eight_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_eight_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_eight_cup.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/cups/pic/cups/vosmerka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_eight_cup.setIcon(icon13)
        self.button_eight_cup.setIconSize(QSize(117, 200))
        self.button_eight_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_eight_cup, 1, 2, 1, 1)

        self.button_five_cup = QToolButton(self.centralwidget)
        self.button_five_cup.setObjectName(u"button_five_cup")
        self.button_five_cup.setFont(font1)
        self.button_five_cup.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_five_cup.setLayoutDirection(Qt.RightToLeft)
        self.button_five_cup.setAutoFillBackground(False)
        icon14 = QIcon()
        icon14.addFile(u":/cups/pic/cups/pyaterka-kubkov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_five_cup.setIcon(icon14)
        self.button_five_cup.setIconSize(QSize(117, 200))
        self.button_five_cup.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_five_cup, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        CupsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CupsWindow)

        QMetaObject.connectSlotsByName(CupsWindow)
    # setupUi

    def retranslateUi(self, CupsWindow):
        CupsWindow.setWindowTitle(QCoreApplication.translate("CupsWindow", u"\u041a\u0443\u0431\u043a\u0438 \u0422\u0430\u0440\u043e", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("CupsWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_nine_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0414\u0435\u0432\u044f\u0442\u043a\u0430", None))
        self.button_four_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0427\u0435\u0442\u0432\u0451\u0440\u043a\u0430", None))
        self.button_two_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0414\u0432\u043e\u0439\u043a\u0430", None))
        self.button_ten_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0414\u0435\u0441\u044f\u0442\u043a\u0430", None))
        self.button_queen_cup.setText(QCoreApplication.translate("CupsWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0430", None))
        self.button_king_cup.setText(QCoreApplication.translate("CupsWindow", u"\u041a\u043e\u0440\u043e\u043b\u044c", None))
        self.button_knight_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0420\u044b\u0446\u0430\u0440\u044c", None))
        self.button_ace_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0422\u0443\u0437", None))
        self.button_page_cup.setText(QCoreApplication.translate("CupsWindow", u"\u041f\u0430\u0436", None))
        self.button_three_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0422\u0440\u043e\u0439\u043a\u0430", None))
        self.button_seven_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430", None))
        self.button_six_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0428\u0435\u0441\u0442\u0451\u0440\u043a\u0430", None))
        self.button_eight_cup.setText(QCoreApplication.translate("CupsWindow", u"\u0412\u043e\u0441\u044c\u043c\u0451\u0440\u043a\u0430", None))
        self.button_five_cup.setText(QCoreApplication.translate("CupsWindow", u"\u041f\u044f\u0442\u0451\u0440\u043a\u0430", None))
    # retranslateUi

