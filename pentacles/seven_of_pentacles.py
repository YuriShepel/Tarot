from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)
import main_pentacles_rc

class Ui_SevenOfPentacles(object):
    def setupUi(self, SevenOfPentacles):
        if not SevenOfPentacles.objectName():
            SevenOfPentacles.setObjectName(u"SevenOfPentacles")
        SevenOfPentacles.resize(850, 850)
        icon = QIcon()
        icon.addFile(u":/pentacles/pic/pentacles/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        SevenOfPentacles.setWindowIcon(icon)
        SevenOfPentacles.setStyleSheet(u" background-color: #0097e6")
        SevenOfPentacles.setAnimated(False)
        self.centralwidget = QWidget(SevenOfPentacles)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_back_to_menu = QPushButton(self.frame)
        self.button_back_to_menu.setObjectName(u"button_back_to_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_back_to_menu.sizePolicy().hasHeightForWidth())
        self.button_back_to_menu.setSizePolicy(sizePolicy)
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

        self.horizontalLayout.addWidget(self.button_back_to_menu)

        self.button_back_to_pentacles = QPushButton(self.frame)
        self.button_back_to_pentacles.setObjectName(u"button_back_to_pentacles")
        sizePolicy.setHeightForWidth(self.button_back_to_pentacles.sizePolicy().hasHeightForWidth())
        self.button_back_to_pentacles.setSizePolicy(sizePolicy)
        self.button_back_to_pentacles.setFont(font)
        self.button_back_to_pentacles.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_back_to_pentacles.setToolTipDuration(0)
        self.button_back_to_pentacles.setLayoutDirection(Qt.RightToLeft)
        self.button_back_to_pentacles.setStyleSheet(u"QPushButton{\n"
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
        self.button_back_to_pentacles.setIconSize(QSize(20, 21))
        self.button_back_to_pentacles.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.button_back_to_pentacles)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.picture = QLabel(self.frame)
        self.picture.setObjectName(u"picture")
        self.picture.setPixmap(QPixmap(u":/pentacles/pic/pentacles/semerka-pentaklei.jpg"))

        self.verticalLayout_2.addWidget(self.picture, 0, Qt.AlignHCenter)

        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.name.setFont(font1)

        self.verticalLayout_2.addWidget(self.name, 0, Qt.AlignHCenter)

        self.text = QTextBrowser(self.frame)
        self.text.setObjectName(u"text")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.text.setFont(font2)
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setAutoFormatting(QTextEdit.AutoNone)
        self.text.setOverwriteMode(False)

        self.verticalLayout_2.addWidget(self.text)


        self.verticalLayout.addWidget(self.frame)

        SevenOfPentacles.setCentralWidget(self.centralwidget)

        self.retranslateUi(SevenOfPentacles)

        QMetaObject.connectSlotsByName(SevenOfPentacles)
    # setupUi

    def retranslateUi(self, SevenOfPentacles):
        SevenOfPentacles.setWindowTitle(QCoreApplication.translate("SevenOfPentacles", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430 \u041f\u0435\u043d\u0442\u0430\u043a\u043b\u0435\u0439", None))
        self.button_back_to_menu.setText(QCoreApplication.translate("SevenOfPentacles", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043e\u043a\u043d\u043e", None))
        self.button_back_to_pentacles.setText(QCoreApplication.translate("SevenOfPentacles", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u043f\u0435\u043d\u0442\u0430\u043a\u043b\u044f\u043c", None))
        self.picture.setText("")
        self.name.setText(QCoreApplication.translate("SevenOfPentacles", u"\u0421\u0435\u043c\u0451\u0440\u043a\u0430 \u041f\u0435\u043d\u0442\u0430\u043a\u043b\u0435\u0439", None))
        self.text.setHtml(QCoreApplication.translate("SevenOfPentacles", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u041f\u0440\u044f\u043c\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0412\u0430\u0436\u043d\u044b\u0439 \u043a\u0440\u0438\u0442\u0435\u0440"
                        "\u0438\u0439 \u0443\u0441\u043f\u0435\u0445\u0430 \u0432 \u0434\u0435\u043b\u0435 \u2013 \u0431\u044b\u0442\u044c \u0442\u0435\u0440\u043f\u0435\u043b\u0438\u0432\u044b\u043c. \u0412 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 \u0433\u043e\u0434\u0430 \u0432\u0430\u0448 \u0442\u0440\u0443\u0434 \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0432\u043e\u0437\u043d\u0430\u0433\u0440\u0430\u0434\u044f\u0442 \u0434\u043e\u0441\u0442\u043e\u0439\u043d\u043e\u0439 \u043e\u043f\u043b\u0430\u0442\u043e\u0439. \u041d\u0435 \u043f\u0435\u0440\u0435\u0436\u0438\u0432\u0430\u0439\u0442\u0435 \u0437\u0430 \u0442\u043e, \u0447\u0442\u043e \u0443\u0441\u0438\u043b\u0438\u044f \u043e\u043a\u0430\u0436\u0443\u0442\u0441\u044f \u043d\u0430\u043f\u0440\u0430\u0441\u043d\u044b\u043c\u0438, \u0434\u0430\u0436\u0435 \u0435\u0441\u043b\u0438 \u0432\u043e\u0437\u043d\u0438\u043a\u0430\u0435\u0442 \u043f\u043e\u0434\u043e\u0431\u043d\u043e\u0435 \u043f\u0440\u0435\u0434\u0447\u0443\u0432\u0441\u0442\u0432\u0438\u0435"
                        " \u2013 \u043e\u043d\u043e \u043b\u043e\u0436\u043d\u043e\u0435.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0415\u0441\u043b\u0438 \u0440\u0430\u0431\u043e\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430, \u0430 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u0432\u0441\u0435 \u043d\u0435\u0442, \u0442\u043e \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043f\u043e\u0434\u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043b\u0438\u0431\u043e \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0447\u0442\u043e-\u0442\u043e \u0434\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0435. \u0410\u0440\u043a\u0430\u043d \u0441\u0432\u0438\u0434\u0435\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0443\u0435\u0442 \u043e \u043b\u0438\u0447\u043d\u043e"
                        "\u0441\u0442\u043d\u043e\u043c \u0440\u043e\u0441\u0442\u0435 \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0432\u0440\u0435\u043c\u0435\u043d\u0438, \u043d\u043e \u043e\u043d \u0431\u0443\u0434\u0435\u0442 \u043e\u0447\u0435\u043d\u044c \u043c\u0435\u0434\u043b\u0435\u043d\u043d\u044b\u043c.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u041f\u0435\u0440\u0435\u0434 \u0442\u0435\u043c, \u043a\u0430\u043a \u043d\u0430\u0447\u0430\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0434\u0435\u043b\u043e, \u043f\u0440\u0435\u0434\u0441\u0442\u043e\u0438\u0442 \u0432\u0437\u0432\u0435\u0441\u0438\u0442\u044c, \u0441\u0442\u043e\u0438\u0442 \u043b\u0438 \u044d\u0442\u0438\u043c \u0437\u0430\u043d\u0438\u043c\u0430\u0442\u044c\u0441\u044f, \u0447\u0442\u043e \u0441 \u044d\u0442\u043e\u0433"
                        "\u043e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c. \u041d\u0438\u043a\u043e\u0433\u0434\u0430 \u043d\u0435 \u0442\u043e\u0440\u043e\u043f\u0438\u0442\u0435\u0441\u044c, \u044d\u0442\u043e \u043d\u0430\u043e\u0431\u043e\u0440\u043e\u0442 \u043e\u0442\u043e\u0434\u0432\u0438\u043d\u0435\u0442 \u043a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u041f\u0435\u0440\u0435\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roma"
                        "n','serif'; font-size:14pt;\">\u0418\u0437\u0431\u0435\u0433\u0430\u0439\u0442\u0435 \u0430\u0432\u0430\u043d\u0442\u044e\u0440\u043d\u044b\u0445 \u0434\u0435\u043b \u0438 \u0430\u0437\u0430\u0440\u0442\u043d\u044b\u0445 \u0438\u0433\u0440, \u0432\u0435\u0434\u044c \u0441\u0435\u0439\u0447\u0430\u0441 \u0444\u043e\u0440\u0442\u0443\u043d\u0430 \u043d\u0435 \u043d\u0430 \u0432\u0430\u0448\u0435\u0439 \u0441\u0442\u043e\u0440\u043e\u043d\u0435. \u041a\u0430\u0440\u0442\u0430 \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u043e \u0431\u044b\u0441\u0442\u0440\u043e\u043c \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u0435 \u0432 \u043f\u0443\u0441\u0442\u043e\u0442\u0443, \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043d\u0435 \u043d\u0435\u0441\u0435\u0442 \u0441\u0435\u0431\u0435 \u043d\u0438\u0447\u0435\u0433\u043e \u043f\u043e\u043b\u0435\u0437\u043d\u043e\u0433\u043e: \u043d\u0438 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439, \u043d\u0438 \u0448\u0430\u043d\u0441\u043e\u0432, \u043d\u0438"
                        " \u0443\u0441\u043f\u0435\u0445\u0430.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0415\u0441\u0442\u044c \u0432\u0435\u0440\u043e\u044f\u0442\u043d\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0431\u043b\u0435\u043c \u0441\u043e \u0437\u0434\u043e\u0440\u043e\u0432\u044c\u0435\u043c, \u0437\u0430\u0431\u043e\u043b\u0435\u0432\u0430\u043d\u0438\u0435 \u0441\u0432\u044f\u0437\u0430\u043d\u043e \u0441 \u0438\u043d\u0444\u0435\u043a\u0446\u0438\u0435\u0439. \u0418\u0437\u0431\u0435\u0433\u0430\u0439\u0442\u0435 \u0442\u0430\u043a\u0438\u0445 \u044d\u043c\u043e\u0446\u0438\u0439 \u043a\u0430\u043a \u043d\u0435\u0442\u0435\u0440\u043f\u0435\u043d\u0438\u0435, \u043d\u0435\u0440\u0432\u043e\u0437\u043d\u043e\u0441\u0442\u044c \u0438 \u0431\u0435\u0441\u043f\u043e\u043a\u043e\u0439\u0441\u0442\u0432\u043e, \u0438\u043d\u0430\u0447\u0435"
                        " \u043d\u0430\u0441\u0442\u0443\u043f\u0438\u0442 \u043f\u0435\u0440\u0438\u043e\u0434 \u0434\u0435\u043f\u0440\u0435\u0441\u0441\u0438\u0438.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u043b\u044e\u0431\u0432\u0438 \u0438 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f\u0445</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-style:italic;\">\u041f\u0440\u044f\u043c\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; tex"
                        "t-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0412 \u0433\u0430\u0434\u0430\u043d\u0438\u0438 \u043d\u0430 \u043b\u044e\u0431\u043e\u0432\u044c \u0438 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f, \u043a\u0430\u0440\u0442\u0430 \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u043e\u0431 \u0443\u0445\u0443\u0434\u0448\u0435\u043d\u0438\u0438 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u0439 \u043c\u0435\u0436\u0434\u0443 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430\u043c\u0438, \u043d\u0430\u0440\u0443\u0448\u0435\u043d\u0438\u0438 \u0433\u0430\u0440\u043c\u043e\u043d\u0438\u0438 \u0438 \u043f\u043e\u0442\u0435\u0440\u0438 \u0434\u043e\u0432\u0435\u0440\u0438\u044f.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0412\u0430\u0436\u043d\u043e, \u043f\u0440\u0438\u043d\u0438\u043c"
                        "\u0430\u0442\u044c \u0431\u043b\u0438\u0437\u043a\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430 \u0442\u0430\u043a\u0438\u043c, \u043a\u0430\u043a\u043e\u0439 \u043e\u043d \u0435\u0441\u0442\u044c, \u043d\u0435 \u0441\u0442\u043e\u0438\u0442 \u0435\u0433\u043e \u043f\u0435\u0440\u0435\u0432\u043e\u0441\u043f\u0438\u0442\u0430\u0442\u044c. \u041d\u0435 \u043d\u0443\u0436\u043d\u043e \u043a\u0440\u0438\u0442\u0438\u043a\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0435 \u0435\u0433\u043e \u0441\u043b\u043e\u0432\u0430 \u0438 \u043f\u043e\u0441\u0442\u0443\u043f\u043a\u0438, \u043e\u0441\u0443\u0436\u0434\u0430\u0442\u044c. \u0411\u0443\u0434\u0435\u0442 \u0433\u043e\u0440\u0430\u0437\u0434\u043e \u043b\u0443\u0447\u0448\u0435, \u0435\u0441\u043b\u0438 \u0432\u044b \u0441\u043f\u043e\u043a\u043e\u0439\u043d\u043e \u043f\u043e\u0433\u043e\u0432\u043e\u0440\u0438\u0442\u0435 \u043d\u0430 \u044d\u0442\u0443 \u0442\u0435\u043c\u0443.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; m"
                        "argin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0415\u0441\u043b\u0438 \u0433\u0430\u0434\u0430\u044e\u0449\u0438\u0439 \u043f\u0440\u043e\u0441\u0438\u0442 \u0443 \u043a\u0430\u0440\u0442\u044b \u0441\u043e\u0432\u0435\u0442, \u0441\u0442\u043e\u0438\u0442 \u043b\u0438 \u0441\u043e\u0445\u0440\u0430\u043d\u044f\u0442\u044c \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f \u0438\u043b\u0438 \u0440\u0430\u0437\u0432\u043e\u0434\u0438\u0442\u044c\u0441\u044f, \u0441\u0435\u043c\u0435\u0440\u043a\u0430 \u043f\u0435\u043d\u0442\u0430\u043a\u043b\u0435\u0439 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442, \u0447\u0442\u043e \u043d\u0435\u043b\u044c\u0437\u044f \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0442\u0430\u043a\u0438\u0435 \u043e\u0447\u0435\u043d\u044c \u0431\u044b\u0441\u0442\u0440\u043e \u0440\u0435\u0448\u0435\u043d\u0438\u044f. \u0421\u043b"
                        "\u0435\u0434\u0443\u0435\u0442 \u0445\u043e\u0440\u043e\u0448\u043e \u043e\u0431\u043e \u0432\u0441\u0435\u043c \u043f\u043e\u0434\u0443\u043c\u0430\u0442\u044c, \u0430 \u0437\u0430\u0442\u0435\u043c \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0440\u0435\u0448\u0435\u043d\u0438\u0435.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u041f\u0435\u0440\u0435\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u041a\u0430\u0440\u0442\u0430 \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u043e\u0431 \u043e\u0442\u0441\u0443\u0442\u0441"
                        "\u0442\u0432\u0438\u0438 \u0433\u0430\u0440\u043c\u043e\u043d\u0438\u0438 \u0432 \u043e\u0442\u043d\u043e\u0448\u0435\u043d\u0438\u044f\u0445. \u0420\u0435\u0448\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u043a\u043e\u043c\u043f\u0440\u043e\u043c\u0438\u0441\u0441, \u0431\u0443\u0434\u0435\u0442 \u043a\u0440\u0430\u0439\u043d\u0435 \u0441\u043b\u043e\u0436\u043d\u043e \u043e\u0431\u043e\u0438\u043c \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430\u043c. \u0412\u0430\u0448\u0430 \u0432\u0442\u043e\u0440\u0430\u044f \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u043a\u0430, \u0431\u0443\u043a\u0432\u0430\u043b\u044c\u043d\u043e \u0442\u044f\u0433\u043e\u0442\u0438\u0442 \u0432\u0430\u0441 \u0438 \u0440\u0430\u0437\u0434\u0440\u0430\u0436\u0430\u0435\u0442. \u0412\u043e\u0437\u043c\u043e\u0436\u043d\u043e, \u043a\u0442\u043e-\u0442\u043e \u0438\u0437 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432 \u0438\u0437\u043c\u0435\u043d\u044f\u0435\u0442 \u0431\u0435\u0437 \u0437\u0430\u0437\u0440\u0435\u043d\u0438\u044f"
                        " \u0441\u043e\u0432\u0435\u0441\u0442\u0438.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0438 \u0438 \u0432\u043e\u043f\u0440\u043e\u0441\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-style:italic;\">\u041f\u0440\u044f\u043c\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u041a\u0430"
                        "\u0440\u0442\u0430 \u0442\u0440\u0430\u043a\u0442\u0443\u0435\u0442\u0441\u044f \u043a\u0430\u043a \u0443\u0441\u043f\u0435\u0448\u043d\u043e\u0435 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u0434\u0435\u043b, \u043d\u0435\u0441\u043c\u043e\u0442\u0440\u044f \u043d\u0430 \u043f\u043e\u0441\u0442\u043e\u044f\u043d\u043d\u043e\u0435 \u0441\u043e\u043c\u043d\u0435\u043d\u0438\u0435 \u0432 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u0438\u043b\u0430\u0445, \u0431\u043e\u043b\u044c\u0448\u043e\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u0435\u0433\u0440\u0430\u0434 \u0438 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u043d\u0430 \u043f\u0443\u0442\u0438 \u043a \u0434\u043e\u0441\u0442\u0438\u0436\u0435\u043d\u0438\u044e \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u043d\u043e\u0439 \u0446\u0435\u043b\u0438.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px"
                        "; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0415\u0441\u043b\u0438 \u043f\u043e\u0434\u0441\u043e\u0437\u043d\u0430\u043d\u0438\u0435 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442, \u0447\u0442\u043e \u0441\u0435\u0439\u0447\u0430\u0441 \u043d\u0435 \u043b\u0443\u0447\u0448\u0435\u0435 \u0432\u0440\u0435\u043c\u044f \u0447\u0442\u043e-\u0442\u043e \u0440\u0435\u0448\u0430\u0442\u044c \u0438\u043b\u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0442\u044c, \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0435\u0441\u044c \u0438 \u043e\u0442\u0434\u043e\u0445\u043d\u0438\u0442\u0435, \u0441\u0434\u0435\u043b\u0430\u0439\u0442\u0435 \u043f\u0430\u0443\u0437\u0443. \u042d\u0442\u043e \u043f\u0440\u0438\u0432\u0435\u0434\u0435\u0442 \u0432\u0430\u0448\u0438 \u043c\u044b\u0441\u043b\u0438 \u0432 \u043d\u043e\u0440\u043c\u0443, \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e, \u043f\u043e\u044f\u0432"
                        "\u0438\u0442\u0441\u044f \u0431\u043b\u0435\u0441\u0442\u044f\u0449\u0430\u044f \u0438\u0434\u0435\u044f, \u043a\u0430\u043a \u0440\u0430\u0437\u0440\u0435\u0448\u0438\u0442\u044c \u0442\u043e\u0442 \u0438\u043b\u0438 \u0438\u043d\u043e\u0439 \u0432\u043e\u043f\u0440\u043e\u0441.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0412 \u0442\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u043a\u043e\u0433\u0434\u0430 \u0433\u0430\u0434\u0430\u044e\u0449\u0438\u0439 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u043d\u0430\u0434 \u0447\u0435\u043c-\u0442\u043e \u0434\u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e \u0434\u043e\u043b\u0433\u043e, \u0432\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u0435\u0442 \u0432 \u044d\u0442\u043e \u0434\u0435\u043b\u043e \u043c\u043d\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u0435\u043d"
                        "\u0438, \u0441\u0438\u043b \u0438 \u043d\u0435\u0440\u0432\u043e\u0432, \u0442\u043e \u0432 \u0431\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0439 \u043f\u0435\u0440\u0438\u043e\u0434 \u0436\u0434\u0435\u0442 \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u0431\u043b\u0430\u0433\u043e\u043f\u043e\u043b\u0443\u0447\u043d\u0430\u044f \u0440\u0430\u0437\u0432\u044f\u0437\u043a\u0430.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-style:italic;\">\u041f\u0435\u0440\u0435\u0432\u0435\u0440\u043d\u0443\u0442\u043e\u0435 \u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0421\u0442\u043e\u0438\u0442"
                        " \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0432\u0441\u0435 \u0432\u0437\u0432\u0435\u0441\u0438\u0442\u044c, \u0441\u043e\u0441\u0440\u0435\u0434\u043e\u0442\u043e\u0447\u0438\u0442\u044c\u0441\u044f \u043d\u0430 \u0447\u0435\u043c-\u0442\u043e \u043e\u0434\u043d\u043e\u043c, \u0447\u0442\u043e \u0438\u043c\u0435\u0435\u0442 \u0448\u0430\u043d\u0441\u044b \u043d\u0430 \u0443\u0441\u043f\u0435\u0445. \u041c\u0435\u043d\u0435\u0435 \u0432\u0430\u0436\u043d\u044b\u0435 \u0434\u0435\u043b\u0430 \u0441\u0442\u043e\u0438\u0442 \u043e\u0442\u043b\u043e\u0436\u0438\u0442\u044c \u043d\u0430 \u043f\u043e\u0442\u043e\u043c, \u0442.\u043a \u043e\u043d\u0438 \u0431\u0443\u0434\u0443\u0442 \u043c\u0435\u0448\u0430\u0442\u044c \u0434\u0432\u0438\u0436\u0435\u043d\u0438\u044e \u0432\u043f\u0435\u0440\u0435\u0434.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman"
                        "','serif'; font-size:14pt;\">\u0415\u0441\u043b\u0438 \u0438\u043d\u0442\u0443\u0438\u0446\u0438\u044f \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442, \u0447\u0442\u043e \u043f\u043e\u044f\u0432\u044f\u0442\u0441\u044f \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u044b \u0441 \u0434\u0435\u043d\u044c\u0433\u0430\u043c\u0438, \u044d\u0442\u043e \u043e\u043f\u0440\u0430\u0432\u0434\u0430\u043d\u043e. \u0418\u043c\u0435\u043d\u043d\u043e \u0438\u0437-\u0437\u0430 \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u044b\u0445 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u043f\u0440\u0438\u0434\u0435\u0442\u0441\u044f \u043e\u0442\u043a\u0430\u0437\u0430\u0442\u044c\u0441\u044f \u043e\u0442 \u043c\u043d\u043e\u0433\u0438\u0445 \u043f\u0440\u0435\u043b\u0435\u0441\u0442\u0435\u0439 \u0432 \u0436\u0438\u0437\u043d\u0438.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><sp"
                        "an style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u041d\u0435 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u0442\u0441\u044f \u0431\u0440\u0430\u0442\u044c \u0434\u0435\u043d\u044c\u0433\u0438 \u0432 \u0434\u043e\u043b\u0433, \u0434\u0435\u043b\u0430\u0442\u044c \u043a\u0440\u0443\u043f\u043d\u044b\u0435 \u043f\u043e\u043a\u0443\u043f\u043a\u0438, \u0442.\u043a \u044d\u0442\u043e \u043c\u043e\u0436\u0435\u0442 \u0443\u0441\u0443\u0433\u0443\u0431\u0438\u0442\u044c \u0444\u0438\u043d\u0430\u043d\u0441\u043e\u0432\u0443\u044e \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u0443.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u044b \u0434\u043d\u044f</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; m"
                        "argin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u0421\u0435\u0433\u043e\u0434\u043d\u044f\u0448\u043d\u0438\u0439 \u0434\u0435\u043d\u044c \u044f\u0432\u043d\u043e \u043d\u0435 \u0434\u043b\u044f \u0441\u043f\u0435\u0448\u043a\u0438, \u0441\u0442\u043e\u0438\u0442 \u0431\u044b\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u0442\u0435\u0440\u043f\u0435\u043b\u0438\u0432\u044b\u043c\u0438, \u043d\u0435\u0441\u043f\u0435\u0448\u043d\u044b\u043c\u0438. \u041f\u0440\u0438\u043d\u0438\u043c\u0430\u0439\u0442\u0435 \u0432\u043e \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435 \u043a\u0430\u0436\u0434\u0443\u044e \u0434\u0435\u0442\u0430\u043b\u044c, \u0432\u0437\u0432\u0435\u0448\u0438\u0432\u0430\u0439\u0442\u0435 \u0432 \u0433\u043e\u043b\u043e\u0432\u0435 \u043a\u0430\u0436\u0434\u043e\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u0435, \u043f\u0440\u0435\u0436\u0434\u0435 \u0447\u0435\u043c \u0443\u0442"
                        "\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0435\u0433\u043e. \u041b\u044e\u0431\u0430\u044f \u043e\u043f\u043b\u043e\u0448\u043d\u043e\u0441\u0442\u044c \u0441\u0435\u0433\u043e\u0434\u043d\u044f \u0441\u043f\u0440\u043e\u0432\u043e\u0446\u0438\u0440\u0443\u0435\u0442 \u043f\u043e\u044f\u0432\u043b\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u0436\u043d\u044b\u0445 \u0441\u0438\u0442\u0443\u0430\u0446\u0438\u0439, \u0440\u0435\u0448\u0435\u043d\u0438\u0435 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u043f\u043e\u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u0432 \u0431\u0443\u0434\u0443\u0449\u0435\u043c \u0431\u043e\u043b\u044c\u0448\u0438\u0445 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0438 \u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0437\u0430\u0442\u0440\u0430\u0442.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style="
                        "\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u041d\u0435\u0442 \u0441\u043c\u044b\u0441\u043b\u0430 \u043d\u0430\u0440\u0443\u0448\u0430\u0442\u044c \u043f\u043b\u0430\u043d\u044b, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u0434\u043e\u043b\u0433\u043e \u0438 \u043c\u0443\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u0435\u0442\u0432\u043e\u0440\u044f\u044e\u0442\u0441\u044f \u0432 \u0436\u0438\u0437\u043d\u044c. \u0415\u0441\u043b\u0438 \u043d\u0430\u0441\u0442\u0440\u043e\u044f \u043d\u0430 \u0442\u0435\u0440\u043f\u0435\u043d\u0438\u0435 \u043d\u0435\u0442, \u043f\u0440\u043e\u0441\u0442\u043e \u0432\u043e\u0437\u044c\u043c\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0434\u044b\u0448\u043a\u0443, \u043e\u0442\u0434\u043e\u0445\u043d\u0438\u0442\u0435, \u043f\u0440\u043e\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0440\u0435\u043c\u044f \u0441 \u043f\u043e\u043b\u044c\u0437\u043e\u0439, \u0443\u0434\u0435\u043b\u0438\u0442\u0435 \u0432\u043d\u0438\u043c\u0430\u043d\u0438\u0435"
                        " \u0441\u0430\u043c\u044b\u043c \u0431\u043b\u0438\u0437\u043a\u0438\u043c, \u0443\u0434\u0438\u0432\u0438\u0442\u0435 \u043f\u0440\u0438\u044f\u0442\u043d\u044b\u043c \u0441\u044e\u0440\u043f\u0440\u0438\u0437\u043e\u043c \u043b\u044e\u0431\u0438\u043c\u043e\u0433\u043e \u0447\u0435\u043b\u043e\u0432\u0435\u043a\u0430. \u0414\u043e\u0431\u0440\u043e \u043e\u0431\u044f\u0437\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0431\u0443\u0434\u0435\u0442 \u0432\u0430\u043c \u0432\u043e\u0437\u0432\u0440\u0430\u0449\u0435\u043d\u043e.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt; font-weight:700;\">\u0421\u043e\u0432\u0435\u0442 \u043a\u0430\u0440\u0442\u044b</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'"
                        "Times New Roman','serif'; font-size:14pt;\">\u041a\u0430\u0440\u0442\u0430 \u0433\u043e\u0432\u043e\u0440\u0438\u0442 \u043e \u0442\u043e\u043c, \u0447\u0442\u043e \u043d\u0435 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u0431\u044b\u0441\u0442\u0440\u043e \u0438 \u0438\u043c\u043f\u0443\u043b\u044c\u0441\u0438\u0432\u043d\u043e \u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u044c \u0432\u0430\u0436\u043d\u044b\u0435 \u0440\u0435\u0448\u0435\u043d\u0438\u044f. \u0412\u0430\u0436\u043d\u043e \u0432\u0441\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e \u0432\u0437\u0432\u0435\u0441\u0438\u0442\u044c \u0438 \u043e\u0431\u0434\u0443\u043c\u0430\u0442\u044c, \u0438 \u0435\u0441\u043b\u0438 \u0432\u0430\u0441 \u043a\u0442\u043e-\u0442\u043e \u0442\u043e\u0440\u043e\u043f\u0438\u0442 \u0432 \u043f\u0440\u0438\u043d\u044f\u0442\u0438\u0438 \u0440\u0435\u0448\u0435\u043d\u0438\u044f, \u0442\u043e \u0432\u043e\u0437\u044c\u043c\u0438\u0442\u0435 \u043e\u0442\u0441\u0440\u043e\u0447\u043a\u0443. \u0412 \u043f"
                        "\u0440\u043e\u0442\u0438\u0432\u043d\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u0432\u044b \u0440\u0438\u0441\u043a\u0443\u0435\u0442\u0435 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043d\u0435\u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u043e\u0441\u043b\u0435\u0434\u0441\u0442\u0432\u0438\u044f, \u043d\u0430 \u0432\u043e\u0441\u0441\u0442\u0430\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u043a\u043e\u0442\u043e\u0440\u044b\u0445 \u0443\u0439\u0434\u0443\u0442 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0438 \u044d\u043d\u0435\u0440\u0433\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0440\u0435\u0441\u0443\u0440\u0441\u044b.</span> </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Times New Roman','serif'; font-size:14pt;\">\u00a0</span> </p></body></html>", None))
    # retranslateUi

