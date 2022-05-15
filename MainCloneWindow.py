# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cloneUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QSizePolicy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 695)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        left_spacer = QWidget()
        left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_spacer = QWidget()
        right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.imgScreen = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgScreen.sizePolicy().hasHeightForWidth())
        self.imgScreen.setSizePolicy(sizePolicy)
        self.imgScreen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imgScreen.setText("")
        self.imgScreen.setAlignment(QtCore.Qt.AlignCenter)
        self.imgScreen.setObjectName("imgScreen")
        self.gridLayout.addWidget(self.imgScreen, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar_2)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionDraw_Text = QtWidgets.QAction(MainWindow)
        self.actionDraw_Text.setObjectName("actionDraw_Text")
        self.actionEnhance = QtWidgets.QAction(MainWindow)
        self.actionEnhance.setObjectName("actionEnhance")
        self.actionColor_Transforms = QtWidgets.QAction(MainWindow)
        self.actionColor_Transforms.setObjectName("actionColor_Transforms")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionFilter = QtWidgets.QAction(MainWindow)
        self.actionFilter.setObjectName("actionFilter")
        self.actionCrop = QtWidgets.QAction(MainWindow)
        self.actionCrop.setObjectName("actionCrop")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionlabel = QtWidgets.QAction(MainWindow)
        self.actionlabel.setText("")
        self.actionlabel.setObjectName("actionlabel")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addWidget(left_spacer)
        self.toolBar.addAction(self.actionDraw_Text)
        self.toolBar.addAction(self.actionEnhance)
        self.toolBar.addAction(self.actionColor_Transforms)
        self.toolBar.addAction(self.actionRotate)
        self.toolBar.addAction(self.actionFilter)
        self.toolBar.addAction(self.actionCrop)
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addWidget(right_spacer)
        self.toolBar_2.addAction(self.actionlabel)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.actionDraw_Text.setText(_translate("MainWindow", "Draw Text"))
        self.actionEnhance.setText(_translate("MainWindow", "Enhance"))
        self.actionColor_Transforms.setText(_translate("MainWindow", "Color Transforms"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionFilter.setText(_translate("MainWindow", "Filter"))
        self.actionCrop.setText(_translate("MainWindow", "Crop"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        MainWindow.showMaximized()

