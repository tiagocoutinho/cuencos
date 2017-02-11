import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QWidget, QHBoxLayout, QLabel

_this_dir = os.path.dirname(__file__)


class CuencosGraphics(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.l = QHBoxLayout(self)
        self.l.setContentsMargins(0, 0, 0, 0)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.pixmap = QPixmap(os.path.join(_this_dir, 'images', 'frente_transparent.png'))
        self.scene.addPixmap(self.pixmap)

        self.l.addWidget(self.view)
