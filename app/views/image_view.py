from PIL import Image
from typing import Optional
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QGraphicsPixmapItem,
)
from PyQt6.QtGui import QPainter

from app.utils import pil_to_qpixmap


class ImageViewer(QGraphicsView):
    def __init__(self, image: Optional[Image.Image] = None):
        super().__init__()

        # 读取图片
        self.pixmap = pil_to_qpixmap(image or Image.new("RGBA", (1, 1), (0, 0, 0, 0)))

        # 创建场景
        self.scene = QGraphicsScene(self)
        self.item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.item)

        self.setScene(self.scene)
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

    def set_image(self, image: Image.Image):
        """设置新的图片"""
        self.pixmap = pil_to_qpixmap(image)
        self.item.setPixmap(self.pixmap)

    def resizeEvent(self, _):
        """窗口大小调整时，自动缩放图片"""
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
