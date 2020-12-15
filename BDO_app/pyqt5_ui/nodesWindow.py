# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nodesWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWindowLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainWindowLabel.setGeometry(QtCore.QRect(0, 0, 800, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.mainWindowLabel.setFont(font)
        self.mainWindowLabel.setAutoFillBackground(False)
        self.mainWindowLabel.setScaledContents(False)
        self.mainWindowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainWindowLabel.setObjectName("mainWindowLabel")
        self.mainButton = QtWidgets.QPushButton(self.centralwidget)
        self.mainButton.setEnabled(True)
        self.mainButton.setGeometry(QtCore.QRect(630, 510, 150, 25))
        self.mainButton.setFlat(False)
        self.mainButton.setObjectName("mainButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 781, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.nodesGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.nodesGrid.setContentsMargins(0, 0, 0, 0)
        self.nodesGrid.setObjectName("nodesGrid")
        self.calpheonButton = QtWidgets.QPushButton(self.layoutWidget)
        self.calpheonButton.setEnabled(True)
        self.calpheonButton.setFlat(False)
        self.calpheonButton.setObjectName("calpheonButton")
        self.nodesGrid.addWidget(self.calpheonButton, 0, 1, 1, 1)
        self.balenosButton = QtWidgets.QPushButton(self.layoutWidget)
        self.balenosButton.setEnabled(True)
        self.balenosButton.setFlat(False)
        self.balenosButton.setObjectName("balenosButton")
        self.nodesGrid.addWidget(self.balenosButton, 0, 0, 1, 1)
        self.valencjaButton = QtWidgets.QPushButton(self.layoutWidget)
        self.valencjaButton.setEnabled(True)
        self.valencjaButton.setFlat(False)
        self.valencjaButton.setObjectName("valencjaButton")
        self.nodesGrid.addWidget(self.valencjaButton, 0, 7, 1, 1)
        self.mediahButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mediahButton.setEnabled(True)
        self.mediahButton.setFlat(False)
        self.mediahButton.setObjectName("mediahButton")
        self.nodesGrid.addWidget(self.mediahButton, 0, 4, 1, 1)
        self.kamasylviaButton = QtWidgets.QPushButton(self.layoutWidget)
        self.kamasylviaButton.setEnabled(True)
        self.kamasylviaButton.setFlat(False)
        self.kamasylviaButton.setObjectName("kamasylviaButton")
        self.nodesGrid.addWidget(self.kamasylviaButton, 0, 3, 1, 1)
        self.odyllitaButton = QtWidgets.QPushButton(self.layoutWidget)
        self.odyllitaButton.setEnabled(True)
        self.odyllitaButton.setFlat(False)
        self.odyllitaButton.setObjectName("odyllitaButton")
        self.nodesGrid.addWidget(self.odyllitaButton, 0, 5, 1, 1)
        self.serendiaButton = QtWidgets.QPushButton(self.layoutWidget)
        self.serendiaButton.setEnabled(True)
        self.serendiaButton.setFlat(False)
        self.serendiaButton.setObjectName("serendiaButton")
        self.nodesGrid.addWidget(self.serendiaButton, 0, 6, 1, 1)
        self.drieghanButton = QtWidgets.QPushButton(self.layoutWidget)
        self.drieghanButton.setEnabled(True)
        self.drieghanButton.setFlat(False)
        self.drieghanButton.setObjectName("drieghanButton")
        self.nodesGrid.addWidget(self.drieghanButton, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 120, 781, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainWindowLabel.setText(_translate("MainWindow", "Nodes"))
        self.mainButton.setText(_translate("MainWindow", "Main"))
        self.calpheonButton.setText(_translate("MainWindow", "Calpheon"))
        self.balenosButton.setText(_translate("MainWindow", "Balenos"))
        self.valencjaButton.setText(_translate("MainWindow", "Valencia"))
        self.mediahButton.setText(_translate("MainWindow", "Mediah"))
        self.kamasylviaButton.setText(_translate("MainWindow", "Kamasylvia"))
        self.odyllitaButton.setText(_translate("MainWindow", "O\'dyllita"))
        self.serendiaButton.setText(_translate("MainWindow", "Serendia"))
        self.drieghanButton.setText(_translate("MainWindow", "Drieghan"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Region"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CP"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Usage"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
