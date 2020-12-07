import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
from PyQt5.uic import loadUi


"""
Window index list:
0 - MainWindow
1 - KutumVsNouverWindow
"""


class MainWindow(QMainWindow):
    """A class to manage the main window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/mainWindow.ui", self)

        self.kutVsNouButton.clicked.connect(self.gotoKutVsNou)

    def gotoKutVsNou(self):
        widget.setCurrentIndex(1)

class KutumVsNouverWindow(QMainWindow):
    def __init__(self):
        super(KutumVsNouverWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/kutVsNou.ui", self)
        self.mainButton.clicked.connect(self.gotoMain)

        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        import modules.kutVsNou as kvs
        kvs.openCsv()
        self.errorLabel.setText("")
        weaponLevel = int(self.weaponLevelComboBox.currentText())
        totalAp = int(self.apLine.text())


        if self.kutumCheckBox.checkState() == 2 and self.nouverCheckBox.checkState() == 0:
            weapon = kvs.kutum[weaponLevel]
            self.calculate(totalAp, weapon, weaponLevel)
        elif self.kutumCheckBox.checkState() == 0 and self.nouverCheckBox.checkState() == 2:
            weapon = kvs.nouver[weaponLevel]
            self.calculate(totalAp, weapon, weaponLevel)
        elif self.kutumCheckBox.checkState() == 0 and self.nouverCheckBox.checkState() == 0:
            self.kutumCheckBox.setChecked(0)
            self.nouverCheckBox.setChecked(0)
            self.errorLabel.setText("Choose Kutum OR Nouver")


    def calculate(self, totalAp, weapon, weaponLevel):
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

class BDOApp:
    """A class to manage the app."""
    def __init__(self):
        """Initialize the app."""


    def runApp(self):
        widget.show()
        sys.exit(app.exec_())


    def changeWindow(self, index):
        widget.setCurrentIndex(index)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

mainWindow = MainWindow()
kutumVsNouverWindow = KutumVsNouverWindow()

widget.addWidget(mainWindow)    # index 0
widget.addWidget(kutumVsNouverWindow)   # index 1

widget.setFixedWidth(800)
widget.setFixedHeight(600)



"""
        # odczytanie poziomu broni

        # wygenerowanie PvE ap

        # wygenerowanie PvP ap

"""
