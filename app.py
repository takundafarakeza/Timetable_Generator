from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import Qt
from utils.generators import PrimarySchool
from utils import Types
from utils.logger_config import logger
import sys


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowFlags(Qt.WindowType.Tool | Qt.WindowType.FramelessWindowHint)


if __name__ == "__main__":
    app = QApplication()
    app.setStyle("Fusion")

    app_window = AppWindow()

    sys.exit(app.exec())
