import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5.uic import loadUi


"""
Window index list:
0 - MainWindow
1 - KutumVsNouverWindow
2 - CookingWindow
"""


class MainWindow(QMainWindow):
    """A class to manage the main window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/mainWindow.ui", self)

        self.kutVsNouButton.clicked.connect(self.gotoKutVsNou)
        self.cookingButton.clicked.connect(self.gotoCooking)

    def gotoKutVsNou(self):
        widget.setCurrentIndex(1)

    def gotoCooking(self):
        widget.setCurrentIndex(2)


class KutumVsNouverWindow(QMainWindow):
    """Window for the Kutum vs Nouver comparison."""
    def __init__(self):
        super(KutumVsNouverWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/kutVsNou.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)
        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        """Check if all the data inputs are ok."""

        import modules.kutVsNou as kvs

        kvs.openCsv()
        self.errorLabel.setText("")
        weaponLevel = int(self.weaponLevelComboBox.currentText())

        try:
            totalAp = int(self.apLine.text())
            if self.kutumCheckBox.checkState() == 2 and self.nouverCheckBox.checkState() == 0:
                weapon = kvs.kutum[weaponLevel]
                self._calculate(totalAp, weapon, weaponLevel)
            elif self.kutumCheckBox.checkState() == 0 and self.nouverCheckBox.checkState() == 2:
                weapon = kvs.nouver[weaponLevel]
                self._calculate(totalAp, weapon, weaponLevel)
            elif self.kutumCheckBox.checkState() == 0 and self.nouverCheckBox.checkState() == 0:
                self.kutumCheckBox.setChecked(0)
                self.nouverCheckBox.setChecked(0)
                self.errorLabel.setText("Choose Kutum OR Nouver")
        except:
            self.errorLabel.setText("Fill in your AP")
            self.apLine.setText("")


    def _calculate(self, totalAp, weapon, weaponLevel):
        """Calculate all the needed AP."""

        import modules.kutVsNou as kvs

        calculateCurrent = kvs.calculateCurrent(totalAp, weapon)
        self.totalPveApLabel.setText("Your total PvE AP " + str(int(calculateCurrent[0])))
        self.totalPvpApLabel.setText("Your total PvP AP " + str(int(calculateCurrent[1])))

        calculateRest = kvs.calcuclateAll(totalAp, weapon)
        apLabels = [
            self.kutPveTriApLabel,
            self.kutPveTetApLabel,
            self.kutPvePenApLabel,
            self.nouPveTriApLabel,
            self.nouPveTetApLabel,
            self.nouPvePenApLabel,
            self.kutPvpTriApLabel,
            self.kutPvpTetApLabel,
            self.kutPvpPenApLabel,
            self.nouPvpTriApLabel,
            self.nouPvpTetApLabel,
            self.nouPvpPenApLabel,
        ]
        a = 0
        for l in apLabels:
            l.setText(calculateRest[a])
            a += 1

    def gotoMain(self):
        self.errorLabel.setText("")
        self.kutumCheckBox.setChecked(0)
        self.nouverCheckBox.setChecked(0)
        widget.setCurrentIndex(0)


class CookingWindow(QMainWindow):
    """A class to manage the cooking window."""
    def __init__(self):
        super(CookingWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/cookingWindow.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)


    def gotoMain(self):
        widget.setCurrentIndex(0)


def main():
    global app, widget
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    mainWindow = MainWindow()
    kutumVsNouverWindow = KutumVsNouverWindow()
    cookingWindow = CookingWindow()

    widget.addWidget(mainWindow)    # index 0
    widget.addWidget(kutumVsNouverWindow)   # index 1
    widget.addWidget(cookingWindow)

    widget.setFixedWidth(800)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())
