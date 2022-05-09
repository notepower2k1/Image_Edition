from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMouseTracking(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 190, 58, 15))
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))

class Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, e):
        text = "x: {0},  y: {1}".format(e.x(), e.y())
        self.label.setText(text)
        self.label.adjustSize()
        super(Form, self).mouseMoveEvent(e)

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
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())