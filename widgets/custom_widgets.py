from PySide6.QtWidgets import (QFrame, QWidget, QHBoxLayout, QVBoxLayout,
                               QLabel, QPushButton, QComboBox, QCompleter,
                               QTableWidget, QCheckBox)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Signal, QSize, QRect, Qt
from functools import partial


class RemovableTableItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(u"container")
        self.setGeometry(QRect(50, 100, 280, 50))
        self.setMinimumSize(QSize(180, 50))
        self.setStyleSheet(u"*{"
                           "	border: none;"
                           "	background: transparent;"
                           "	color: #414141;"
                           "}"
                           "QWidget#container{"
                           "	border: 1px solid #D3D4D6;"
                           "	border-radius: 5px;"
                           "	background: #EBECEF;"
                           "}")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QLabel(self.frame)
        self.header.setObjectName(u"header")
        font = QFont()
        font.setBold(True)
        self.header.setFont(font)

        self.verticalLayout.addWidget(self.header)
        self.text = QLabel(self.frame)
        self.text.setObjectName(u"text")
        self.verticalLayout.addWidget(self.text)
        self.horizontalLayout.addWidget(self.frame)

        self.remove_btn = QPushButton(self)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setMinimumSize(QSize(40, 50))
        self.remove_btn.setMaximumSize(QSize(40, 50))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.remove_btn.setIcon(icon)
        self.remove_btn.setIconSize(QSize(10, 10))
        self.horizontalLayout.addWidget(self.remove_btn)

    def set_header(self, text: str):
        self.header.setText(text)

    def set_text(self, text: str):
        self.text.setText(text)


class ButtonFrame(QFrame):
    clicked = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, event, /):
        self.clicked.emit(self.objectName())
        super().mouseReleaseEvent(event)


class ButtonFrameSilent(QFrame):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mouseReleaseEvent(self, event, /):
        self.clicked.emit()
        super().mouseReleaseEvent(event)


class SearchableComboBox(QComboBox):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setEditable(True)

        completer = QCompleter(self.model(), self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        self.setCompleter(completer)

        self.lineEdit().textEdited.connect(completer.complete)


class DayCheckGroup(QTableWidget):
    def __init__(self):
        super().__init__(0, 1)

        self.setHorizontalHeaderLabels(["Available days"])
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.setShowGrid(False)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.parent_callback = None

        self.setColumnWidth(0, 240)

        self.setStyleSheet("""
                            QTableWidget {
                                border: none;
                            }
                            QHeaderView::section {
                                background-color: #EBECEF;
                                padding: 3px;
                                border: none;
                                font-weight: bold;
                            }

                            QHeaderView::section:horizontal {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QHeaderView::section:vertical {
                                border-right: 1px solid #D3D4D6;
                                border-bottom: 1px solid #D3D4D6;
                            }

                            QTableWidget::item {
                                border-bottom: 1px solid #E3E4E6;
                                padding: 3px;
                            }
                        """)
        self.verticalHeader().setVisible(False)
        self.days = {}

    def get_available_days(self):
        available = []
        for day in self.days:
            if self.days[day] == "available":
                available.append(day)
        return available

    def remove_add_day(self, day, checked):
        if checked == Qt.CheckState.Checked:
            self.days[day] = "available"
        else:
            self.days[day] = "unavailable"

    def add_item(self, day_id, day_name, available=True):
        row = self.rowCount()
        self.insertRow(row)
        self.setRowHeight(row, 30)

        day = QCheckBox(day_name)
        self.days[day_id] = "available" if available else "unavailable"
        day.setChecked(available)
        day.checkStateChanged.connect(partial(self.remove_add_day, day_id))
        self.setCellWidget(row, 0, day)
