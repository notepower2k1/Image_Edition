import sys

from PIL import Image, ImageQt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QApplication
from PyQt5 import QtGui

class ImageViewer(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("PyQt Image Viewer")

        # Open up image in Pillow
        image = Image.open("newImage.jpg")
        QtImage1 = ImageQt.ImageQt(image)
        QtImage2 = QtGui.QImage(QtImage1)
        pixmap = QtGui.QPixmap.fromImage(QtImage2)
        self.image_label = QLabel('')
        self.image_label.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    app.exec_()