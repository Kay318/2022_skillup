from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
from PIL import Image
import sys
import time
import os

class ImageViewer(QWidget):
    def __init__(self, img_dir):
        super().__init__()
        pixmap = QPixmap(img_dir)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ImageViewer()
    ui.show()
    sys.exit(app.exec_())