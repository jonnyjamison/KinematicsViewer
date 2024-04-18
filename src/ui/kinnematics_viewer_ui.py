# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesigner/KinnematicsViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ui.plotting_features import PlottingFeatures


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 661)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(330, 170, 191, 61))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.plotArea = QtWidgets.QFrame(self.centralwidget)
        self.plotArea.setGeometry(QtCore.QRect(30, 70, 521, 461))
        self.plotArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plotArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plotArea.setObjectName("plotArea")
        self.kinData = QtWidgets.QTabWidget(self.centralwidget)
        self.kinData.setGeometry(QtCore.QRect(580, 60, 391, 241))
        self.kinData.setObjectName("kinData")
        self.front = QtWidgets.QWidget()
        self.front.setObjectName("front")
        self.frontInput = QtWidgets.QTableWidget(self.front)
        self.frontInput.setGeometry(QtCore.QRect(20, 10, 351, 192))
        self.frontInput.setObjectName("frontInput")
        self.frontInput.setColumnCount(3)
        self.frontInput.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.frontInput.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.frontInput.setHorizontalHeaderItem(2, item)
        self.frontInput.horizontalHeader().setDefaultSectionSize(50)
        self.kinData.addTab(self.front, "")
        self.rear = QtWidgets.QWidget()
        self.rear.setObjectName("rear")
        self.rearInput = QtWidgets.QTableWidget(self.rear)
        self.rearInput.setGeometry(QtCore.QRect(20, 10, 351, 192))
        self.rearInput.setObjectName("rearInput")
        self.rearInput.setColumnCount(3)
        self.rearInput.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        item.setFont(font)
        self.rearInput.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.rearInput.setHorizontalHeaderItem(2, item)
        self.rearInput.horizontalHeader().setDefaultSectionSize(50)
        self.kinData.addTab(self.rear, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 540, 521, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frontView = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.frontView.setObjectName("frontView")
        self.horizontalLayout.addWidget(self.frontView)
        self.sideView = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sideView.setObjectName("sideView")
        self.horizontalLayout.addWidget(self.sideView)
        self.topView = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.topView.setObjectName("topView")
        self.horizontalLayout.addWidget(self.topView)
        self.rearView = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.rearView.setObjectName("rearView")
        self.horizontalLayout.addWidget(self.rearView)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(600, 390, 351, 51))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 10, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkRollCentre = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkRollCentre.setObjectName("checkRollCentre")
        self.horizontalLayout_2.addWidget(self.checkRollCentre)
        self.checkWheelAxis = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkWheelAxis.setObjectName("checkWheelAxis")
        self.horizontalLayout_2.addWidget(self.checkWheelAxis)
        self.checkSideViewIC = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkSideViewIC.setObjectName("checkSideViewIC")
        self.horizontalLayout_2.addWidget(self.checkSideViewIC)
        self.tableOutput = QtWidgets.QTableWidget(self.centralwidget)
        self.tableOutput.setGeometry(QtCore.QRect(660, 450, 241, 151))
        self.tableOutput.setObjectName("tableOutput")
        self.tableOutput.setColumnCount(2)
        self.tableOutput.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableOutput.setHorizontalHeaderItem(1, item)
        self.tableOutput.horizontalHeader().setDefaultSectionSize(75)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 481, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("QtDesigner/../image/logo.png"))
        self.label.setObjectName("label")
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setGeometry(QtCore.QRect(660, 310, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName("plotButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 978, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuImport = QtWidgets.QMenu(self.menuBar)
        self.menuImport.setObjectName("menuImport")
        self.menuExport = QtWidgets.QMenu(self.menuBar)
        self.menuExport.setObjectName("menuExport")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionImport_from_xls = QtWidgets.QAction(MainWindow)
        self.actionImport_from_xls.setObjectName("actionImport_from_xls")
        self.actionExport_to_xls = QtWidgets.QAction(MainWindow)
        self.actionExport_to_xls.setObjectName("actionExport_to_xls")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuImport.addAction(self.actionImport_from_xls)
        self.menuExport.addAction(self.actionExport_to_xls)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuImport.menuAction())
        self.menuBar.addAction(self.menuExport.menuAction())

        self.retranslateUi(MainWindow)
        self.kinData.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kinnematics Viewer"))
        item = self.frontInput.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Upper Wishbone - Leading Pivot"))
        item = self.frontInput.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upper Wishbone - Trailling Pivot"))
        item = self.frontInput.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Upper Wishbone - Upright Pivot"))
        item = self.frontInput.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Lower Wishbone - Leading Pivot"))
        item = self.frontInput.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lower Wishbone - Trailling Pivot"))
        item = self.frontInput.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lower Wishbone - Upright Pivot"))
        item = self.frontInput.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.frontInput.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.frontInput.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z"))
        self.kinData.setTabText(self.kinData.indexOf(self.front), _translate("MainWindow", "Front"))
        item = self.rearInput.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Upper Wishbone - Leading Pivot"))
        item = self.rearInput.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Upper Wishbone - Trailling Pivot"))
        item = self.rearInput.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Upper Wishbone - Upright Pivot"))
        item = self.rearInput.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Lower Wishbone - Leading Pivot"))
        item = self.rearInput.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Lower Wishbone - Trailling Pivot"))
        item = self.rearInput.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Lower Wishbone - Upright Pivot"))
        item = self.rearInput.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "x"))
        item = self.rearInput.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "y"))
        item = self.rearInput.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "z"))
        self.kinData.setTabText(self.kinData.indexOf(self.rear), _translate("MainWindow", "Rear"))
        self.frontView.setText(_translate("MainWindow", "Front"))
        self.sideView.setText(_translate("MainWindow", "Side"))
        self.topView.setText(_translate("MainWindow", "Top"))
        self.rearView.setText(_translate("MainWindow", "Rear"))
        self.checkRollCentre.setText(_translate("MainWindow", "Roll Centre"))
        self.checkWheelAxis.setText(_translate("MainWindow", "Wheel Axis"))
        self.checkSideViewIC.setText(_translate("MainWindow", "Side View IC"))
        item = self.tableOutput.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Camber"))
        item = self.tableOutput.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Toe"))
        item = self.tableOutput.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Anti-Dive"))
        item = self.tableOutput.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Anti-Squat"))
        item = self.tableOutput.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Front"))
        item = self.tableOutput.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Rear"))
        self.plotButton.setText(_translate("MainWindow", "Plot!"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionImport_from_xls.setText(_translate("MainWindow", "Import from .xls"))
        self.actionExport_to_xls.setText(_translate("MainWindow", "Export to .xls"))



class KinematicsViewer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.plotting_features = PlottingFeatures(self.ui)



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
