# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cookingCostWindow.ui'
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
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 761, 421))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 510, 481, 27))
        self.widget.setObjectName("widget")
        self.buttonsLayout = QtWidgets.QGridLayout(self.widget)
        self.buttonsLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonsLayout.setObjectName("buttonsLayout")
        self.calculateButton = QtWidgets.QPushButton(self.widget)
        self.calculateButton.setEnabled(True)
        self.calculateButton.setFlat(False)
        self.calculateButton.setObjectName("calculateButton")
        self.buttonsLayout.addWidget(self.calculateButton, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.widget)
        self.backButton.setEnabled(True)
        self.backButton.setFlat(False)
        self.backButton.setObjectName("backButton")
        self.buttonsLayout.addWidget(self.backButton, 0, 1, 1, 1)
        self.mainButton = QtWidgets.QPushButton(self.widget)
        self.mainButton.setEnabled(True)
        self.mainButton.setFlat(False)
        self.mainButton.setObjectName("mainButton")
        self.buttonsLayout.addWidget(self.mainButton, 0, 2, 1, 1)
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
        self.mainWindowLabel.setText(_translate("MainWindow", "Meal gain/loss"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Meal"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Market"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Meal1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Ingr1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Ingr2"))
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Ingr3"))
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Ingr4"))
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "Ingr5"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.mainButton.setText(_translate("MainWindow", "Main"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())