# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PentaclesHYbfSj.ui'
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
import main_pentacles_rc

class Ui_PentaclesWindow(object):
    def setupUi(self, PentaclesWindow):
        if not PentaclesWindow.objectName():
            PentaclesWindow.setObjectName(u"PentaclesWindow")
        PentaclesWindow.resize(691, 812)
        icon = QIcon()
        icon.addFile(u":/pentacles/pic/pentacles/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        PentaclesWindow.setWindowIcon(icon)
        PentaclesWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(PentaclesWindow)
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
        self.button_nine_pen = QToolButton(self.centralwidget)
        self.button_nine_pen.setObjectName(u"button_nine_pen")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.button_nine_pen.setFont(font1)
        self.button_nine_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_nine_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_nine_pen.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/pentacles/pic/pentacles/devyatka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_nine_pen.setIcon(icon1)
        self.button_nine_pen.setIconSize(QSize(117, 200))
        self.button_nine_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_nine_pen, 1, 1, 1, 1)

        self.button_four_pen = QToolButton(self.centralwidget)
        self.button_four_pen.setObjectName(u"button_four_pen")
        self.button_four_pen.setFont(font1)
        self.button_four_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_four_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_four_pen.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/pentacles/pic/pentacles/chetverka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_four_pen.setIcon(icon2)
        self.button_four_pen.setIconSize(QSize(117, 200))
        self.button_four_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_four_pen, 2, 1, 1, 1)

        self.button_two_pen = QToolButton(self.centralwidget)
        self.button_two_pen.setObjectName(u"button_two_pen")
        self.button_two_pen.setFont(font1)
        self.button_two_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_two_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_two_pen.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/pentacles/pic/pentacles/dvoika-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_two_pen.setIcon(icon3)
        self.button_two_pen.setIconSize(QSize(117, 200))
        self.button_two_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_two_pen, 2, 3, 1, 1)

        self.button_ten_pen = QToolButton(self.centralwidget)
        self.button_ten_pen.setObjectName(u"button_ten_pen")
        self.button_ten_pen.setFont(font1)
        self.button_ten_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ten_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_ten_pen.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/pentacles/pic/pentacles/desyatka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ten_pen.setIcon(icon4)
        self.button_ten_pen.setIconSize(QSize(117, 200))
        self.button_ten_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_ten_pen, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_king_pen = QToolButton(self.centralwidget)
        self.button_king_pen.setObjectName(u"button_king_pen")
        self.button_king_pen.setFont(font1)
        self.button_king_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_king_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_king_pen.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/pentacles/pic/pentacles/korol-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_king_pen.setIcon(icon5)
        self.button_king_pen.setIconSize(QSize(117, 200))
        self.button_king_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_king_pen, 0, 1, 1, 1)

        self.button_knight_pen = QToolButton(self.centralwidget)
        self.button_knight_pen.setObjectName(u"button_knight_pen")
        self.button_knight_pen.setFont(font1)
        self.button_knight_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_knight_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_knight_pen.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/pentacles/pic/pentacles/rycar-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_knight_pen.setIcon(icon6)
        self.button_knight_pen.setIconSize(QSize(117, 200))
        self.button_knight_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_knight_pen, 0, 3, 1, 1)

        self.button_ace_pen = QToolButton(self.centralwidget)
        self.button_ace_pen.setObjectName(u"button_ace_pen")
        self.button_ace_pen.setFont(font1)
        self.button_ace_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ace_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_ace_pen.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/pentacles/pic/pentacles/tuz_pentakley.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ace_pen.setIcon(icon7)
        self.button_ace_pen.setIconSize(QSize(117, 200))
        self.button_ace_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_ace_pen, 0, 0, 1, 1)

        self.button_page_pen = QToolButton(self.centralwidget)
        self.button_page_pen.setObjectName(u"button_page_pen")
        self.button_page_pen.setFont(font1)
        self.button_page_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_page_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_page_pen.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/pentacles/pic/pentacles/pazh-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page_pen.setIcon(icon8)
        self.button_page_pen.setIconSize(QSize(117, 200))
        self.button_page_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_page_pen, 0, 4, 1, 1)

        self.button_queen_pen = QToolButton(self.centralwidget)
        self.button_queen_pen.setObjectName(u"button_queen_pen")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(10)
        self.button_queen_pen.setFont(font2)
        self.button_queen_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_queen_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_queen_pen.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/pentacles/pic/pentacles/koroleva-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_queen_pen.setIcon(icon9)
        self.button_queen_pen.setIconSize(QSize(117, 200))
        self.button_queen_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_queen_pen, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 5)

        self.button_three_pen = QToolButton(self.centralwidget)
        self.button_three_pen.setObjectName(u"button_three_pen")
        self.button_three_pen.setFont(font1)
        self.button_three_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_three_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_three_pen.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/pentacles/pic/pentacles/troika-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_three_pen.setIcon(icon10)
        self.button_three_pen.setIconSize(QSize(117, 200))
        self.button_three_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_three_pen, 2, 2, 1, 1, Qt.AlignHCenter)

        self.button_seven_pen = QToolButton(self.centralwidget)
        self.button_seven_pen.setObjectName(u"button_seven_pen")
        self.button_seven_pen.setFont(font1)
        self.button_seven_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_seven_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_seven_pen.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/pentacles/pic/pentacles/semerka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_seven_pen.setIcon(icon11)
        self.button_seven_pen.setIconSize(QSize(117, 200))
        self.button_seven_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_seven_pen, 1, 3, 1, 1)

        self.button_six_pen = QToolButton(self.centralwidget)
        self.button_six_pen.setObjectName(u"button_six_pen")
        self.button_six_pen.setFont(font1)
        self.button_six_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_six_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_six_pen.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/pentacles/pic/pentacles/shesterka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_six_pen.setIcon(icon12)
        self.button_six_pen.setIconSize(QSize(117, 200))
        self.button_six_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_six_pen, 1, 4, 1, 1)

        self.button_eight_pen = QToolButton(self.centralwidget)
        self.button_eight_pen.setObjectName(u"button_eight_pen")
        self.button_eight_pen.setFont(font1)
        self.button_eight_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_eight_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_eight_pen.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/pentacles/pic/pentacles/vosmerka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_eight_pen.setIcon(icon13)
        self.button_eight_pen.setIconSize(QSize(117, 200))
        self.button_eight_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_eight_pen, 1, 2, 1, 1)

        self.button_five_pen = QToolButton(self.centralwidget)
        self.button_five_pen.setObjectName(u"button_five_pen")
        self.button_five_pen.setFont(font1)
        self.button_five_pen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_five_pen.setLayoutDirection(Qt.RightToLeft)
        self.button_five_pen.setAutoFillBackground(False)
        icon14 = QIcon()
        icon14.addFile(u":/pentacles/pic/pentacles/pyaterka-pentaklei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_five_pen.setIcon(icon14)
        self.button_five_pen.setIconSize(QSize(117, 200))
        self.button_five_pen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_five_pen, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        PentaclesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(PentaclesWindow)

        QMetaObject.connectSlotsByName(PentaclesWindow)
    # setupUi

    def retranslateUi(self, PentaclesWindow):
        PentaclesWindow.setWindowTitle(QCoreApplication.translate("PentaclesWindow", u"\u041f\u0435\u043d\u0442\u0430\u043a\u043b\u0438 \u0422\u0430\u0440\u043e", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("PentaclesWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_nine_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0414\u0435\u0432\u044f\u0442\u043a\u0430", None))
        self.button_four_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0427\u0435\u0442\u0432\u0451\u0440\u043a\u0430", None))
        self.button_two_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0414\u0432\u043e\u0439\u043a\u0430", None))
        self.button_ten_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0414\u0435\u0441\u044f\u0442\u043a\u0430", None))
        self.button_king_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u041a\u043e\u0440\u043e\u043b\u044c", None))
        self.button_knight_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0420\u044b\u0446\u0430\u0440\u044c", None))
        self.button_ace_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0422\u0443\u0437", None))
        self.button_page_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u041f\u0430\u0436", None))
        self.button_queen_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0430", None))
        self.button_three_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0422\u0440\u043e\u0439\u043a\u0430", None))
        self.button_seven_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430", None))
        self.button_six_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0428\u0435\u0441\u0442\u0451\u0440\u043a\u0430", None))
        self.button_eight_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u0412\u043e\u0441\u044c\u043c\u0451\u0440\u043a\u0430", None))
        self.button_five_pen.setText(QCoreApplication.translate("PentaclesWindow", u"\u041f\u044f\u0442\u0451\u0440\u043a\u0430", None))
    # retranslateUi

