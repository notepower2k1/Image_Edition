# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ColorTransferUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColorTransfer_Form(object):
    def setupUi(self, ColorTransfer_Form):
        ColorTransfer_Form.setObjectName("ColorTransfer_Form")
        ColorTransfer_Form.setWindowModality(QtCore.Qt.NonModal)
        ColorTransfer_Form.resize(210, 368)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorTransfer_Form.sizePolicy().hasHeightForWidth())
        ColorTransfer_Form.setSizePolicy(sizePolicy)
        self.pushButton = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton.setGeometry(QtCore.QRect(9, 9, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton_2.setGeometry(QtCore.QRect(9, 124, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton_3.setGeometry(QtCore.QRect(9, 181, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 70, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton_5.setGeometry(QtCore.QRect(9, 238, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(ColorTransfer_Form)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 300, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")

        self.retranslateUi(ColorTransfer_Form)
        QtCore.QMetaObject.connectSlotsByName(ColorTransfer_Form)

    def retranslateUi(self, ColorTransfer_Form):
        _translate = QtCore.QCoreApplication.translate
        ColorTransfer_Form.setWindowTitle(_translate("ColorTransfer_Form", "Form"))
        self.pushButton.setText(_translate("ColorTransfer_Form", "Blue Magenta"))
        self.pushButton_2.setText(_translate("ColorTransfer_Form", "Green"))
        self.pushButton_3.setText(_translate("ColorTransfer_Form", "Brown"))
        self.pushButton_4.setText(_translate("ColorTransfer_Form", "Green Cyan"))
        self.pushButton_5.setText(_translate("ColorTransfer_Form", "Magenta Pink"))
        self.pushButton_6.setText(_translate("ColorTransfer_Form", "Undo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ColorTransfer_Form = QtWidgets.QWidget()
    ui = Ui_ColorTransfer_Form()
    ui.setupUi(ColorTransfer_Form)
    ColorTransfer_Form.show()
    sys.exit(app.exec_())
