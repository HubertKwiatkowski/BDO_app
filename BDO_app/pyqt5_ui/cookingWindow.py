# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cookingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainWindowLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainWindowLabel.setGeometry(QtCore.QRect(0, 20, 1201, 32))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.mainWindowLabel.setFont(font)
        self.mainWindowLabel.setAutoFillBackground(False)
        self.mainWindowLabel.setScaledContents(False)
        self.mainWindowLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainWindowLabel.setObjectName("mainWindowLabel")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 171, 213))
        self.layoutWidget.setObjectName("layoutWidget")
        self.cookingGrid = QtWidgets.QGridLayout(self.layoutWidget)
        self.cookingGrid.setContentsMargins(0, 0, 0, 0)
        self.cookingGrid.setObjectName("cookingGrid")
        self.toolsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.toolsButton.setEnabled(False)
        self.toolsButton.setFlat(False)
        self.toolsButton.setObjectName("toolsButton")
        self.cookingGrid.addWidget(self.toolsButton, 3, 0, 1, 1)
        self.guidsButton = QtWidgets.QPushButton(self.layoutWidget)
        self.guidsButton.setEnabled(False)
        self.guidsButton.setFlat(False)
        self.guidsButton.setObjectName("guidsButton")
        self.cookingGrid.addWidget(self.guidsButton, 4, 0, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(self.layoutWidget)
        self.calculateButton.setEnabled(True)
        self.calculateButton.setFlat(False)
        self.calculateButton.setObjectName("calculateButton")
        self.cookingGrid.addWidget(self.calculateButton, 5, 0, 1, 1)
        self.recipesButton = QtWidgets.QPushButton(self.layoutWidget)
        self.recipesButton.setEnabled(True)
        self.recipesButton.setFlat(False)
        self.recipesButton.setObjectName("recipesButton")
        self.cookingGrid.addWidget(self.recipesButton, 0, 0, 1, 1)
        self.masteryButton = QtWidgets.QPushButton(self.layoutWidget)
        self.masteryButton.setEnabled(False)
        self.masteryButton.setFlat(False)
        self.masteryButton.setObjectName("masteryButton")
        self.cookingGrid.addWidget(self.masteryButton, 2, 0, 1, 1)
        self.xpButton = QtWidgets.QPushButton(self.layoutWidget)
        self.xpButton.setEnabled(False)
        self.xpButton.setFlat(False)
        self.xpButton.setObjectName("xpButton")
        self.cookingGrid.addWidget(self.xpButton, 1, 0, 1, 1)
        self.mainButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mainButton.setEnabled(True)
        self.mainButton.setFlat(False)
        self.mainButton.setObjectName("mainButton")
        self.cookingGrid.addWidget(self.mainButton, 6, 0, 1, 1)
        self.cookingList = QtWidgets.QListWidget(self.centralwidget)
        self.cookingList.setEnabled(True)
        self.cookingList.setGeometry(QtCore.QRect(190, 90, 341, 571))
        self.cookingList.setObjectName("cookingList")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(600, 90, 591, 571))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.infoLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.infoLabel.setText("")
        self.infoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout.addWidget(self.infoLabel, 0, 0, 1, 1)
        self.ingLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.ingLabel.setText("")
        self.ingLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.ingLabel.setWordWrap(True)
        self.ingLabel.setObjectName("ingLabel")
        self.gridLayout.addWidget(self.ingLabel, 1, 0, 1, 1)
        self.priceLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.priceLabel.setText("")
        self.priceLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.priceLabel.setWordWrap(True)
        self.priceLabel.setObjectName("priceLabel")
        self.gridLayout.addWidget(self.priceLabel, 2, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 310, 171, 170))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.oneFiveCheckBox = QtWidgets.QCheckBox(self.widget)
        self.oneFiveCheckBox.setObjectName("oneFiveCheckBox")
        self.gridLayout_2.addWidget(self.oneFiveCheckBox, 5, 0, 1, 1)
        self.valuePackCheckBox = QtWidgets.QCheckBox(self.widget)
        self.valuePackCheckBox.setObjectName("valuePackCheckBox")
        self.gridLayout_2.addWidget(self.valuePackCheckBox, 1, 0, 1, 1)
        self.oneCheckBox = QtWidgets.QCheckBox(self.widget)
        self.oneCheckBox.setObjectName("oneCheckBox")
        self.gridLayout_2.addWidget(self.oneCheckBox, 4, 0, 1, 1)
        self.zeroCheckBox = QtWidgets.QCheckBox(self.widget)
        self.zeroCheckBox.setObjectName("zeroCheckBox")
        self.gridLayout_2.addWidget(self.zeroCheckBox, 2, 0, 1, 1)
        self.zeroFiveCheckBox = QtWidgets.QCheckBox(self.widget)
        self.zeroFiveCheckBox.setObjectName("zeroFiveCheckBox")
        self.gridLayout_2.addWidget(self.zeroFiveCheckBox, 3, 0, 1, 1)
        self.calcCheckBox = QtWidgets.QCheckBox(self.widget)
        self.calcCheckBox.setObjectName("calcCheckBox")
        self.gridLayout_2.addWidget(self.calcCheckBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainWindowLabel.setText(_translate("MainWindow", "Cooking"))
        self.toolsButton.setText(_translate("MainWindow", "Cooking Tools"))
        self.guidsButton.setText(_translate("MainWindow", "Guids"))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.recipesButton.setText(_translate("MainWindow", "Recipes"))
        self.masteryButton.setText(_translate("MainWindow", "Cooking Mastery"))
        self.xpButton.setText(_translate("MainWindow", "Cooking XP"))
        self.mainButton.setText(_translate("MainWindow", "Main"))
        self.oneFiveCheckBox.setText(_translate("MainWindow", "1.5%"))
        self.valuePackCheckBox.setText(_translate("MainWindow", "Value Pack"))
        self.oneCheckBox.setText(_translate("MainWindow", "1.0%"))
        self.zeroCheckBox.setText(_translate("MainWindow", "0.0%"))
        self.zeroFiveCheckBox.setText(_translate("MainWindow", "0.5%"))
        self.calcCheckBox.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())