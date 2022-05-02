# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(410, 499)
        Form.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint,False)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 371, 31))
        self.textEdit.setObjectName("textEdit")
        self.drawBtn = QtWidgets.QPushButton(Form)
        self.drawBtn.setGeometry(QtCore.QRect(20, 430, 171, 51))
        self.drawBtn.setObjectName("drawBtn")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 100, 371, 114))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.BlueSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.BlueSpinBox.setEnabled(False)
        self.BlueSpinBox.setMaximum(255)
        self.BlueSpinBox.setObjectName("BlueSpinBox")
        self.gridLayout.addWidget(self.BlueSpinBox, 2, 2, 1, 1)
        self.RedSlide = QtWidgets.QSlider(self.groupBox)
        self.RedSlide.setEnabled(False)
        self.RedSlide.setMaximum(255)
        self.RedSlide.setOrientation(QtCore.Qt.Horizontal)
        self.RedSlide.setObjectName("RedSlide")
        self.gridLayout.addWidget(self.RedSlide, 0, 1, 1, 1)
        self.BlueSlide = QtWidgets.QSlider(self.groupBox)
        self.BlueSlide.setEnabled(False)
        self.BlueSlide.setMaximum(255)
        self.BlueSlide.setOrientation(QtCore.Qt.Horizontal)
        self.BlueSlide.setObjectName("BlueSlide")
        self.gridLayout.addWidget(self.BlueSlide, 2, 1, 1, 1)
        self.GreenSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.GreenSpinBox.setEnabled(False)
        self.GreenSpinBox.setMaximum(255)
        self.GreenSpinBox.setObjectName("GreenSpinBox")
        self.gridLayout.addWidget(self.GreenSpinBox, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.GreenSlide = QtWidgets.QSlider(self.groupBox)
        self.GreenSlide.setEnabled(False)
        self.GreenSlide.setMaximum(255)
        self.GreenSlide.setOrientation(QtCore.Qt.Horizontal)
        self.GreenSlide.setObjectName("GreenSlide")
        self.gridLayout.addWidget(self.GreenSlide, 1, 1, 1, 1)
        self.RedSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.RedSpinBox.setEnabled(False)
        self.RedSpinBox.setMaximum(255)
        self.RedSpinBox.setObjectName("RedSpinBox")
        self.gridLayout.addWidget(self.RedSpinBox, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.displayColorWidget = QtWidgets.QFrame(self.groupBox)
        self.displayColorWidget.setMinimumSize(QtCore.QSize(64, 73))
        self.displayColorWidget.setAutoFillBackground(True)
        self.displayColorWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.displayColorWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.displayColorWidget.setObjectName("displayColorWidget")
        self.gridLayout.addWidget(self.displayColorWidget, 0, 3, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 230, 371, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 21, 351, 74))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btnT_L = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnT_L.setObjectName("btnT_L")
        self.gridLayout_2.addWidget(self.btnT_L, 0, 0, 1, 1)
        self.btnT_R = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnT_R.setObjectName("btnT_R")
        self.gridLayout_2.addWidget(self.btnT_R, 0, 1, 1, 1)
        self.btnB_L = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnB_L.setObjectName("btnB_L")
        self.gridLayout_2.addWidget(self.btnB_L, 1, 0, 1, 1)
        self.btnB_R = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnB_R.setObjectName("btnB_R")
        self.gridLayout_2.addWidget(self.btnB_R, 1, 1, 1, 1)
        self.btnCenter = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnCenter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnCenter.setObjectName("btnCenter")
        self.gridLayout_2.addWidget(self.btnCenter, 2, 0, 1, 1)
        self.btnOther = QtWidgets.QRadioButton(self.layoutWidget)
        self.btnOther.setObjectName("btnOther")
        self.gridLayout_2.addWidget(self.btnOther, 2, 1, 1, 1)
        self.max_X = QtWidgets.QLabel(self.groupBox_2)
        self.max_X.setGeometry(QtCore.QRect(10, 140, 161, 16))
        self.max_X.setText("")
        self.max_X.setObjectName("max_X")
        self.max_Y = QtWidgets.QLabel(self.groupBox_2)
        self.max_Y.setGeometry(QtCore.QRect(10, 160, 161, 16))
        self.max_Y.setText("")
        self.max_Y.setObjectName("max_Y")
        self.splitter = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter.setGeometry(QtCore.QRect(190, 110, 121, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.txtX = QtWidgets.QSpinBox(self.splitter)
        self.txtX.setMaximum(999999999)
        self.txtX.setObjectName("txtX")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_2.setGeometry(QtCore.QRect(190, 140, 121, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setObjectName("label_5")
        self.txtY = QtWidgets.QSpinBox(self.splitter_2)
        self.txtY.setMaximum(999999999)
        self.txtY.setObjectName("txtY")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(130, 70, 50, 22))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(50, 0))
        self.label_6.setObjectName("label_6")
        self.fontsizeSpinBox = QtWidgets.QSpinBox(Form)
        self.fontsizeSpinBox.setGeometry(QtCore.QRect(190, 70, 51, 22))
        self.fontsizeSpinBox.setMinimum(1)
        self.fontsizeSpinBox.setProperty("value", 18)
        self.fontsizeSpinBox.setObjectName("fontsizeSpinBox")
        self.btnUndo = QtWidgets.QPushButton(Form)
        self.btnUndo.setGeometry(QtCore.QRect(220, 430, 171, 51))
        self.btnUndo.setObjectName("btnUndo")

        self.retranslateUi(Form)
        self.GreenSlide.valueChanged['int'].connect(self.GreenSpinBox.setValue) # type: ignore
        self.BlueSlide.valueChanged['int'].connect(self.BlueSpinBox.setValue) # type: ignore
        self.RedSpinBox.valueChanged['int'].connect(self.RedSlide.setValue) # type: ignore
        self.BlueSpinBox.valueChanged['int'].connect(self.BlueSlide.setValue) # type: ignore
        self.RedSlide.valueChanged['int'].connect(self.RedSpinBox.setValue) # type: ignore
        self.GreenSpinBox.valueChanged['int'].connect(self.GreenSlide.setValue) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.drawBtn.setText(_translate("Form", "Draw"))
        self.groupBox.setTitle(_translate("Form", "Color"))
        self.label_2.setText(_translate("Form", "G"))
        self.label.setText(_translate("Form", "R"))
        self.label_3.setText(_translate("Form", "B"))
        self.groupBox_2.setTitle(_translate("Form", "Position"))
        self.btnT_L.setText(_translate("Form", "Top-Left"))
        self.btnT_R.setText(_translate("Form", "Top-Right"))
        self.btnB_L.setText(_translate("Form", "Bottom-Left"))
        self.btnB_R.setText(_translate("Form", "Bottom-Right"))
        self.btnCenter.setText(_translate("Form", "Center"))
        self.btnOther.setText(_translate("Form", "Other"))
        self.label_4.setText(_translate("Form", "X"))
        self.label_5.setText(_translate("Form", "Y"))
        self.label_6.setText(_translate("Form", "Font size"))
        self.btnUndo.setText(_translate("Form", "Undo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
