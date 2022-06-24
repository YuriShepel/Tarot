# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WandsaHYJzr.ui'
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
import main_wands_rc

class Ui_WandsWindow(object):
    def setupUi(self, WandsWindow):
        if not WandsWindow.objectName():
            WandsWindow.setObjectName(u"WandsWindow")
        WandsWindow.resize(691, 812)
        icon = QIcon()
        icon.addFile(u":/wands/pic/wands/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        WandsWindow.setWindowIcon(icon)
        WandsWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(WandsWindow)
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
        self.button_nine_wands = QToolButton(self.centralwidget)
        self.button_nine_wands.setObjectName(u"button_nine_wands")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.button_nine_wands.setFont(font1)
        self.button_nine_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_nine_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_nine_wands.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/wands/pic/wands/devyatka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_nine_wands.setIcon(icon1)
        self.button_nine_wands.setIconSize(QSize(117, 200))
        self.button_nine_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_nine_wands, 1, 1, 1, 1)

        self.button_four_wands = QToolButton(self.centralwidget)
        self.button_four_wands.setObjectName(u"button_four_wands")
        self.button_four_wands.setFont(font1)
        self.button_four_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_four_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_four_wands.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/wands/pic/wands/chetverka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_four_wands.setIcon(icon2)
        self.button_four_wands.setIconSize(QSize(117, 200))
        self.button_four_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_four_wands, 2, 1, 1, 1)

        self.button_two_wands = QToolButton(self.centralwidget)
        self.button_two_wands.setObjectName(u"button_two_wands")
        self.button_two_wands.setFont(font1)
        self.button_two_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_two_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_two_wands.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/wands/pic/wands/dvoika-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_two_wands.setIcon(icon3)
        self.button_two_wands.setIconSize(QSize(117, 200))
        self.button_two_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_two_wands, 2, 3, 1, 1)

        self.button_ten_wands = QToolButton(self.centralwidget)
        self.button_ten_wands.setObjectName(u"button_ten_wands")
        self.button_ten_wands.setFont(font1)
        self.button_ten_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ten_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_ten_wands.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/wands/pic/wands/desyatka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ten_wands.setIcon(icon4)
        self.button_ten_wands.setIconSize(QSize(117, 200))
        self.button_ten_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_ten_wands, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_king_wands = QToolButton(self.centralwidget)
        self.button_king_wands.setObjectName(u"button_king_wands")
        self.button_king_wands.setFont(font1)
        self.button_king_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_king_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_king_wands.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/wands/pic/wands/korol-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_king_wands.setIcon(icon5)
        self.button_king_wands.setIconSize(QSize(117, 200))
        self.button_king_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_king_wands, 0, 1, 1, 1)

        self.button_knight_wands = QToolButton(self.centralwidget)
        self.button_knight_wands.setObjectName(u"button_knight_wands")
        self.button_knight_wands.setFont(font1)
        self.button_knight_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_knight_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_knight_wands.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/wands/pic/wands/rycar-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_knight_wands.setIcon(icon6)
        self.button_knight_wands.setIconSize(QSize(117, 200))
        self.button_knight_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_knight_wands, 0, 3, 1, 1)

        self.button_ace_wands = QToolButton(self.centralwidget)
        self.button_ace_wands.setObjectName(u"button_ace_wands")
        self.button_ace_wands.setFont(font1)
        self.button_ace_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ace_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_ace_wands.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/wands/pic/wands/tuz-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ace_wands.setIcon(icon7)
        self.button_ace_wands.setIconSize(QSize(117, 200))
        self.button_ace_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_ace_wands, 0, 0, 1, 1)

        self.button_page_wands = QToolButton(self.centralwidget)
        self.button_page_wands.setObjectName(u"button_page_wands")
        self.button_page_wands.setFont(font1)
        self.button_page_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_page_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_page_wands.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/wands/pic/wands/pazh-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_wands.setIcon(icon8)
        self.button_page_wands.setIconSize(QSize(117, 200))
        self.button_page_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_page_wands, 0, 4, 1, 1)

        self.button_queen_wands = QToolButton(self.centralwidget)
        self.button_queen_wands.setObjectName(u"button_queen_wands")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(10)
        self.button_queen_wands.setFont(font2)
        self.button_queen_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_queen_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_queen_wands.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/wands/pic/wands/koroleva-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_queen_wands.setIcon(icon9)
        self.button_queen_wands.setIconSize(QSize(117, 200))
        self.button_queen_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_queen_wands, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 5)

        self.button_three_wands = QToolButton(self.centralwidget)
        self.button_three_wands.setObjectName(u"button_three_wands")
        self.button_three_wands.setFont(font1)
        self.button_three_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_three_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_three_wands.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/wands/pic/wands/troika-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_three_wands.setIcon(icon10)
        self.button_three_wands.setIconSize(QSize(117, 200))
        self.button_three_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_three_wands, 2, 2, 1, 1, Qt.AlignHCenter)

        self.button_seven_wands = QToolButton(self.centralwidget)
        self.button_seven_wands.setObjectName(u"button_seven_wands")
        self.button_seven_wands.setFont(font1)
        self.button_seven_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_seven_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_seven_wands.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/wands/pic/wands/semerka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_seven_wands.setIcon(icon11)
        self.button_seven_wands.setIconSize(QSize(117, 200))
        self.button_seven_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_seven_wands, 1, 3, 1, 1)

        self.button_six_wands = QToolButton(self.centralwidget)
        self.button_six_wands.setObjectName(u"button_six_wands")
        self.button_six_wands.setFont(font1)
        self.button_six_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_six_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_six_wands.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/wands/pic/wands/shesterka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_six_wands.setIcon(icon12)
        self.button_six_wands.setIconSize(QSize(117, 200))
        self.button_six_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_six_wands, 1, 4, 1, 1)

        self.button_eight_wands = QToolButton(self.centralwidget)
        self.button_eight_wands.setObjectName(u"button_eight_wands")
        self.button_eight_wands.setFont(font1)
        self.button_eight_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_eight_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_eight_wands.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/wands/pic/wands/vosmerka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_eight_wands.setIcon(icon13)
        self.button_eight_wands.setIconSize(QSize(117, 200))
        self.button_eight_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_eight_wands, 1, 2, 1, 1)

        self.button_five_wands = QToolButton(self.centralwidget)
        self.button_five_wands.setObjectName(u"button_five_wands")
        self.button_five_wands.setFont(font1)
        self.button_five_wands.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_five_wands.setLayoutDirection(Qt.RightToLeft)
        self.button_five_wands.setAutoFillBackground(False)
        icon14 = QIcon()
        icon14.addFile(u":/wands/pic/wands/pyaterka-zhezlov.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_five_wands.setIcon(icon14)
        self.button_five_wands.setIconSize(QSize(117, 200))
        self.button_five_wands.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_five_wands, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        WandsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WandsWindow)

        QMetaObject.connectSlotsByName(WandsWindow)
    # setupUi

    def retranslateUi(self, WandsWindow):
        WandsWindow.setWindowTitle(QCoreApplication.translate("WandsWindow", u"\u0416\u0435\u0437\u043b\u044b \u0422\u0430\u0440\u043e", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("WandsWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_nine_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0414\u0435\u0432\u044f\u0442\u043a\u0430", None))
        self.button_four_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0427\u0435\u0442\u0432\u0451\u0440\u043a\u0430", None))
        self.button_two_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0414\u0432\u043e\u0439\u043a\u0430", None))
        self.button_ten_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0414\u0435\u0441\u044f\u0442\u043a\u0430", None))
        self.button_king_wands.setText(QCoreApplication.translate("WandsWindow", u"\u041a\u043e\u0440\u043e\u043b\u044c", None))
        self.button_knight_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0420\u044b\u0446\u0430\u0440\u044c", None))
        self.button_ace_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0422\u0443\u0437", None))
        self.button_page_wands.setText(QCoreApplication.translate("WandsWindow", u"\u041f\u0430\u0436", None))
        self.button_queen_wands.setText(QCoreApplication.translate("WandsWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0430", None))
        self.button_three_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0422\u0440\u043e\u0439\u043a\u0430", None))
        self.button_seven_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430", None))
        self.button_six_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0428\u0435\u0441\u0442\u0451\u0440\u043a\u0430", None))
        self.button_eight_wands.setText(QCoreApplication.translate("WandsWindow", u"\u0412\u043e\u0441\u044c\u043c\u0451\u0440\u043a\u0430", None))
        self.button_five_wands.setText(QCoreApplication.translate("WandsWindow", u"\u041f\u044f\u0442\u0451\u0440\u043a\u0430", None))
    # retranslateUi

