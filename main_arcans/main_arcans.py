# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainArcansHEwUYY.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)
import main_arcans_win_rc

class Ui_MainArcansWindow(object):
    def setupUi(self, MainArcansWindow):
        if not MainArcansWindow.objectName():
            MainArcansWindow.setObjectName(u"MainArcansWindow")
        MainArcansWindow.resize(1091, 812)
        icon = QIcon()
        icon.addFile(u":/mainArcans/pic/main_arcans/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainArcansWindow.setWindowIcon(icon)
        MainArcansWindow.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(MainArcansWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
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

        self.verticalLayout.addWidget(self.button_back_to_menu)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_fool = QToolButton(self.centralwidget)
        self.button_fool.setObjectName(u"button_fool")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.button_fool.setFont(font1)
        self.button_fool.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_fool.setLayoutDirection(Qt.RightToLeft)
        self.button_fool.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/mainArcans/pic/main_arcans/shut.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_fool.setIcon(icon1)
        self.button_fool.setIconSize(QSize(117, 200))
        self.button_fool.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_fool)

        self.button_mage = QToolButton(self.centralwidget)
        self.button_mage.setObjectName(u"button_mage")
        self.button_mage.setFont(font1)
        self.button_mage.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_mage.setLayoutDirection(Qt.RightToLeft)
        self.button_mage.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/mainArcans/pic/main_arcans/mag.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_mage.setIcon(icon2)
        self.button_mage.setIconSize(QSize(117, 200))
        self.button_mage.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_mage)

        self.button_pristess = QToolButton(self.centralwidget)
        self.button_pristess.setObjectName(u"button_pristess")
        font2 = QFont()
        font2.setFamilies([u"Arial Black"])
        font2.setPointSize(9)
        self.button_pristess.setFont(font2)
        self.button_pristess.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_pristess.setLayoutDirection(Qt.RightToLeft)
        self.button_pristess.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/mainArcans/pic/main_arcans/verhovaya-zhrica.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_pristess.setIcon(icon3)
        self.button_pristess.setIconSize(QSize(117, 200))
        self.button_pristess.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_pristess)

        self.button_empress = QToolButton(self.centralwidget)
        self.button_empress.setObjectName(u"button_empress")
        self.button_empress.setFont(font1)
        self.button_empress.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_empress.setLayoutDirection(Qt.RightToLeft)
        self.button_empress.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/mainArcans/pic/main_arcans/imperatrica.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_empress.setIcon(icon4)
        self.button_empress.setIconSize(QSize(117, 200))
        self.button_empress.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_empress)

        self.button_emperor = QToolButton(self.centralwidget)
        self.button_emperor.setObjectName(u"button_emperor")
        self.button_emperor.setFont(font1)
        self.button_emperor.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_emperor.setLayoutDirection(Qt.RightToLeft)
        self.button_emperor.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/mainArcans/pic/main_arcans/imperator.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_emperor.setIcon(icon5)
        self.button_emperor.setIconSize(QSize(117, 200))
        self.button_emperor.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_emperor)

        self.button_hierophant = QToolButton(self.centralwidget)
        self.button_hierophant.setObjectName(u"button_hierophant")
        self.button_hierophant.setFont(font1)
        self.button_hierophant.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_hierophant.setLayoutDirection(Qt.RightToLeft)
        self.button_hierophant.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/mainArcans/pic/main_arcans/verhovnyi-zhrec.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_hierophant.setIcon(icon6)
        self.button_hierophant.setIconSize(QSize(117, 200))
        self.button_hierophant.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_hierophant)

        self.button_lovers = QToolButton(self.centralwidget)
        self.button_lovers.setObjectName(u"button_lovers")
        self.button_lovers.setFont(font1)
        self.button_lovers.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_lovers.setLayoutDirection(Qt.RightToLeft)
        self.button_lovers.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u":/mainArcans/pic/main_arcans/vlublennye.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_lovers.setIcon(icon7)
        self.button_lovers.setIconSize(QSize(117, 200))
        self.button_lovers.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_lovers)

        self.button_chariot = QToolButton(self.centralwidget)
        self.button_chariot.setObjectName(u"button_chariot")
        self.button_chariot.setFont(font1)
        self.button_chariot.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_chariot.setLayoutDirection(Qt.RightToLeft)
        self.button_chariot.setAutoFillBackground(False)
        icon8 = QIcon()
        icon8.addFile(u":/mainArcans/pic/main_arcans/kolesnica.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_chariot.setIcon(icon8)
        self.button_chariot.setIconSize(QSize(117, 200))
        self.button_chariot.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout.addWidget(self.button_chariot)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_strenght = QToolButton(self.centralwidget)
        self.button_strenght.setObjectName(u"button_strenght")
        self.button_strenght.setFont(font1)
        self.button_strenght.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_strenght.setLayoutDirection(Qt.RightToLeft)
        self.button_strenght.setAutoFillBackground(False)
        icon9 = QIcon()
        icon9.addFile(u":/mainArcans/pic/main_arcans/sila.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_strenght.setIcon(icon9)
        self.button_strenght.setIconSize(QSize(117, 200))
        self.button_strenght.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_strenght)

        self.button_hermit = QToolButton(self.centralwidget)
        self.button_hermit.setObjectName(u"button_hermit")
        self.button_hermit.setFont(font1)
        self.button_hermit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_hermit.setLayoutDirection(Qt.RightToLeft)
        self.button_hermit.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/mainArcans/pic/main_arcans/otshelnik.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_hermit.setIcon(icon10)
        self.button_hermit.setIconSize(QSize(117, 200))
        self.button_hermit.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_hermit)

        self.button_fortune = QToolButton(self.centralwidget)
        self.button_fortune.setObjectName(u"button_fortune")
        self.button_fortune.setFont(font1)
        self.button_fortune.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_fortune.setLayoutDirection(Qt.RightToLeft)
        self.button_fortune.setAutoFillBackground(False)
        icon11 = QIcon()
        icon11.addFile(u":/mainArcans/pic/main_arcans/koleso-fortuny.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_fortune.setIcon(icon11)
        self.button_fortune.setIconSize(QSize(117, 200))
        self.button_fortune.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_fortune)

        self.button_justice = QToolButton(self.centralwidget)
        self.button_justice.setObjectName(u"button_justice")
        self.button_justice.setFont(font1)
        self.button_justice.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_justice.setLayoutDirection(Qt.RightToLeft)
        self.button_justice.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/mainArcans/pic/main_arcans/spravedlivost.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_justice.setIcon(icon12)
        self.button_justice.setIconSize(QSize(117, 200))
        self.button_justice.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_justice)

        self.button_henged = QToolButton(self.centralwidget)
        self.button_henged.setObjectName(u"button_henged")
        self.button_henged.setFont(font1)
        self.button_henged.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_henged.setLayoutDirection(Qt.RightToLeft)
        self.button_henged.setAutoFillBackground(False)
        icon13 = QIcon()
        icon13.addFile(u":/mainArcans/pic/main_arcans/poveshennyi.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_henged.setIcon(icon13)
        self.button_henged.setIconSize(QSize(117, 200))
        self.button_henged.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_henged)

        self.button_death = QToolButton(self.centralwidget)
        self.button_death.setObjectName(u"button_death")
        self.button_death.setFont(font1)
        self.button_death.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_death.setLayoutDirection(Qt.RightToLeft)
        self.button_death.setAutoFillBackground(False)
        icon14 = QIcon()
        icon14.addFile(u":/mainArcans/pic/main_arcans/smert.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_death.setIcon(icon14)
        self.button_death.setIconSize(QSize(117, 200))
        self.button_death.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_death)

        self.button_temperance = QToolButton(self.centralwidget)
        self.button_temperance.setObjectName(u"button_temperance")
        self.button_temperance.setFont(font1)
        self.button_temperance.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_temperance.setLayoutDirection(Qt.RightToLeft)
        self.button_temperance.setAutoFillBackground(False)
        icon15 = QIcon()
        icon15.addFile(u":/mainArcans/pic/main_arcans/umerennost.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_temperance.setIcon(icon15)
        self.button_temperance.setIconSize(QSize(117, 200))
        self.button_temperance.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_temperance)

        self.button_devil = QToolButton(self.centralwidget)
        self.button_devil.setObjectName(u"button_devil")
        self.button_devil.setFont(font1)
        self.button_devil.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_devil.setLayoutDirection(Qt.RightToLeft)
        self.button_devil.setAutoFillBackground(False)
        icon16 = QIcon()
        icon16.addFile(u":/mainArcans/pic/main_arcans/diyavol.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_devil.setIcon(icon16)
        self.button_devil.setIconSize(QSize(117, 200))
        self.button_devil.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.button_devil)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_tower = QToolButton(self.centralwidget)
        self.button_tower.setObjectName(u"button_tower")
        self.button_tower.setFont(font1)
        self.button_tower.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_tower.setLayoutDirection(Qt.RightToLeft)
        self.button_tower.setAutoFillBackground(False)
        icon17 = QIcon()
        icon17.addFile(u":/mainArcans/pic/main_arcans/padayushaya-bashnya.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_tower.setIcon(icon17)
        self.button_tower.setIconSize(QSize(117, 200))
        self.button_tower.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_tower)

        self.button_star = QToolButton(self.centralwidget)
        self.button_star.setObjectName(u"button_star")
        self.button_star.setFont(font1)
        self.button_star.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_star.setLayoutDirection(Qt.RightToLeft)
        self.button_star.setAutoFillBackground(False)
        icon18 = QIcon()
        icon18.addFile(u":/mainArcans/pic/main_arcans/zvezda.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_star.setIcon(icon18)
        self.button_star.setIconSize(QSize(117, 200))
        self.button_star.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_star)

        self.button_moon = QToolButton(self.centralwidget)
        self.button_moon.setObjectName(u"button_moon")
        self.button_moon.setFont(font1)
        self.button_moon.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_moon.setLayoutDirection(Qt.RightToLeft)
        self.button_moon.setAutoFillBackground(False)
        icon19 = QIcon()
        icon19.addFile(u":/mainArcans/pic/main_arcans/luna.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_moon.setIcon(icon19)
        self.button_moon.setIconSize(QSize(117, 200))
        self.button_moon.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_moon)

        self.button_sun = QToolButton(self.centralwidget)
        self.button_sun.setObjectName(u"button_sun")
        self.button_sun.setFont(font1)
        self.button_sun.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_sun.setLayoutDirection(Qt.RightToLeft)
        self.button_sun.setAutoFillBackground(False)
        icon20 = QIcon()
        icon20.addFile(u":/mainArcans/pic/main_arcans/solnce.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_sun.setIcon(icon20)
        self.button_sun.setIconSize(QSize(117, 200))
        self.button_sun.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_sun)

        self.button_judgement = QToolButton(self.centralwidget)
        self.button_judgement.setObjectName(u"button_judgement")
        self.button_judgement.setFont(font1)
        self.button_judgement.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_judgement.setLayoutDirection(Qt.RightToLeft)
        self.button_judgement.setAutoFillBackground(False)
        icon21 = QIcon()
        icon21.addFile(u":/mainArcans/pic/main_arcans/strashnyi-sud.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_judgement.setIcon(icon21)
        self.button_judgement.setIconSize(QSize(117, 200))
        self.button_judgement.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_judgement)

        self.button_world = QToolButton(self.centralwidget)
        self.button_world.setObjectName(u"button_world")
        self.button_world.setFont(font1)
        self.button_world.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_world.setLayoutDirection(Qt.RightToLeft)
        self.button_world.setAutoFillBackground(False)
        icon22 = QIcon()
        icon22.addFile(u":/mainArcans/pic/main_arcans/mir.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_world.setIcon(icon22)
        self.button_world.setIconSize(QSize(117, 200))
        self.button_world.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_3.addWidget(self.button_world)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainArcansWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainArcansWindow)

        QMetaObject.connectSlotsByName(MainArcansWindow)
    # setupUi

    def retranslateUi(self, MainArcansWindow):
        MainArcansWindow.setWindowTitle(QCoreApplication.translate("MainArcansWindow", u"\u0421\u0442\u0430\u0440\u0448\u0438\u0435 \u0410\u0440\u043a\u0430\u043d\u044b", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("MainArcansWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_fool.setText(QCoreApplication.translate("MainArcansWindow", u"\u0428\u0443\u0442", None))
        self.button_mage.setText(QCoreApplication.translate("MainArcansWindow", u"\u041c\u0430\u0433", None))
        self.button_pristess.setText(QCoreApplication.translate("MainArcansWindow", u"\u0416\u0440\u0438\u0446\u0430", None))
        self.button_empress.setText(QCoreApplication.translate("MainArcansWindow", u"\u0418\u043c\u043f\u0435\u0440\u0430\u0442\u0440\u0438\u0446\u0430", None))
        self.button_emperor.setText(QCoreApplication.translate("MainArcansWindow", u"\u0418\u043c\u043f\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.button_hierophant.setText(QCoreApplication.translate("MainArcansWindow", u"\u0416\u0440\u0435\u0446", None))
        self.button_lovers.setText(QCoreApplication.translate("MainArcansWindow", u"\u0412\u043b\u044e\u0431\u043b\u0451\u043d\u043d\u044b\u0435", None))
        self.button_chariot.setText(QCoreApplication.translate("MainArcansWindow", u"\u041a\u043e\u043b\u0435\u0441\u043d\u0438\u0446\u0430", None))
        self.button_strenght.setText(QCoreApplication.translate("MainArcansWindow", u"\u0421\u0438\u043b\u0430", None))
        self.button_hermit.setText(QCoreApplication.translate("MainArcansWindow", u"\u041e\u0442\u0448\u0435\u043b\u044c\u043d\u0438\u043a", None))
        self.button_fortune.setText(QCoreApplication.translate("MainArcansWindow", u"\u0424\u043e\u0440\u0442\u0443\u043d\u0430", None))
        self.button_justice.setText(QCoreApplication.translate("MainArcansWindow", u"\u0421\u043f\u0440\u0430\u0432\u0435\u0434\u043b\u0438\u0432\u043e\u0441\u0442\u044c", None))
        self.button_henged.setText(QCoreApplication.translate("MainArcansWindow", u"\u041f\u043e\u0432\u0435\u0448\u0435\u043d\u043d\u044b\u0439", None))
        self.button_death.setText(QCoreApplication.translate("MainArcansWindow", u"\u0421\u043c\u0435\u0440\u0442\u044c", None))
        self.button_temperance.setText(QCoreApplication.translate("MainArcansWindow", u"\u0423\u043c\u0435\u0440\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.button_devil.setText(QCoreApplication.translate("MainArcansWindow", u"\u0414\u044c\u044f\u0432\u043e\u043b", None))
        self.button_tower.setText(QCoreApplication.translate("MainArcansWindow", u"\u0411\u0430\u0448\u043d\u044f", None))
        self.button_star.setText(QCoreApplication.translate("MainArcansWindow", u"\u0417\u0432\u0435\u0437\u0434\u0430", None))
        self.button_moon.setText(QCoreApplication.translate("MainArcansWindow", u"\u041b\u0443\u043d\u0430", None))
        self.button_sun.setText(QCoreApplication.translate("MainArcansWindow", u"\u0421\u043e\u043b\u043d\u0446\u0435", None))
        self.button_judgement.setText(QCoreApplication.translate("MainArcansWindow", u"\u0421\u0443\u0434", None))
        self.button_world.setText(QCoreApplication.translate("MainArcansWindow", u"\u041c\u0438\u0440", None))
    # retranslateUi

