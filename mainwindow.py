# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QTabWidget, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hedding = QLabel(self.centralwidget)
        self.hedding.setObjectName(u"hedding")
        self.hedding.setLayoutDirection(Qt.LeftToRight)
        self.hedding.setStyleSheet(u"font: 700 18pt \"Ubuntu\";")
        self.hedding.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.hedding)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Options = QTreeWidget(self.centralwidget)
        QTreeWidgetItem(self.Options)
        QTreeWidgetItem(self.Options)
        QTreeWidgetItem(self.Options)
        self.Options.setObjectName(u"Options")
        self.Options.setStyleSheet(u"QTreeWidget::item{\n"
"	font: 700 15pt \"Ubuntu Mono\";\n"
"	border-radius:2px;\n"
"	padding-top:10px;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Options)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_10 = QGridLayout(self.page_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tabWidget_3 = QTabWidget(self.page_2)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.gridLayout_9 = QGridLayout(self.widget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.uploadexe_btn = QPushButton(self.widget)
        self.uploadexe_btn.setObjectName(u"uploadexe_btn")

        self.horizontalLayout_12.addWidget(self.uploadexe_btn)

        self.uploadexe_line = QLineEdit(self.widget)
        self.uploadexe_line.setObjectName(u"uploadexe_line")

        self.horizontalLayout_12.addWidget(self.uploadexe_line)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.uploadimg_btn = QPushButton(self.widget)
        self.uploadimg_btn.setObjectName(u"uploadimg_btn")

        self.horizontalLayout_11.addWidget(self.uploadimg_btn)

        self.uploadimage_line = QLineEdit(self.widget)
        self.uploadimage_line.setObjectName(u"uploadimage_line")

        self.horizontalLayout_11.addWidget(self.uploadimage_line)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.processimgexe = QPushButton(self.widget)
        self.processimgexe.setObjectName(u"processimgexe")

        self.horizontalLayout_15.addWidget(self.processimgexe)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.gridLayout_9.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.tabWidget_3.addTab(self.widget, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.decodeexe_btn = QPushButton(self.tab_2)
        self.decodeexe_btn.setObjectName(u"decodeexe_btn")

        self.horizontalLayout_13.addWidget(self.decodeexe_btn)

        self.decodeexex_line = QLineEdit(self.tab_2)
        self.decodeexex_line.setObjectName(u"decodeexex_line")

        self.horizontalLayout_13.addWidget(self.decodeexex_line)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.processdecodeexe = QPushButton(self.tab_2)
        self.processdecodeexe.setObjectName(u"processdecodeexe")

        self.horizontalLayout_14.addWidget(self.processdecodeexe)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.gridLayout_8.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_2, "")

        self.gridLayout_10.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        self.gridLayout_2 = QGridLayout(self.page_0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.page_0)
        self.tabWidget.setObjectName(u"tabWidget")
        self.img_encode = QWidget()
        self.img_encode.setObjectName(u"img_encode")
        self.gridLayout_3 = QGridLayout(self.img_encode)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.img_encode)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.path_encode_img = QLineEdit(self.img_encode)
        self.path_encode_img.setObjectName(u"path_encode_img")

        self.horizontalLayout_2.addWidget(self.path_encode_img)

        self.open_encode_img = QPushButton(self.img_encode)
        self.open_encode_img.setObjectName(u"open_encode_img")

        self.horizontalLayout_2.addWidget(self.open_encode_img)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.img_enode_holder = QLabel(self.img_encode)
        self.img_enode_holder.setObjectName(u"img_enode_holder")
        self.img_enode_holder.setMinimumSize(QSize(350, 0))
        self.img_enode_holder.setMaximumSize(QSize(400, 16777215))
        self.img_enode_holder.setFrameShadow(QFrame.Raised)
        self.img_enode_holder.setPixmap(QPixmap(u"../../../../../../../Pictures/WhatsApp Image 2023-11-03 at 12.21.56 AM.jpeg"))
        self.img_enode_holder.setScaledContents(True)
        self.img_enode_holder.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.img_enode_holder, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 15)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3.setStretch(2, 4)
        self.verticalLayout_3.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.img_encode)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.img_encode, "")
        self.img_decode = QWidget()
        self.img_decode.setObjectName(u"img_decode")
        self.gridLayout_4 = QGridLayout(self.img_decode)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.img_decode)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.img_decode_open = QPushButton(self.img_decode)
        self.img_decode_open.setObjectName(u"img_decode_open")

        self.horizontalLayout_5.addWidget(self.img_decode_open)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.img_decode_holder = QLabel(self.img_decode)
        self.img_decode_holder.setObjectName(u"img_decode_holder")
        self.img_decode_holder.setMinimumSize(QSize(350, 0))
        self.img_decode_holder.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.img_decode_holder)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.decode_img_text = QTextEdit(self.img_decode)
        self.decode_img_text.setObjectName(u"decode_img_text")

        self.verticalLayout_9.addWidget(self.decode_img_text)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)

        self.verticalLayout_7.setStretch(2, 4)
        self.verticalLayout_7.setStretch(3, 1)

        self.verticalLayout_10.addLayout(self.verticalLayout_7)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.tabWidget.addTab(self.img_decode, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_6 = QGridLayout(self.page_1)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_2 = QTabWidget(self.page_1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_5 = QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.tab_3)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.primary_img = QPushButton(self.tab_3)
        self.primary_img.setObjectName(u"primary_img")

        self.horizontalLayout_9.addWidget(self.primary_img)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.seconday_img = QPushButton(self.tab_3)
        self.seconday_img.setObjectName(u"seconday_img")

        self.horizontalLayout_9.addWidget(self.seconday_img)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 25, -1, 25)
        self.img_img_primary = QLabel(self.tab_3)
        self.img_img_primary.setObjectName(u"img_img_primary")
        self.img_img_primary.setScaledContents(True)
        self.img_img_primary.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.img_img_primary)

        self.img_img_secondary = QLabel(self.tab_3)
        self.img_img_secondary.setObjectName(u"img_img_secondary")
        self.img_img_secondary.setScaledContents(True)
        self.img_img_secondary.setAlignment(Qt.AlignCenter)
        self.img_img_secondary.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.img_img_secondary)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.img_img_export = QPushButton(self.tab_3)
        self.img_img_export.setObjectName(u"img_img_export")

        self.horizontalLayout_7.addWidget(self.img_img_export)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.verticalLayout_11.setStretch(2, 2)

        self.gridLayout_5.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.tab_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_15.addWidget(self.label_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.open_encode_img_2 = QPushButton(self.tab_4)
        self.open_encode_img_2.setObjectName(u"open_encode_img_2")

        self.horizontalLayout_10.addWidget(self.open_encode_img_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_10)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(25, 25, 25, 25)
        self.img_img_decode = QLabel(self.tab_4)
        self.img_img_decode.setObjectName(u"img_img_decode")
        self.img_img_decode.setMinimumSize(QSize(350, 0))

        self.verticalLayout_14.addWidget(self.img_img_decode, 0, Qt.AlignHCenter)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButton_2 = QPushButton(self.tab_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_8.addWidget(self.pushButton_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_8)

        self.verticalLayout_15.setStretch(2, 2)

        self.gridLayout_7.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.gridLayout_6.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_1)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.Options, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.path_encode_img)
        QWidget.setTabOrder(self.path_encode_img, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.img_decode_open)
        QWidget.setTabOrder(self.img_decode_open, self.decode_img_text)
        QWidget.setTabOrder(self.decode_img_text, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.primary_img)
        QWidget.setTabOrder(self.primary_img, self.img_img_export)
        QWidget.setTabOrder(self.img_img_export, self.open_encode_img_2)
        QWidget.setTabOrder(self.open_encode_img_2, self.pushButton_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hedding.setText(QCoreApplication.translate("MainWindow", u"Stenography", None))
        ___qtreewidgetitem = self.Options.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Opertions", None));

        __sortingEnabled = self.Options.isSortingEnabled()
        self.Options.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.Options.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Image Encode", None));
        ___qtreewidgetitem2 = self.Options.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Image to Image Encode", None));
        ___qtreewidgetitem3 = self.Options.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Image exe Encode", None));
        self.Options.setSortingEnabled(__sortingEnabled)

        self.uploadexe_btn.setText(QCoreApplication.translate("MainWindow", u"Upload exe", None))
        self.uploadimg_btn.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.processimgexe.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.widget), QCoreApplication.translate("MainWindow", u"Image exe Encode", None))
        self.decodeexe_btn.setText(QCoreApplication.translate("MainWindow", u"Decode", None))
        self.processdecodeexe.setText(QCoreApplication.translate("MainWindow", u"Process", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Image exe Decode", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Encode Image With Text", None))
        self.open_encode_img.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.img_enode_holder.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.img_encode), QCoreApplication.translate("MainWindow", u"Encode Text", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Decode Image", None))
        self.img_decode_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.img_decode_holder.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.img_decode), QCoreApplication.translate("MainWindow", u"Decode Text", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hide Image inside Image", None))
        self.primary_img.setText(QCoreApplication.translate("MainWindow", u"Primary Image", None))
        self.seconday_img.setText(QCoreApplication.translate("MainWindow", u"Seconday Image", None))
        self.img_img_primary.setText(QCoreApplication.translate("MainWindow", u"Primary Image", None))
        self.img_img_secondary.setText(QCoreApplication.translate("MainWindow", u"Seconday Image", None))
        self.img_img_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Encode", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Decode Hiddin Image", None))
        self.open_encode_img_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.img_img_decode.setText(QCoreApplication.translate("MainWindow", u"Img_img_decode", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Decode", None))
    # retranslateUi

