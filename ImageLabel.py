from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QRubberBand
import os


class QImageLabel(QLabel):
    def __init__(self, parentQWidget=None):
        super(QImageLabel, self).__init__(parentQWidget)
        self.currentQRubberBand = None
        self.originQPoint = None
        self.initUI()

    def initUI(self):
        self.setPixmap(QPixmap(''))
        if os.path.exists('cropImage.png'):
            os.remove("cropImage.png")
        else:
            pass
    def mousePressEvent(self, eventQMouseEvent):
        if not self.pixmap().isNull():
            self.originQPoint = eventQMouseEvent.pos()
            self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self)
            self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, QtCore.QSize()))
            self.currentQRubberBand.show()

    def mouseMoveEvent(self, eventQMouseEvent):
        if not self.pixmap().isNull():
            self.currentQRubberBand.setGeometry(QtCore.QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def mouseReleaseEvent(self, eventQMouseEvent):
        if not self.pixmap().isNull():
            self.currentQRubberBand.hide()
            currentQRect = self.currentQRubberBand.geometry()
            self.currentQRubberBand.deleteLater()
            cropQPixmap = self.pixmap().copy(currentQRect)
            cropQPixmap.save('cropImage.png')

