import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QRubberBand, QColorDialog, QMessageBox
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, pyqtSlot, QEvent, QSize
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage
from PIL import Image, ImageFont, ImageDraw, ImageQt, ImageColor, ImageFilter, ImageEnhance, ImageQt
import os

from ColorTransferWindow import Ui_ColorTransfer_Form
from EnhanceWindow import Ui_EnhanceForm
from FilterWindow import Ui_FilterDialog
from MainCloneWindow import Ui_MainWindow
from AddTextGUI import Ui_Form
from RotateWindow import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.currentQRubberBand = None
        self.originQPoint = None
        self.setupUi(self)
        # khai bao nut start
        self.actionOpen.triggered.connect(self.showScreen)
        self.actionSave_as.triggered.connect(self.saveImage)
        self.actionDraw_Text.triggered.connect(self.addText)
        self.actionEnhance.triggered.connect(self.enhanceEvent)
        self.actionClear.triggered.connect(self.clearImage)
        self.actionColor_Transforms.triggered.connect(self.colorTransfer)
        self.actionCrop.triggered.connect(self.testcrop)
        self.actionRotate.triggered.connect(self.rotateEvent)
        self.actionFilter.triggered.connect(self.FilterEvent)
        # self.clicked.connect(self.history)
        # self.uic.pushButton_4.clicked.connect(self.Open_SubScreen)
        self.fname = ''
        self.original_pixmap = None
        # Mo Man hinh phu
        self.uic1 = Ui_Form()
        self.Second_window = QtWidgets.QDialog()
        self.uic2 = Ui_EnhanceForm()
        self.Third_window = QtWidgets.QDialog()
        self.uic3 = Ui_ColorTransfer_Form()
        self.Fourth_window = QtWidgets.QDialog()
        self.uic4 = Ui_Dialog()
        self.Fifth_window = QtWidgets.QDialog()
        self.uic5 = Ui_FilterDialog()
        self.Sixth_window = QtWidgets.QDialog()
        # Set vi tri
        self.width_img = 0
        self.heigh_img = 0
        self.font_size = 18
        self.currentTextColor = (0, 0, 0)
        self.currentPixmap = None
        # crop
        self.isCrop = False
        self.imgScreen.mousePressEvent = self.cropEvent1
        self.imgScreen.mouseMoveEvent = self.cropEvent2
        self.imgScreen.mouseReleaseEvent = self.cropEvent3
        self.listPixMap = []

        self.labelwidth = 0
        self.labelheigh = 0

    def cropEvent1(self, eventQMouseEvent):
        if self.isCrop:
            if self.fname == '':
                pass
            else:
                self.originQPoint = eventQMouseEvent.pos()
                self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self.imgScreen)
                self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QSize()))
                self.currentQRubberBand.show()

    def cropEvent2(self, eventQMouseEvent):
        text = "x: {0},  y: {1}".format(eventQMouseEvent.x(), eventQMouseEvent.y())
        self.actionlabel.setText(text)

        if self.isCrop:
            if self.fname == '':
                pass
            else:
                self.currentQRubberBand.setGeometry(QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def cropEvent3(self, eventQMouseEvent):
        if self.isCrop:
            if self.fname == '':
                pass
            else:
                self.currentQRubberBand.hide()
                currentQRect = self.currentQRubberBand.geometry()
                self.currentQRubberBand.deleteLater()
                cropQPixmap = self.imgScreen.pixmap().copy(currentQRect)

                myImage = ImageQt.fromqpixmap(cropQPixmap)

                im = myImage.convert("RGBA")
                pixmap = ImageQt.toqpixmap(im)
                self.imgScreen.setPixmap(pixmap)
                self.currentPixmap = pixmap
                self.isCrop = False

    def closeEvent(self, event):
        answer = QtWidgets.QMessageBox.question(
            self,
            'Are you sure you want to quit ?',
            'Task is in progress !',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        super().closeEvent(event)

    def showScreen(self):
        # Open file dialog
        if self.labelwidth == 0:
            self.labelwidth = self.imgScreen.width()
        if self.labelheigh == 0:
            self.labelheigh = self.imgScreen.height()
        self.imgScreen.setFixedSize(self.labelwidth, self.labelheigh)
        self.fname, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                    "All Files (*);;Image Files *.jpg; *.jpeg;")

        # Hien thi anh trong label
        if self.fname != '':
            image = Image.open(self.fname)
            im = image.convert("RGBA")

            # Kiem tra size cua label va anh
            label_w = self.imgScreen.width()
            label_h = self.imgScreen.height()
            if im.width >= label_w or im.height >= label_h:
                im = im.resize((label_w, label_h))
            else:
                pass
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.imgScreen.setFixedSize(im.width, im.height)
            self.original_pixmap = pixmap
            self.currentPixmap = pixmap
        else:
            pass

    def handleButton(self):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.ShiftModifier:
            print('Shift+Click')
        elif modifiers == Qt.ControlModifier:
            print('Ctrl+Click')
        elif modifiers == (Qt.ShiftModifier | Qt.ControlModifier):
            print('Ctrl+Shift+Click')
        else:
            print('Mouse Click')

    def addText(self):
        # Mo cua so Add Text
        self.Second_window = QtWidgets.QDialog()
        self.uic1.setupUi(self.Second_window)
        self.Second_window.show()

        # Event click cua so color picker
        self.uic1.displayColorWidget.mouseReleaseEvent = lambda event: self.addColor()

        self.uic1.drawBtn.clicked.connect(self.drawText)
        self.uic1.textEdit.textChanged.connect(self.changeColor)
        # Kiem tra radio button
        self.uic1.btnCenter.clicked.connect(self.check)
        self.uic1.btnT_L.clicked.connect(self.check)
        self.uic1.btnT_R.clicked.connect(self.check)
        self.uic1.btnB_L.clicked.connect(self.check)
        self.uic1.btnB_R.clicked.connect(self.check)
        self.uic1.btnOther.clicked.connect(self.check)
        self.uic1.fontsizeSpinBox.valueChanged.connect(self.changefontSize)
        self.uic1.txtX.valueChanged.connect(self.changePositionOther)
        self.uic1.txtY.valueChanged.connect(self.changePositionOther)
        self.uic1.btnUndo.clicked.connect(self.clearImage)

        if self.fname != '':
            myImage = Image.open(str(self.fname))

            self.uic1.max_X.setText("Max X: " + str(myImage.width))
            self.uic1.max_Y.setText("Max Y: " + str(myImage.height))

    def drawText(self):
        myText = self.uic1.textEdit.toPlainText()

        if self.fname != '':
            if self.currentPixmap is None:
                myImage = Image.open(str(self.fname))
            else:
                myImage = ImageQt.fromqpixmap(self.currentPixmap)

            textFont = ImageFont.truetype("arial.ttf", self.font_size)
            editImage = ImageDraw.Draw(myImage)
            editImage.text((self.width_img, self.heigh_img), myText, str('#%02x%02x%02x' % self.currentTextColor),
                           align='center',
                           font=textFont)
            im = myImage.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def addColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            red = color.getRgb()[0]
            green = color.getRgb()[1]
            blue = color.getRgb()[2]
            self.uic1.RedSlide.setValue(int(red))
            self.uic1.BlueSlide.setValue(int(blue))
            self.uic1.GreenSlide.setValue(int(green))
            self.uic1.displayColorWidget.setStyleSheet(f"background-color:rgb({red},{green},{blue});")
            self.currentTextColor = (red, green, blue)
            self.changeColor()

    def changeColor(self):

        red = list(self.currentTextColor)[0]
        green = list(self.currentTextColor)[1]
        blue = list(self.currentTextColor)[2]

        self.uic1.textEdit.setTextColor(QColor(red, green, blue))

    def check(self):
        image = Image.open(self.fname)

        w = 0
        h = 0
        if self.uic1.btnCenter.isChecked():
            w = image.width / 2
            h = image.height / 2
        elif self.uic1.btnT_L.isChecked():
            w = 0
            h = 0
        elif self.uic1.btnT_R.isChecked():
            w = image.width - self.font_size * 2
            h = 0
        elif self.uic1.btnB_L.isChecked():
            w = 0
            h = image.height - self.font_size * 2
        elif self.uic1.btnB_R.isChecked():
            w = image.width - self.font_size * 2
            h = image.height - self.font_size * 2
        elif self.uic1.btnOther.isChecked():
            pass

        self.width_img = w
        self.heigh_img = h

        # changing text of label

    def changefontSize(self):
        self.font_size = self.uic1.fontsizeSpinBox.value()

    def changePositionOther(self):
        self.width_img = self.uic1.txtX.value()
        self.heigh_img = self.uic1.txtY.value()

    def clearImage(self):
        if self.original_pixmap:
            image = Image.open(self.fname)
            im = image.convert("RGBA")

            # Kiem tra size cua label va anh
            label_w = self.imgScreen.width()
            label_h = self.imgScreen.height()
            if im.width >= label_w or im.height >= label_h:
                im = im.resize((label_w, label_h))
            else:
                pass

            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap

    def enhanceEvent(self):
        self.Third_window = QtWidgets.QDialog()
        self.uic2.setupUi(self.Third_window)
        self.Third_window.show()

        self.uic2.brightnessSlide.sliderReleased.connect(self.brightnessChange)
        self.uic2.sharpnessSlide.sliderReleased.connect(self.sharpnessChange)
        self.uic2.colorSlide.sliderReleased.connect(self.colorChange)
        self.uic2.contrastSlide.sliderReleased.connect(self.contrastChange)

    def brightnessChange(self):
        value = self.uic2.brightnessSlide.value() / 10
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Brightness(im).enhance(value)
            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def sharpnessChange(self):
        value = self.uic2.sharpnessSlide.value() / 10
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Sharpness(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)

            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def colorChange(self):
        value = self.uic2.colorSlide.value() / 10
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Color(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def contrastChange(self):
        value = self.uic2.contrastSlide.value() / 10
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Contrast(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)

            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def saveImage(self):
        if self.fname:
            image_path = "/image"
            if os.path.exists(image_path):
                ImageName = self.fname.split("/")
                myImage = Image.open(str(self.fname))
                myImage.save(f"{image_path}/" + ImageName[-1], 'JPEG')
            else:
                os.mkdir(image_path)

    def colorTransfer(self):
        self.Fourth_window = QtWidgets.QDialog()
        self.uic3.setupUi(self.Fourth_window)
        self.Fourth_window.show()

        self.uic3.pushButton.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_2.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_3.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_4.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_5.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_6.clicked.connect(self.eventColorTransfer)

    def eventColorTransfer(self):
        if self.fname != '':
            if self.currentPixmap is None:
                myImage = Image.open(str(self.fname))
            else:
                myImage = ImageQt.fromqpixmap(self.currentPixmap)

            btn = self.Fourth_window.sender()
            red, green, blue = myImage.split()
            temp_image = None

            if btn == self.uic3.pushButton:
                temp_image = Image.merge("RGB", (green, red, blue))
            elif btn == self.uic3.pushButton_2:
                temp_image = Image.merge("RGB", (green, blue, red))
            elif btn == self.uic3.pushButton_3:
                temp_image = Image.merge("RGB", (blue, green, red))
            elif btn == self.uic3.pushButton_4:
                temp_image = Image.merge("RGB", (red, blue, green))
            elif btn == self.uic3.pushButton_5:
                temp_image = Image.merge("RGB", (blue, red, green))
            elif btn == self.uic3.pushButton_6:
                self.clearImage()
            else:
                pass

            if temp_image is not None:
                im = temp_image.convert("RGBA")
                pixmap = ImageQt.toqpixmap(im)
                self.imgScreen.setPixmap(pixmap)
                self.currentPixmap = pixmap
                self.listPixMap.append(pixmap)
            else:
                pass

    def testcrop(self):
        self.isCrop = True

    def rotateEvent(self):
        self.Fifth_window = QtWidgets.QDialog()
        self.uic4.setupUi(self.Fifth_window)
        self.Fifth_window.show()

        self.uic4.pushButton.clicked.connect(self.flipEvent)
        self.uic4.pushButton_2.clicked.connect(self.flipEvent)
        self.uic4.pushButton_3.clicked.connect(self.rotateImage)
        self.uic4.pushButton_4.clicked.connect(self.clearImage)

    def flipEvent(self):
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            btn = self.Fifth_window.sender()
            image_flip = None
            if btn == self.uic4.pushButton:
                image_flip = im.transpose(Image.FLIP_TOP_BOTTOM)
            elif btn == self.uic4.pushButton_2:
                image_flip = im.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                pass

            im = image_flip.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
        else:
            pass

    def rotateImage(self):
        value = self.uic4.spinBox.value()
        if self.fname != '':
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            image_rotate = im.rotate(value, expand=True)
            im = image_rotate.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.imgScreen.setPixmap(pixmap)
            self.currentPixmap = pixmap
            self.listPixMap.append(pixmap)
            self.uic4.spinBox.setValue(0)

    def undoRotate(self):
        pass

    def FilterEvent(self):
        self.Sixth_window = QtWidgets.QDialog()
        self.uic5.setupUi(self.Sixth_window)
        self.Sixth_window.show()

        self.uic5.pushButton.clicked.connect(self.eventfilter)
        self.uic5.pushButton_2.clicked.connect(self.eventfilter)
        self.uic5.pushButton_3.clicked.connect(self.eventfilter)
        self.uic5.pushButton_4.clicked.connect(self.eventfilter)
        self.uic5.pushButton_5.clicked.connect(self.eventfilter)
        self.uic5.pushButton_7.clicked.connect(self.eventfilter)
        self.uic5.pushButton_8.clicked.connect(self.eventfilter)

    def eventfilter(self):
        if self.fname != '':
            if self.currentPixmap is None:
                myImage = Image.open(str(self.fname))
            else:
                myImage = ImageQt.fromqpixmap(self.currentPixmap)

            btn = self.Fourth_window.sender()
            temp_image = None

            if btn == self.uic5.pushButton:
                temp_image = myImage.filter(ImageFilter.BLUR)
            elif btn == self.uic5.pushButton_2:
                temp_image = myImage.filter(ImageFilter.CONTOUR)
            elif btn == self.uic5.pushButton_4:
                temp_image = myImage.filter(ImageFilter.EDGE_ENHANCE)
            elif btn == self.uic5.pushButton_5:
                temp_image = myImage.filter(ImageFilter.DETAIL)
            elif btn == self.uic5.pushButton_7:
                temp_image = myImage.filter(ImageFilter.SHARPEN)
            elif btn == self.uic5.pushButton_8:
                temp_image = myImage.filter(ImageFilter.SMOOTH)
            else:
                pass

            if temp_image is not None:
                im = temp_image.convert("RGBA")
                pixmap = ImageQt.toqpixmap(im)
                self.imgScreen.setPixmap(pixmap)
                self.currentPixmap = pixmap
                self.listPixMap.append(pixmap)
            else:
                pass

    def history(self):
        for item in self.listPixMap:
            print(item)

    def checkDialog(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
