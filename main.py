import sys
from PyQt6.QtWidgets import QApplication
from app.views.main_window import MainWindow


def main():
    """应用程序主入口"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
