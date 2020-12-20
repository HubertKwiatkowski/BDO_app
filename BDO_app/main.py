import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUi


"""
Window index list:
0 - MainWindow
1 - KutumVsNouverWindow
2 - CookingWindow
3 - NodesWindow
"""


class MainWindow(QMainWindow):
    """A class to manage the main window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/mainWindow.ui", self)

        self.kutVsNouButton.clicked.connect(self.gotoKutVsNou)
        self.cookingButton.clicked.connect(self.gotoCooking)
        self.nodesButton.clicked.connect(self.gotoNodes)

    def gotoKutVsNou(self):
        widget.setCurrentIndex(1)

    def gotoCooking(self):
        widget.setCurrentIndex(2)

    def gotoNodes(self):
        widget.setCurrentIndex(3)


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
        """Calculate other AP."""

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


class NodesWindow(QMainWindow):
    """A class to manage the node window."""
    def __init__(self):
        super(NodesWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/nodesWindow.ui", self)

        self.importNodes()
        self.showAll()
        self.tableWidget.setSortingEnabled(False)

        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 195)
        self.tableWidget.setColumnWidth(2, 190)
        self.tableWidget.setColumnWidth(3, 30)
        self.tableWidget.setColumnWidth(4, 180)
        self.tableWidget.setColumnWidth(5, 30)

        self.allButton.clicked.connect(self.showAll)
        self.balenosButton.clicked.connect(self.showBalenos)
        self.calpheonButton.clicked.connect(self.showCalpheon)
        self.drieghanButton.clicked.connect(self.showDrieghan)
        self.kamasylviaButton.clicked.connect(self.showKamasylvia)
        self.mediahButton.clicked.connect(self.showMediah)
        self.odyllitaButton.clicked.connect(self.showOdyllita)
        self.serendiaButton.clicked.connect(self.showSerendia)
        self.valenciaButton.clicked.connect(self.showValencia)

        self.mainButton.clicked.connect(self.gotoMain)


    def importNodes(self):
        """Import city nodes and create the table."""
        import modules.cityNodes as cn

        self.allCityNodes = cn.importAll()

        for row in range(len(self.allCityNodes)):
            self.tableWidget.insertRow(row)
            width = len(self.allCityNodes[row])
            for col in range(width):
                item = QTableWidgetItem(self.allCityNodes[row][col])
                self.tableWidget.setItem(row, col, item)


    def showAll(self):
        """Show all the city nodes."""
        all = self.allCityNodes
        for row in range(len(all)):
            self.tableWidget.setRowHidden(row, False)

        self.tableWidget.setColumnWidth(2, 190)


    def showBalenos(self):
        """Show Balenos only city nodes."""
        balenos = self.allCityNodes
        for row in range(len(balenos)):
            if balenos[row][0] != 'Balenos':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)

        self.tableWidget.setColumnWidth(2, 195)


    def showCalpheon(self):
        """Show Calpheon only city nodes."""
        calpheon = self.allCityNodes
        for row in range(len(calpheon)):
            if calpheon[row][0] != 'Calpheon':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showDrieghan(self):
        """Show Drieghan only city nodes."""
        drieghan = self.allCityNodes
        for row in range(len(drieghan)):
            if drieghan[row][0] != 'Drieghan':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showKamasylvia(self):
        """Show Kamasylvia only city nodes."""
        kamasylvia = self.allCityNodes
        for row in range(len(kamasylvia)):
            if kamasylvia[row][0] != 'Kamasylvia':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showMediah(self):
        """Show Mediah only city nodes."""
        mediah = self.allCityNodes
        for row in range(len(mediah)):
            if mediah[row][0] != 'Mediah':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showOdyllita(self):
        """Show Odyllita only city nodes."""
        odyllita = self.allCityNodes
        for row in range(len(odyllita)):
            if odyllita[row][0] != 'Odyllita':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showSerendia(self):
        """Show Serendia only city nodes."""
        serendia = self.allCityNodes
        for row in range(len(serendia)):
            if serendia[row][0] != 'Serendia':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def showValencia(self):
        """Show Valencia only city nodes."""
        valencia = self.allCityNodes
        for row in range(len(valencia)):
            if valencia[row][0] != 'Valencia':
                self.tableWidget.setRowHidden(row, True)
            else:
                self.tableWidget.setRowHidden(row, False)


    def gotoMain(self):
        widget.setCurrentIndex(0)


def main():
    global app, widget
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    mainWindow = MainWindow()
    kutumVsNouverWindow = KutumVsNouverWindow()
    cookingWindow = CookingWindow()
    nodesWindow = NodesWindow()

    widget.addWidget(mainWindow)            # index 0
    widget.addWidget(kutumVsNouverWindow)   # index 1
    widget.addWidget(cookingWindow)         # index 2
    widget.addWidget(nodesWindow)           # index 3

    widget.setFixedWidth(800)
    widget.setFixedHeight(600)
    widget.show()
    sys.exit(app.exec_())
