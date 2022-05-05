import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QSpinBox, QColorDialog, QMessageBox
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PIL import Image, ImageFont, ImageDraw, ImageQt, ImageColor, ImageFilter, ImageEnhance, ImageQt
import os

from ColorTransferWindow import Ui_ColorTransfer_Form
from EnhanceWindow import Ui_EnhanceForm
from MainWindow import Ui_MainWindow
from AddTextGUI import Ui_Form
from ImageLabel import QImageLabel


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut start
        self.uic.openBtn.clicked.connect(self.showScreen)
        self.uic.pushButton_2.clicked.connect(self.saveImage)
        self.uic.pushButton_3.clicked.connect(self.addText)
        self.uic.pushButton_4.clicked.connect(self.enhanceEvent)
        self.uic.pushButton_5.clicked.connect(self.clearImage)
        self.uic.pushButton.clicked.connect(self.colorTransfer)
        self.uic.pushButton_6.clicked.connect(self.testcrop)
        # self.uic.pushButton_4.clicked.connect(self.Open_SubScreen)
        self.fname = ''
        self.original_image = ''
        # Mo Man hinh phu
        self.uic1 = Ui_Form()
        self.Second_window = QtWidgets.QMainWindow()
        self.uic2 = Ui_EnhanceForm()
        self.Third_window = QtWidgets.QMainWindow()
        self.uic3 = Ui_ColorTransfer_Form()
        self.Fourth_window = QtWidgets.QMainWindow()
        # Set vi tri
        self.width_img = 0
        self.heigh_img = 0
        self.font_size = 18
        self.currentTextColor = (0, 0, 0)
        self.currentPixmap = None
        # crop
        self.isCrop = False

    def showScreen(self):
        # Open file dialog
        self.fname, _ = QFileDialog.getOpenFileName(self.main_win, "Open File", "",
                                                    "All Files (*);;Image Files *.jpg; *.jpeg;")

        # Hien thi anh trong label
        if self.fname:
            image = Image.open(self.fname)
            im = image.convert("RGBA")

            # Kiem tra size cua label va anh
            label_w = self.uic.imgScreen.width()
            label_h = self.uic.imgScreen.height()
            if im.width >= label_w or im.height >= label_h:
                im = im.resize((label_w, label_h))
            else:
                pass

            pixmap = ImageQt.toqpixmap(im)
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.original_image = self.fname
            self.currentPixmap = pixmap
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
        self.Second_window = QtWidgets.QMainWindow()
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

        if self.fname:
            myImage = Image.open(str(self.fname))

            self.uic1.max_X.setText("Max X: " + str(myImage.width))
            self.uic1.max_Y.setText("Max Y: " + str(myImage.height))

    def drawText(self):
        myText = self.uic1.textEdit.toPlainText()

        if self.fname:
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
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap
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
        if self.original_image:
            image = Image.open(self.fname)
            im = image.convert("RGBA")

            # Kiem tra size cua label va anh
            label_w = self.uic.imgScreen.width()
            label_h = self.uic.imgScreen.height()
            if im.width >= label_w or im.height >= label_h:
                im = im.resize((label_w, label_h))
            else:
                pass

            pixmap = ImageQt.toqpixmap(im)
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap

    def enhanceEvent(self):
        self.Third_window = QtWidgets.QMainWindow()
        self.uic2.setupUi(self.Third_window)
        self.Third_window.show()

        self.uic2.brightnessSlide.sliderReleased.connect(self.brightnessChange)
        self.uic2.sharpnessSlide.sliderReleased.connect(self.sharpnessChange)
        self.uic2.colorSlide.sliderReleased.connect(self.colorChange)
        self.uic2.contrastSlide.sliderReleased.connect(self.contrastChange)

    def brightnessChange(self):
        value = self.uic2.brightnessSlide.value() / 10
        if self.fname:
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Brightness(im).enhance(value)
            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap
        else:
            pass

    def sharpnessChange(self):
        value = self.uic2.sharpnessSlide.value() / 10
        if self.fname:
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Sharpness(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)

            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap
        else:
            pass

    def colorChange(self):
        value = self.uic2.colorSlide.value() / 10
        if self.fname:
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Color(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap
        else:
            pass

    def contrastChange(self):
        value = self.uic2.contrastSlide.value() / 10
        if self.fname:
            if self.currentPixmap is None:
                im = Image.open(self.fname)
            else:
                im = ImageQt.fromqpixmap(self.currentPixmap)

            enhanced = ImageEnhance.Contrast(im).enhance(value)

            im = enhanced.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)

            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
            self.currentPixmap = pixmap
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
        self.Fourth_window = QtWidgets.QMainWindow()
        self.uic3.setupUi(self.Fourth_window)
        self.Fourth_window.show()

        self.uic3.pushButton.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_2.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_3.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_4.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_5.clicked.connect(self.eventColorTransfer)
        self.uic3.pushButton_6.clicked.connect(self.eventColorTransfer)

    def eventColorTransfer(self):
        if self.fname:
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
                self.uic.imgScreen.setPixmap(pixmap)
                self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())
                self.currentPixmap = pixmap
            else:
                pass

    def testcrop(self):
        if os.path.exists('cropImage.png'):
            image = Image.open('cropImage.png')
            im = image.convert("RGBA")
            pixmap = ImageQt.toqpixmap(im)
            self.uic.imgScreen.setPixmap(pixmap)
            self.uic.imgScreen.setFixedSize(self.uic.imgScreen.width(), self.uic.imgScreen.height())

        else:
            QMessageBox.about(self.uic.centralwidget, "Error", "No Crop Image yet!!!")

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
