# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewerxQpaeX.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_ViewerWindow(object):
    def setupUi(self, ViewerWindow):
        if not ViewerWindow.objectName():
            ViewerWindow.setObjectName(u"ViewerWindow")
        ViewerWindow.resize(968, 550)
        ViewerWindow.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #414141;\n"
"}\n"
"\n"
"QPushButton#close_btn{\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#minimize_btn{\n"
"	border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#close_btn:hover{\n"
"	background: #D62626;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	background: #FBFCFE;\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#main_container{\n"
"	background: #EBECEF;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #B1B1B1;\n"
"}\n"
"\n"
"QWidget#menu_container{\n"
"	background: #EBECEF;\n"
"	border-right: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QFrame#footer{\n"
"	background: #EBECEF;\n"
"	border-top: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QWidget#container{\n"
"	background: #F3F4F6;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QWidget#toolbar{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-"
                        "left: 5px;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QPushButton#current_project {\n"
"	border: 1px solid #D3D4D6;\n"
"	background: #F3F4F6;\n"
"	padding-left:5px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#search_container {\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#recent_status_txt{\n"
"	color: #818181;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background: #DBEAFE;\n"
"}\n"
"\n"
"QToolTip{\n"
"	background: #F3F4F6;\n"
"	border: 1px solid #E3E4E6;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"	border: none;\n"
"	background: #EBECEF;\n"
"	height: 8px;\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"	background: #B1B1B1;\n"
"	min-width: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"	background-color: #EBECEF;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	border: none;\n"
"	background: #EBECEF;\n"
"	width: 8px"
                        ";\n"
"	margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background: #B1B1B1;\n"
"	min-height: 10px;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"	background-color: #EBECEF;\n"
"}\n"
"\n"
"QToolButton::menu-indicator{\n"
"	image: none;\n"
"	width: 0px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"	image: url(':/icons/icons/drop_down.svg');\n"
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QSpinBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QSpinBox:down-button{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QSpinBox:up-button{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QSpinBox:down-arrow{\n"
"	image: url(':/icons/icons/drop_down.svg');\n"
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QSpinBox:up-arrow{\n"
"	image: url(':/icons/icons/drop_up.svg');\n"
"	height: "
                        "24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"                            QTableWidget {\n"
"                                border: none;\n"
"                            }\n"
"                            QHeaderView::section {\n"
"                                background-color: #EBECEF;\n"
"                                padding: 3px;\n"
"                                border: none;\n"
"                                font-weight: bold;\n"
"                            }\n"
"                            \n"
"                            QHeaderView::section:horizontal {\n"
"                                border-right: 1px solid #D3D4D6;\n"
"                                border-bottom: 1px solid #D3D4D6;\n"
"                            }\n"
"                            \n"
"                            QHeaderView::section:vertical {\n"
"                                border-right: 1px solid #D3D4D6;\n"
"                                border-bottom: 1px solid #D3D4D6;\n"
"                            }\n"
"      "
                        "                      \n"
"                            QTableWidget::item {\n"
"                                border-bottom: 1px solid #E3E4E6;\n"
"                                padding: 3px;\n"
"                            }")
        self.verticalLayout = QVBoxLayout(ViewerWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(ViewerWindow)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout_2 = QVBoxLayout(self.main_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QWidget(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMinimumSize(QSize(0, 30))
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout = QHBoxLayout(self.toolbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_icon = QPushButton(self.toolbar)
        self.window_icon.setObjectName(u"window_icon")
        self.window_icon.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.window_icon.setIcon(icon)
        self.window_icon.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.window_icon)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.toolbar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.filter = QComboBox(self.frame)
        self.filter.setObjectName(u"filter")
        self.filter.setGeometry(QRect(8, 5, 181, 22))

        self.horizontalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(self.toolbar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(120, 0))
        self.frame_3.setMaximumSize(QSize(120, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.close_btn = QPushButton(self.frame_3)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(80, 0, 40, 30))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon1)
        self.close_btn.setIconSize(QSize(10, 10))
        self.minimize_btn = QPushButton(self.frame_3)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setGeometry(QRect(0, 0, 40, 30))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.minimize_btn.setIcon(icon2)
        self.maximize_btn = QPushButton(self.frame_3)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setGeometry(QRect(40, 0, 40, 30))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStop))
        self.maximize_btn.setIcon(icon3)
        self.maximize_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.toolbar)

        self.container = QWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tab_view = QTabWidget(self.container)
        self.tab_view.setObjectName(u"tab_view")

        self.horizontalLayout_2.addWidget(self.tab_view)


        self.verticalLayout_2.addWidget(self.container)


        self.verticalLayout.addWidget(self.main_container)


        self.retranslateUi(ViewerWindow)

        self.filter.setCurrentIndex(-1)
        self.tab_view.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ViewerWindow)
    # setupUi

    def retranslateUi(self, ViewerWindow):
        ViewerWindow.setWindowTitle(QCoreApplication.translate("ViewerWindow", u"Form", None))
        self.window_icon.setText("")
        self.filter.setCurrentText("")
        self.filter.setPlaceholderText("")
        self.close_btn.setText("")
        self.minimize_btn.setText("")
        self.maximize_btn.setText("")
    # retranslateUi

