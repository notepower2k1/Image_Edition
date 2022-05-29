import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QRubberBand, QColorDialog, QMessageBox
from PyQt5.QtCore import Qt, QPoint, QRect, QObject, pyqtSignal, pyqtSlot, QEvent, QSize, Qt
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage, QIcon
from PIL import Image, ImageFont, ImageDraw, ImageQt, ImageColor, ImageFilter, ImageEnhance, ImageQt
import os

from regex import R

from ColorTransferWindow import Ui_ColorTransfer_Form
from EnhanceWindow import Ui_EnhanceForm
from FilterWindow import Ui_FilterDialog
from MainCloneWindow import Ui_MainWindow
from AddTextGUI import Ui_Form
from RotateWindow import Ui_Dialog
from HistoryWindow import Ui_HistoryDialog
from ResizeWindow import Ui_ResizeDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.x = 0
        self.y = 0
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
        self.actionHistory.triggered.connect(self.history)
        self.actionResize.triggered.connect(self.resizeImage)
        self.actionUndo.triggered.connect(self.undo)
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
        self.uic6 = Ui_HistoryDialog()
        self.Seventh_window = QtWidgets.QDialog()
        self.uic7 = Ui_ResizeDialog()
        self.Eighth_window = QtWidgets.QDialog()
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

        text = "x: 0,  y: 0"
        self.actionlabel.setText(text)

    # Crop Event
    def cropEvent1(self, eventQMouseEvent):
        if self.isCrop:
            if self.fname == '':
                pass
            else:
                # Create Crop Point Start
                self.originQPoint = eventQMouseEvent.pos()
                self.currentQRubberBand = QRubberBand(QRubberBand.Rectangle, self.imgScreen)
                self.currentQRubberBand.setGeometry(QRect(self.originQPoint, QSize()))
                self.currentQRubberBand.show()

    def cropEvent2(self, eventQMouseEvent):

        # Set some value postion
        text = "x: {0},  y: {1}".format(eventQMouseEvent.x(), eventQMouseEvent.y())
        self.actionlabel.setText(text)

        self.x = eventQMouseEvent.x()
        self.y = eventQMouseEvent.y()

        if self.Second_window.isVisible():
            self.uic1.txtX.setValue(self.x)
            self.uic1.txtY.setValue(self.y)

        if self.isCrop:
            if self.fname == '':
                pass
            else:
                # Expanded crop Rectangle with eventQmouse
                self.currentQRubberBand.setGeometry(QRect(self.originQPoint, eventQMouseEvent.pos()).normalized())

    def cropEvent3(self, eventQMouseEvent):
        if self.isCrop:
            if self.fname == '':
                pass
            else:
                # Crop Image With Rectangle
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
                self.listPixMap.append(pixmap)

    def closeEvent(self, event):
        answer = QtWidgets.QMessageBox.question(
            self,
            'Are you sure you want to quit ?',
            'Task is in progress !',
            QtWidgets.QMessageBox.Yes,
            QtWidgets.QMessageBox.No)
        if answer == QtWidgets.QMessageBox.Yes:
            event.accept()
            items = vars(self)
            # Closing all Dialog when close app
            self.runCloseDialogs()
            super().closeEvent(event)
        else:
            event.ignore()

    def showScreen(self):
        # Open file dialog
        if self.labelwidth == 0:
            self.labelwidth = self.imgScreen.width()
        if self.labelheigh == 0:
            self.labelheigh = self.imgScreen.height()
        self.imgScreen.setFixedSize(self.labelwidth, self.labelheigh)
        self.fname, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                    "All Files (*);;Image Files *.jpg; *.jpeg;")
        self.listPixMap.clear()
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
        if self.fname != '':
            self.runCloseDialogs()
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
            self.uic1.txtX.valueChanged.connect(self.check)
            self.uic1.txtY.valueChanged.connect(self.check)

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
        w = self.imgScreen.width()
        h = self.imgScreen.height()

        if self.uic1.btnCenter.isChecked():
            self.width_img = w / 2
            self.heigh_img = h / 2
        if self.uic1.btnT_L.isChecked():
            self.width_img = 0
            self.heigh_img = 0
        if self.uic1.btnT_R.isChecked():
            self.width_img = w - self.font_size * 2
            self.heigh_img = 0
        if self.uic1.btnB_L.isChecked():
            self.width_img = 0
            self.heigh_img = h - self.font_size * 2
        if self.uic1.btnB_R.isChecked():
            self.width_img = w - self.font_size * 2
            self.heigh_img = h - self.font_size * 2
        if self.uic1.btnOther.isChecked():
            self.width_img = self.uic1.txtX.value()
            self.heigh_img = self.uic1.txtY.value()
        else:
            pass

    def changefontSize(self):
        self.font_size = self.uic1.fontsizeSpinBox.value()

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
            self.listPixMap.clear()

    def enhanceEvent(self):
        if self.fname != '':
            self.runCloseDialogs()
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
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if file != '':
            if self.fname != '':
                if self.currentPixmap is None:
                    im = Image.open(self.fname)
                    im.save(f"{file}/photo.jpg")
                else:
                    im = ImageQt.fromqpixmap(self.currentPixmap)
                    im.save(f"{file}/photo.jpg")
        else:
            pass

    def colorTransfer(self):
        if self.fname != '':
            self.runCloseDialogs()
            self.Fourth_window = QtWidgets.QDialog()
            self.uic3.setupUi(self.Fourth_window)
            self.Fourth_window.show()

            self.uic3.pushButton.clicked.connect(self.eventColorTransfer)
            self.uic3.pushButton_2.clicked.connect(self.eventColorTransfer)
            self.uic3.pushButton_3.clicked.connect(self.eventColorTransfer)
            self.uic3.pushButton_4.clicked.connect(self.eventColorTransfer)
            self.uic3.pushButton_5.clicked.connect(self.eventColorTransfer)

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
        if self.fname != '':
            self.runCloseDialogs()
            self.Fifth_window = QtWidgets.QDialog()
            self.uic4.setupUi(self.Fifth_window)
            self.Fifth_window.show()

            self.uic4.pushButton.clicked.connect(self.flipEvent)
            self.uic4.pushButton_2.clicked.connect(self.flipEvent)
            self.uic4.pushButton_3.clicked.connect(self.rotateImage)

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

    def FilterEvent(self):
        if self.fname != '':
            self.runCloseDialogs()
            self.Sixth_window = QtWidgets.QDialog()
            self.uic5.setupUi(self.Sixth_window)
            self.Sixth_window.show()

            self.uic5.pushButton.clicked.connect(self.eventfilter)
            self.uic5.pushButton_2.clicked.connect(self.eventfilter)
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
        if self.fname != '':
            # Mở history dialog
            self.Seventh_window = QtWidgets.QDialog()
            self.uic6.setupUi(self.Seventh_window)
            self.Seventh_window.show()
            # Thêm các pixmap vào qlistwidget của history dialog
            for item in reversed(self.listPixMap):
                imageItem = QtWidgets.QListWidgetItem(QIcon(item), os.path.basename(self.fname))
                self.uic6.listWidget.addItem(imageItem)
            # Các event (apply, delete các pixmap trong history)
            self.uic6.pushButton.clicked.connect(self.deleteHistoryEvent)
            self.uic6.pushButton_2.clicked.connect(self.applyHistoryEvent)
            # event click chọn các pixmap trong qlistwidget
            self.uic6.listWidget.itemClicked.connect(self.historySelectionEvent)
            # Thêm apply event close cho qdialog history
            self.Seventh_window.closeEvent = self.historyCloseEvent

    def historyCloseEvent(self, event):
        if self.listPixMap:
            answer = QtWidgets.QMessageBox.question(
                self,
                'Notify! ',
                'Are you sure you want to apply this history ?',
                QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.Apply)
            if answer == QtWidgets.QMessageBox.Apply:
                super().closeEvent(event)
            else:
                self.imgScreen.setPixmap(self.listPixMap[-1])
                self.currentPixmap = self.listPixMap[-1]
                super().closeEvent(event)

    def applyHistoryEvent(self):
        if self.listPixMap:
            answer = QtWidgets.QMessageBox.question(
                self,
                'Notify!',
                'Are you sure you want to apply this history ?',
                QtWidgets.QMessageBox.No,
                QtWidgets.QMessageBox.Apply)
            if answer == QtWidgets.QMessageBox.Apply:
                # Đóng cửa sổ qdialog
                self.Seventh_window.accept()
            else:
                # Đóng cửa sổ qdialog và hoàn tác
                self.imgScreen.setPixmap(self.listPixMap[-1])
                self.currentPixmap = self.listPixMap[-1]
                self.Seventh_window.accept()
            pass
        else:
            self.Seventh_window.accept()

    def historySelectionEvent(self, item):
        # Lấy giá trị width height của ảnh default
        label_w = self.imgScreen.width()
        label_h = self.imgScreen.height()
        # Get icon (ảnh) của các pixmap
        icon = item.icon()
        # Set màn hình hiện tại bằng icon vừa get được
        self.imgScreen.setPixmap(icon.pixmap(icon.actualSize(QSize(label_w, label_h))))

    def deleteHistoryEvent(self):
        # Lấy giá trị default của ảnh và ảnh đang select trong qlistwidget
        label_w = self.imgScreen.width()
        label_h = self.imgScreen.height()
        defaultSize = QSize(label_w, label_h)
        listWidget = self.uic6.listWidget
        listItems = listWidget.selectedItems()

        # Không làm gì và tắt nếu list không có gì
        if not listItems: return

        # Xóa item trong qlistwidget và listpixmap hiện tại
        for item in listItems:
            listWidget.takeItem(listWidget.row(item))
            self.listPixMap.pop(listWidget.row(item))

        # Điều chỉnh ảnh đang show theo qlistwidget và listpixmap hiện tại
        if not listWidget:
            self.clearImage()
        else:
            icon = listWidget.item(0).icon()
            self.imgScreen.setPixmap(icon.pixmap(icon.actualSize(defaultSize)))

    def resizeImage(self):
        if self.fname != '':
            # Mở resize dialog
            self.runCloseDialogs()
            self.Eighth_window = QtWidgets.QDialog()
            self.uic7.setupUi(self.Eighth_window)
            self.Eighth_window.show()
            # Các event
            self.uic7.pushButton.clicked.connect(self.resizeImageEvent)

    def resizeImageEvent(self):
        # Điều chỉnh pixmap hiện tại theo scale lấy được từ 2 input width height
        pixmap = self.currentPixmap.scaled(self.uic7.sbWidth.value(), self.uic7.sbHeight.value(), Qt.KeepAspectRatio)
        self.imgScreen.setPixmap(pixmap)
        self.listPixMap.append(pixmap)

    def checkDialog(self):
        pass

    def undo(self):
        if self.fname != '':
            if len(self.listPixMap) <= 1:
                self.clearImage()
            else:
                pixmap = self.listPixMap[(self.listPixMap.index(self.currentPixmap)) - 1]
                self.listPixMap.pop()
                self.imgScreen.setPixmap(pixmap)
                self.currentPixmap = pixmap

    def runCloseDialogs(self):

        items = vars(self)

        for i in items:
            item = items[i]
            if isinstance(item, QtWidgets.QDialog) and item.isVisible():
                item.setVisible(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
