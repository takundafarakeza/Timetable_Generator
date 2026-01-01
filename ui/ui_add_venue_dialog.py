# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_venue_dialogvmJhmB.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_AddVenue(object):
    def setupUi(self, AddVenue):
        if not AddVenue.objectName():
            AddVenue.setObjectName(u"AddVenue")
        AddVenue.resize(305, 351)
        AddVenue.setStyleSheet(u"* {\n"
"	background: transparent;\n"
"	border: none;\n"
"	color: #414141;\n"
"}\n"
"\n"
"QComboBox{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	outline: none;\n"
"	background: #FBFCFE;\n"
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
"	height: 24px;\n"
"	width: 24px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;"
                        "\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	border: 1px solid #D3D4D6;\n"
"	border-radius: 5px;\n"
"	padding-left: 5px;\n"
"	background: #FBFCFE;\n"
"}\n"
"\n"
"QWidget#main_container {\n"
"	background: #EBECEF;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #B1B1B1;\n"
"}\n"
"\n"
"QWidget#container {\n"
"	background: #F3F4F6;\n"
"}\n"
"\n"
"#close_btn:hover{\n"
"	background: #DC2626;\n"
"}\n"
"\n"
"#toolbar{\n"
"	border-bottom: 2px solid #E3E4E6;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(AddVenue)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddVenue)
        self.main_container.setObjectName(u"main_container")
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.toolbar = QWidget(self.main_container)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMaximumSize(QSize(16777215, 30))
        self.close_btn = QPushButton(self.toolbar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setGeometry(QRect(270, 0, 35, 30))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.close_btn.setIcon(icon)
        self.close_btn.setIconSize(QSize(10, 10))

        self.verticalLayout.addWidget(self.toolbar)

        self.container = QWidget(self.main_container)
        self.container.setObjectName(u"container")
        self.verticalLayout_3 = QVBoxLayout(self.container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.frame = QFrame(self.container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.venue_name = QLineEdit(self.frame)
        self.venue_name.setObjectName(u"venue_name")
        self.venue_name.setGeometry(QRect(30, 30, 241, 30))
        self.venue_name.setMinimumSize(QSize(0, 30))
        self.venue_save = QPushButton(self.frame)
        self.venue_save.setObjectName(u"venue_save")
        self.venue_save.setGeometry(QRect(190, 220, 81, 30))
        self.venue_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.venue_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.venue_latitude = QLineEdit(self.frame)
        self.venue_latitude.setObjectName(u"venue_latitude")
        self.venue_latitude.setGeometry(QRect(30, 80, 111, 30))
        self.venue_latitude.setMinimumSize(QSize(0, 30))
        self.venue_latitude.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.venue_longitude = QLineEdit(self.frame)
        self.venue_longitude.setObjectName(u"venue_longitude")
        self.venue_longitude.setGeometry(QRect(160, 80, 111, 30))
        self.venue_longitude.setMinimumSize(QSize(0, 30))
        self.venue_longitude.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.venue_location_description = QTextEdit(self.frame)
        self.venue_location_description.setObjectName(u"venue_location_description")
        self.venue_location_description.setGeometry(QRect(30, 130, 241, 61))

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddVenue)

        QMetaObject.connectSlotsByName(AddVenue)
    # setupUi

    def retranslateUi(self, AddVenue):
        AddVenue.setWindowTitle(QCoreApplication.translate("AddVenue", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddVenue", u"Venue", None))
        self.venue_name.setPlaceholderText(QCoreApplication.translate("AddVenue", u"Venue name", None))
        self.venue_save.setText(QCoreApplication.translate("AddVenue", u"Save", None))
        self.venue_latitude.setPlaceholderText(QCoreApplication.translate("AddVenue", u"Latitude", None))
        self.venue_longitude.setPlaceholderText(QCoreApplication.translate("AddVenue", u"Longitude", None))
        self.venue_location_description.setPlaceholderText(QCoreApplication.translate("AddVenue", u"Location description", None))
    # retranslateUi

