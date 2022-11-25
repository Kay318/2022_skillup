from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class ImageViewer(QWidget):
    def __init__(self, img_dir):
        super().__init__()
        screen = QDesktopWidget().screenGeometry()        
        pixmap = QPixmap(img_dir)
        label = QLabel()
        label.setPixmap(pixmap)
        label.setScaledContents(True)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        if pixmap.width() <= screen.width() and pixmap.height() <= screen.height():
            self.move(round((screen.width()-pixmap.width())/2), round((screen.height()-pixmap.height())/2))
        elif pixmap.width() >= screen.width() and pixmap.height() <= screen.height():
            self.move(0, round((screen.height()-pixmap.height())/2))
        elif pixmap.width() <= screen.width() and pixmap.height() >= screen.height():
            self.move(round((screen.width()-pixmap.width())/2), 0)
        else:
            self.move(0,0)
        self.setLayout(vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = ImageViewer()
    ui.show()
    sys.exit(app.exec_())