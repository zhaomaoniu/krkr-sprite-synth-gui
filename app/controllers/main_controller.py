from pathlib import Path
from typing import Optional
from krkr_sprite_synth import SpriteSynth
from PyQt6.QtWidgets import QComboBox, QLabel

from app.views.image_view import ImageViewer


class MainController:
    """主窗口控制器，处理UI事件和业务逻辑"""

    def __init__(self, view):
        self.view = view

        self.a_info_path = None
        self.b_info_path = None
        self.a_layers_info_path = None
        self.b_layers_info_path = None
        self.assets_path = None
        self.character_name = None

        self.dress_cb: Optional[QComboBox] = None
        self.face_cb: Optional[QComboBox] = None
        self.pose_cb: Optional[QComboBox] = None

        self.save_status: Optional[QLabel] = None

        self.image_viewer: Optional[ImageViewer] = None

        self.sprite_synth = None

    def _try_fill_combobox(self):
        """尝试填充下拉框"""
        if not (
            self.a_info_path is not None
            and self.a_layers_info_path is not None
            and self.assets_path is not None
        ):
            return

        self.sprite_synth = SpriteSynth(
            a_info_path=self.a_info_path,
            b_info_path=self.b_info_path,
            a_layers_info_path=self.a_layers_info_path,
            b_layers_info_path=self.b_layers_info_path,
            assets_path=self.assets_path,
            character_name=self.character_name,
        )

        dresses = sorted(
            list(
                {entry[0] for entry in self.sprite_synth.info_parser.a_dress.keys()}
                | {entry[0] for entry in self.sprite_synth.info_parser.b_dress.keys()}
            )
        )
        faces = sorted(
            list(
                {
                    entry.split("@")[0]
                    for entry in self.sprite_synth.info_parser.a_face.keys()
                }
                | {
                    entry.split("@")[0]
                    for entry in self.sprite_synth.info_parser.b_face.keys()
                }
            )
        )
        diffs = sorted(
            list(
                {entry[1] for entry in self.sprite_synth.info_parser.a_dress.keys()}
                | {entry[1] for entry in self.sprite_synth.info_parser.b_dress.keys()}
            )
        )

        self.dress_cb.clear()
        self.dress_cb.addItems(dresses)
        self.face_cb.clear()
        self.face_cb.addItems(faces)
        self.pose_cb.clear()
        self.pose_cb.addItems(diffs)

    def on_a_info_selected(self, path):
        """处理选择 A Info 文件事件"""
        self.a_info_path = path
        self._try_fill_combobox()

    def on_b_info_selected(self, path):
        """处理选择 B Info 文件事件"""
        self.b_info_path = path
        self._try_fill_combobox()

    def on_a_layers_info_selected(self, path):
        """处理选择 A Layer Info 文件事件"""
        self.a_layers_info_path = path
        self._try_fill_combobox()

    def on_b_layers_info_selected(self, path):
        """处理选择 B Layer Info 文件事件"""
        self.b_layers_info_path = path
        self._try_fill_combobox()

    def on_assets_selected(self, path):
        """处理选择 Assets 文件夹事件"""
        self.assets_path = path
        self._try_fill_combobox()

    def on_character_name_changed(self, name):
        """处理角色名称变更事件"""
        self.character_name = name
        self._try_fill_combobox()

    def on_dress_selected(self, _):
        """处理选择服装事件"""
        dress = self.dress_cb.currentText()
        face = self.face_cb.currentText()
        pose = self.pose_cb.currentText()

        if dress == "" or face == "" or pose == "":
            return

        result = self.sprite_synth.draw(dress=dress, face=face, pose=pose)
        self.image_viewer.set_image(result)

    def on_face_selected(self, _):
        """处理选择表情事件"""
        dress = self.dress_cb.currentText()
        face = self.face_cb.currentText()
        pose = self.pose_cb.currentText()

        if dress == "" or face == "" or pose == "":
            return

        result = self.sprite_synth.draw(dress=dress, face=face, pose=pose)
        self.image_viewer.set_image(result)

    def on_pose_selected(self, _):
        """处理选择姿势事件"""
        dress = self.dress_cb.currentText()
        face = self.face_cb.currentText()
        pose = self.pose_cb.currentText()

        if dress == "" or face == "" or pose == "":
            return

        result = self.sprite_synth.draw(dress=dress, face=face, pose=pose)
        self.image_viewer.set_image(result)

    def on_save_clicked(self):
        """处理保存事件"""
        if (
            self.sprite_synth is None
            or self.image_viewer is None
            or self.image_viewer.pixmap.isNull()
        ):
            self.save_status.setText("请先选择角色信息")
            return

        file_name = Path(self.sprite_synth.a_info_path).name
        character_name = file_name.split("a")[0]

        save_path = f"{character_name}_{self.dress_cb.currentText()}_{self.face_cb.currentText()}_{self.pose_cb.currentText()}.png"

        self.image_viewer.pixmap.save(save_path, "PNG")
        self.save_status.setText(f"保存成功：{save_path}")
