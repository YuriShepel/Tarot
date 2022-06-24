# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SwordsixFOCu.ui'
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
import main_swords_rc

class Ui_SwordsWindow(object):
    def setupUi(self, SwordsWindow):
        if not SwordsWindow.objectName():
            SwordsWindow.setObjectName(u"SwordsWindow")
        SwordsWindow.resize(694, 812)
        icon = QIcon()
        icon.addFile(u":/swords/pic/swords/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        SwordsWindow.setWindowIcon(icon)
        SwordsWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(SwordsWindow)
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
        self.button_nine_sw = QToolButton(self.centralwidget)
        self.button_nine_sw.setObjectName(u"button_nine_sw")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.button_nine_sw.setFont(font1)
        self.button_nine_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_nine_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_nine_sw.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/swords/pic/swords/devyatka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_nine_sw.setIcon(icon1)
        self.button_nine_sw.setIconSize(QSize(117, 200))
        self.button_nine_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_nine_sw, 1, 1, 1, 1)

        self.button_four_sw = QToolButton(self.centralwidget)
        self.button_four_sw.setObjectName(u"button_four_sw")
        self.button_four_sw.setFont(font1)
        self.button_four_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_four_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_four_sw.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/swords/pic/swords/chetverka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_four_sw.setIcon(icon2)
        self.button_four_sw.setIconSize(QSize(117, 200))
        self.button_four_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_four_sw, 2, 1, 1, 1)

        self.button_two_sw = QToolButton(self.centralwidget)
        self.button_two_sw.setObjectName(u"button_two_sw")
        self.button_two_sw.setFont(font1)
        self.button_two_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_two_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_two_sw.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/swords/pic/swords/dvoika-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_two_sw.setIcon(icon3)
        self.button_two_sw.setIconSize(QSize(117, 200))
        self.button_two_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_two_sw, 2, 3, 1, 1)

        self.button_ten_sw = QToolButton(self.centralwidget)
        self.button_ten_sw.setObjectName(u"button_ten_sw")
        self.button_ten_sw.setFont(font1)
        self.button_ten_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ten_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_ten_sw.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/swords/pic/swords/desyatka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ten_sw.setIcon(icon4)
        self.button_ten_sw.setIconSize(QSize(117, 200))
        self.button_ten_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_ten_sw, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_queen = QToolButton(self.centralwidget)
        self.button_queen.setObjectName(u"button_queen")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(10)
        self.button_queen.setFont(font2)
        self.button_queen.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_queen.setLayoutDirection(Qt.RightToLeft)
        self.button_queen.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/swords/pic/swords/koroleva-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_queen.setIcon(icon5)
        self.button_queen.setIconSize(QSize(117, 200))
        self.button_queen.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_queen, 1, 2, 1, 1)

        self.button_king = QToolButton(self.centralwidget)
        self.button_king.setObjectName(u"button_king")
        self.button_king.setFont(font1)
        self.button_king.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_king.setLayoutDirection(Qt.RightToLeft)
        self.button_king.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/swords/pic/swords/korol-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_king.setIcon(icon6)
        self.button_king.setIconSize(QSize(117, 200))
        self.button_king.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_king, 1, 1, 1, 1)

        self.button_knight = QToolButton(self.centralwidget)
        self.button_knight.setObjectName(u"button_knight")
        self.button_knight.setFont(font1)
        self.button_knight.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_knight.setLayoutDirection(Qt.RightToLeft)
        self.button_knight.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/swords/pic/swords/rycar-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_knight.setIcon(icon7)
        self.button_knight.setIconSize(QSize(117, 200))
        self.button_knight.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_knight, 1, 3, 1, 1)

        self.button_ace = QToolButton(self.centralwidget)
        self.button_ace.setObjectName(u"button_ace")
        self.button_ace.setFont(font1)
        self.button_ace.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_ace.setLayoutDirection(Qt.RightToLeft)
        self.button_ace.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/swords/pic/swords/tuz-mechei1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_ace.setIcon(icon8)
        self.button_ace.setIconSize(QSize(117, 200))
        self.button_ace.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_ace, 1, 0, 1, 1)

        self.button_page = QToolButton(self.centralwidget)
        self.button_page.setObjectName(u"button_page")
        self.button_page.setFont(font1)
        self.button_page.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_page.setLayoutDirection(Qt.RightToLeft)
        self.button_page.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/swords/pic/swords/pazh-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_page.setIcon(icon9)
        self.button_page.setIconSize(QSize(117, 200))
        self.button_page.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.button_page, 1, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 5)

        self.button_three_sw = QToolButton(self.centralwidget)
        self.button_three_sw.setObjectName(u"button_three_sw")
        self.button_three_sw.setFont(font1)
        self.button_three_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_three_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_three_sw.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/swords/pic/swords/troika-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_three_sw.setIcon(icon10)
        self.button_three_sw.setIconSize(QSize(117, 200))
        self.button_three_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_three_sw, 2, 2, 1, 1, Qt.AlignHCenter)

        self.button_seven_sw = QToolButton(self.centralwidget)
        self.button_seven_sw.setObjectName(u"button_seven_sw")
        self.button_seven_sw.setFont(font1)
        self.button_seven_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_seven_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_seven_sw.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/swords/pic/swords/semerka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_seven_sw.setIcon(icon11)
        self.button_seven_sw.setIconSize(QSize(117, 200))
        self.button_seven_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_seven_sw, 1, 3, 1, 1)

        self.button_six_sw = QToolButton(self.centralwidget)
        self.button_six_sw.setObjectName(u"button_six_sw")
        self.button_six_sw.setFont(font1)
        self.button_six_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_six_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_six_sw.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/swords/pic/swords/shesterka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_six_sw.setIcon(icon12)
        self.button_six_sw.setIconSize(QSize(117, 200))
        self.button_six_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_six_sw, 1, 4, 1, 1)

        self.button_eight_sw = QToolButton(self.centralwidget)
        self.button_eight_sw.setObjectName(u"button_eight_sw")
        self.button_eight_sw.setFont(font1)
        self.button_eight_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_eight_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_eight_sw.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/swords/pic/swords/vosmerka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_eight_sw.setIcon(icon13)
        self.button_eight_sw.setIconSize(QSize(117, 200))
        self.button_eight_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_eight_sw, 1, 2, 1, 1)

        self.button_five_sw = QToolButton(self.centralwidget)
        self.button_five_sw.setObjectName(u"button_five_sw")
        self.button_five_sw.setFont(font1)
        self.button_five_sw.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_five_sw.setLayoutDirection(Qt.RightToLeft)
        self.button_five_sw.setAutoFillBackground(False)
        icon14 = QIcon()
        icon14.addFile(u":/swords/pic/swords/pyaterka-mechei.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_five_sw.setIcon(icon14)
        self.button_five_sw.setIconSize(QSize(117, 200))
        self.button_five_sw.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_2.addWidget(self.button_five_sw, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        SwordsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SwordsWindow)

        QMetaObject.connectSlotsByName(SwordsWindow)
    # setupUi

    def retranslateUi(self, SwordsWindow):
        SwordsWindow.setWindowTitle(QCoreApplication.translate("SwordsWindow", u"\u041c\u0435\u0447\u0438 \u0422\u0430\u0440\u043e", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("SwordsWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_nine_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0414\u0435\u0432\u044f\u0442\u043a\u0430", None))
        self.button_four_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0427\u0435\u0442\u0432\u0451\u0440\u043a\u0430", None))
        self.button_two_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0414\u0432\u043e\u0439\u043a\u0430", None))
        self.button_ten_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0414\u0435\u0441\u044f\u0442\u043a\u0430", None))
        self.button_queen.setText(QCoreApplication.translate("SwordsWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432\u0430", None))
        self.button_king.setText(QCoreApplication.translate("SwordsWindow", u"\u041a\u043e\u0440\u043e\u043b\u044c", None))
        self.button_knight.setText(QCoreApplication.translate("SwordsWindow", u"\u0420\u044b\u0446\u0430\u0440\u044c", None))
        self.button_ace.setText(QCoreApplication.translate("SwordsWindow", u"\u0422\u0443\u0437", None))
        self.button_page.setText(QCoreApplication.translate("SwordsWindow", u"\u041f\u0430\u0436", None))
        self.button_three_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0422\u0440\u043e\u0439\u043a\u0430", None))
        self.button_seven_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430", None))
        self.button_six_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0428\u0435\u0441\u0442\u0451\u0440\u043a\u0430", None))
        self.button_eight_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u0412\u043e\u0441\u044c\u043c\u0451\u0440\u043a\u0430", None))
        self.button_five_sw.setText(QCoreApplication.translate("SwordsWindow", u"\u041f\u044f\u0442\u0451\u0440\u043a\u0430", None))
    # retranslateUi

