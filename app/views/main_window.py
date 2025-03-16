from PyQt6.QtWidgets import (
    QLabel,
    QWidget,
    QLineEdit,
    QComboBox,
    QPushButton,
    QMainWindow,
    QGridLayout,
)

from app.views.image_view import ImageViewer
from app.controllers.main_controller import MainController
from app.widgets import FolderSelectorWidget, FileSelectorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = MainController(self)
        self.init_ui()

    def init_ui(self):
        """初始化UI界面"""

        self.setWindowTitle("Kirikiri Sprite Synth")
        self.setGeometry(100, 50, 1280, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        label_a_info = QLabel("A Info")
        selector_a_info = FileSelectorWidget(
            title="选择 A Info 文件",
            file_types="所有文件 (*);;文本文件 (*.txt);;SINFO 文件 (*.sinfo)",
        )
        label_a_info.setFixedSize(100, 30)
        selector_a_info.setFixedSize(200, 70)
        selector_a_info.file_path_changed.connect(self.controller.on_a_info_selected)
        label_b_info = QLabel("B Info")
        selector_b_info = FileSelectorWidget(
            title="选择 B Info 文件",
            file_types="所有文件 (*);;文本文件 (*.txt);;SINFO 文件 (*.sinfo)",
        )
        label_b_info.setFixedSize(100, 30)
        selector_b_info.setFixedSize(200, 70)
        selector_b_info.file_path_changed.connect(self.controller.on_b_info_selected)
        label_a_layer = QLabel("A Layer Info")
        folder_selector_a = FileSelectorWidget(
            title="选择 A Layer Info 文件", file_types="所有文件 (*);;文本文件 (*.txt)"
        )
        label_a_layer.setFixedSize(100, 30)
        folder_selector_a.setFixedSize(200, 70)
        folder_selector_a.file_path_changed.connect(
            self.controller.on_a_layers_info_selected
        )
        label_b_layer = QLabel("B Layer Info")
        folder_selector_b = FileSelectorWidget(
            title="选择 B Layer Info 文件", file_types="所有文件 (*);;文本文件 (*.txt)"
        )
        folder_selector_b.file_path_changed.connect(
            self.controller.on_b_layers_info_selected
        )
        label_b_layer.setFixedSize(100, 30)
        folder_selector_b.setFixedSize(200, 70)
        label_assets = QLabel("Assets")
        selector_assets = FolderSelectorWidget(title="选择 Assets 文件夹")
        selector_assets.folder_path_changed.connect(self.controller.on_assets_selected)
        label_assets.setFixedSize(100, 30)
        selector_assets.setFixedSize(200, 70)
        label_character = QLabel("Character")
        line_edit_character = QLineEdit()
        line_edit_character.textChanged.connect(
            self.controller.on_character_name_changed
        )
        label_character.setFixedSize(100, 30)
        line_edit_character.setFixedSize(200, 30)

        label_dress = QLabel("Dress")
        combo_box_dress = QComboBox()
        combo_box_dress.currentIndexChanged.connect(self.controller.on_dress_selected)
        label_face = QLabel("Face")
        combo_box_face = QComboBox()
        combo_box_face.currentIndexChanged.connect(self.controller.on_face_selected)
        label_pose = QLabel("Pose")
        combo_box_pose = QComboBox()
        combo_box_pose.currentIndexChanged.connect(self.controller.on_pose_selected)
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.controller.on_save_clicked)
        save_status = QLabel("")
        save_status.setFixedSize(200, 30)

        self.controller.dress_cb = combo_box_dress
        self.controller.face_cb = combo_box_face
        self.controller.pose_cb = combo_box_pose

        self.controller.save_status = save_status

        image_viewer = ImageViewer()
        self.controller.image_viewer = image_viewer

        layout.addWidget(label_a_info, 0, 0)
        layout.addWidget(selector_a_info, 0, 1)
        layout.addWidget(label_b_info, 1, 0)
        layout.addWidget(selector_b_info, 1, 1)
        layout.addWidget(label_a_layer, 2, 0)
        layout.addWidget(folder_selector_a, 2, 1)
        layout.addWidget(label_b_layer, 3, 0)
        layout.addWidget(folder_selector_b, 3, 1)
        layout.addWidget(label_assets, 4, 0)
        layout.addWidget(selector_assets, 4, 1)
        layout.addWidget(label_character, 5, 0)
        layout.addWidget(line_edit_character, 5, 1)
        layout.addWidget(label_dress, 6, 0)
        layout.addWidget(combo_box_dress, 6, 1)
        layout.addWidget(label_face, 7, 0)
        layout.addWidget(combo_box_face, 7, 1)
        layout.addWidget(label_pose, 8, 0)
        layout.addWidget(combo_box_pose, 8, 1)
        layout.addWidget(save_button, 9, 0)
        layout.addWidget(save_status, 9, 1)
        layout.addWidget(image_viewer, 0, 2, 10, 1)
