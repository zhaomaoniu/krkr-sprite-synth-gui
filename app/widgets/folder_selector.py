from pathlib import Path
from PyQt6.QtWidgets import (
    QLabel,
    QWidget,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
)
from PyQt6.QtCore import pyqtSignal


class FolderSelectorWidget(QWidget):
    folder_path_changed = pyqtSignal(Path)

    def __init__(self, title="文件夹选择示例", button_text="选择文件夹"):
        super().__init__()

        self.title = title
        self.button_text = button_text

        self.path = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.label = QLabel("未选择文件夹", self)

        self.btn = QPushButton(self.button_text, self)
        self.btn.clicked.connect(self.openFolderDialog)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def openFolderDialog(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, self.title, "", QFileDialog.Option.ShowDirsOnly
        )
        if folder_path:
            self.path = Path(folder_path)
            self.label.setText(self.path.name)
            self.folder_path_changed.emit(self.path)

    def get_folder_path(self):
        return self.path
