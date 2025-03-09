from PIL import Image
from PyQt6.QtGui import QPixmap, QImage


def pil_to_qpixmap(pil_image: Image.Image) -> QPixmap:
    """将 PIL.Image 转换为 QPixmap"""
    pil_image = pil_image.convert("RGBA")  # 确保图像格式正确
    data = pil_image.tobytes("raw", "RGBA")
    qimage = QImage(
        data, pil_image.width, pil_image.height, QImage.Format.Format_RGBA8888
    )
    return QPixmap.fromImage(qimage)
