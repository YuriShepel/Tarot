# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomrjyPAT.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import main_win_taro_rc

class Ui_RandomWin(object):
    def setupUi(self, RandomWin):
        if not RandomWin.objectName():
            RandomWin.setObjectName(u"RandomWin")
        RandomWin.resize(570, 364)
        icon = QIcon()
        icon.addFile(u":/mainTaroWin/pic/main_taro_pic/tarot_ico.png", QSize(), QIcon.Normal, QIcon.Off)
        RandomWin.setWindowIcon(icon)
        RandomWin.setStyleSheet(u" background-color: #0097e6")
        self.centralwidget = QWidget(RandomWin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(12)
        font.setBold(True)
        self.textBrowser.setFont(font)

        self.verticalLayout.addWidget(self.textBrowser)

        RandomWin.setCentralWidget(self.centralwidget)

        self.retranslateUi(RandomWin)

        QMetaObject.connectSlotsByName(RandomWin)
    # setupUi

    def retranslateUi(self, RandomWin):
        RandomWin.setWindowTitle(QCoreApplication.translate("RandomWin", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("RandomWin", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Arial Black'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

