from pathlib import Path
from PyQt6.QtWidgets import (
    QLabel,
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
)
from PyQt6.QtCore import pyqtSignal


class FileSelectorWidget(QWidget):
    file_path_changed = pyqtSignal(Path)

    def __init__(
        self, title="文件选择示例", button_text="选择文件", file_types="所有文件 (*)"
    ):
        super().__init__()

        self.title = title
        self.button_text = button_text
        self.file_types = file_types

        self.path = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.label = QLabel("未选择文件", self)

        self.btn = QPushButton(self.button_text, self)
        self.btn.clicked.connect(self.openFileDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def openFileDialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.title, "", self.file_types
        )
        if file_path:
            self.path = Path(file_path)
            self.label.setText(self.path.name)
            self.file_path_changed.emit(self.path)

    def get_file_path(self):
        return self.path
