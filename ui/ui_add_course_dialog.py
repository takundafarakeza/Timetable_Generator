# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_course_dialogIiNWYw.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_AddCourse(object):
    def setupUi(self, AddCourse):
        if not AddCourse.objectName():
            AddCourse.setObjectName(u"AddCourse")
        AddCourse.resize(305, 303)
        AddCourse.setStyleSheet(u"* {\n"
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
        self.verticalLayout_2 = QVBoxLayout(AddCourse)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_container = QWidget(AddCourse)
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
        self.close_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        self.course_name = QLineEdit(self.frame)
        self.course_name.setObjectName(u"course_name")
        self.course_name.setGeometry(QRect(30, 30, 241, 30))
        self.course_name.setMinimumSize(QSize(0, 30))
        self.course_save = QPushButton(self.frame)
        self.course_save.setObjectName(u"course_save")
        self.course_save.setGeometry(QRect(190, 170, 81, 30))
        self.course_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.course_save.setStyleSheet(u"padding: 5px;\n"
"background: #57954F;\n"
"color: #F3F4F6;\n"
"border-radius: 3px;")
        self.course_short_name = QLineEdit(self.frame)
        self.course_short_name.setObjectName(u"course_short_name")
        self.course_short_name.setGeometry(QRect(30, 90, 241, 30))
        self.course_short_name.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout.addWidget(self.container)


        self.verticalLayout_2.addWidget(self.main_container)


        self.retranslateUi(AddCourse)

        QMetaObject.connectSlotsByName(AddCourse)
    # setupUi

    def retranslateUi(self, AddCourse):
        AddCourse.setWindowTitle(QCoreApplication.translate("AddCourse", u"Dialog", None))
        self.close_btn.setText("")
        self.label.setText(QCoreApplication.translate("AddCourse", u"Course", None))
        self.course_name.setPlaceholderText(QCoreApplication.translate("AddCourse", u"Course name", None))
        self.course_save.setText(QCoreApplication.translate("AddCourse", u"Save", None))
        self.course_short_name.setPlaceholderText(QCoreApplication.translate("AddCourse", u"Course short name, e.g CS", None))
    # retranslateUi

