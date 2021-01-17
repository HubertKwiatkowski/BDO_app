import sys


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.uic import loadUi


"""
Window index list:
0 - MainWindow
1 - KutumVsNouverWindow
2 - CookingWindow
3 - NodesWindow
4 - AlchemyWindow
5 - ProcessingWindow
6 - PriceCheckWindow
"""


class MainWindow(QMainWindow):
    """A class to manage the main window."""
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/mainWindow.ui", self)

        self.kutVsNouButton.clicked.connect(self.gotoKutVsNou)
        self.cookingButton.clicked.connect(self.gotoCooking)
        self.nodesButton.clicked.connect(self.gotoNodes)
        self.alchemyButton.clicked.connect(self.gotoAlchemy)
        self.processingButton.clicked.connect(self.gotoProcessing)
        self.priceCheckButton.clicked.connect(self.gotoPriceCheck)

    def gotoKutVsNou(self):
        widget.setCurrentIndex(1)

    def gotoCooking(self):
        widget.setCurrentIndex(2)

    def gotoNodes(self):
        widget.setCurrentIndex(3)

    def gotoAlchemy(self):
        widget.setCurrentIndex(4)

    def gotoProcessing(self):
        widget.setCurrentIndex(5)

    def gotoPriceCheck(self):
        widget.setCurrentIndex(6)


class KutumVsNouverWindow(QMainWindow):
    """Window for the Kutum vs Nouver comparison."""
    def __init__(self):
        super(KutumVsNouverWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/kutVsNou.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)
        self.submitButton.clicked.connect(self.submit)

    def submit(self):
        """Check if all the data inputs are ok and run calculations."""

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

        import modules.cooking as cooking
        import modules.priceCheck as pc

        self.pc = pc
        self.allRecipes = cooking.importAll()
        self.allItems = pc.importAll()

        self.showRecipes()

        self.calcButton.clicked.connect(lambda: self.priceLabel.setText(self._changePriceLabel()))

        self.mainButton.clicked.connect(self.gotoMain)

    def showRecipes(self):
        """Show all the recipes."""
        for row in range(len(self.allRecipes)):
            self.cookingList.insertItem(row, self.allRecipes[row][0])

        self.cookingList.currentRowChanged.connect(
            lambda: self.infoLabel.setText(self._changeInfoLabel())
        )
        
        self.cookingList.currentRowChanged.connect(
            lambda: self.ingLabel.setText(self._changeIngLabel())
        )

        self.cookingList.currentRowChanged.connect(
            lambda: self.priceLabel.setText("")
        )


    def _changeInfoLabel(self):
        """Display info about the meal."""
 
        infoLabelText = f"""Effect:\n{self.allRecipes[self.cookingList.currentRow()][14]}\n"""

        return infoLabelText


    def _changeIngLabel(self):
        """Display ingredients."""
 
        ingLabelText = f"""Ingredients:
{self.allRecipes[self.cookingList.currentRow()][4]} {self.allRecipes[self.cookingList.currentRow()][5]}
{self.allRecipes[self.cookingList.currentRow()][6]} {self.allRecipes[self.cookingList.currentRow()][7]}
{self.allRecipes[self.cookingList.currentRow()][8]} {self.allRecipes[self.cookingList.currentRow()][9]}
{self.allRecipes[self.cookingList.currentRow()][10]} {self.allRecipes[self.cookingList.currentRow()][11]}
{self.allRecipes[self.cookingList.currentRow()][12]} {self.allRecipes[self.cookingList.currentRow()][13]}\n
Skill level required:   {self.allRecipes[self.cookingList.currentRow()][2]}\n
Expirience:     {self.allRecipes[self.cookingList.currentRow()][1]}\n"""

        return ingLabelText

    def _changePriceLabel(self):
        """Display prices."""
        prices = []
        prices = self._calculateMeal()
        mealPrice = int(prices[0])
        totalPrice = int((prices[1]) / 2.5)
        base = 0.65
        zeroFive = 0.005
        oneZero = 0.01
        oneFive = 0.015
        valuePack = 0.3
        bonus = 0
        if self.zeroFiveCheckBox.checkState() == 2:
            bonus = zeroFive
        if self.oneZeroCheckBox.checkState() == 2:
            bonus = oneFZero
        if self.oneFiveCheckBox.checkState() == 2:
            bonus = oneFive      
        if self.valuePackCheckBox.checkState() == 2: 
            bonus += valuePack
        
        if bonus == 0:
            netto = base
        else:
            netto = base * (1 + bonus)

        priceLabelText = f"""Price check:
Ingredients market price:   {totalPrice}
Meal market price:  {mealPrice} (taxed {int(mealPrice * netto)})
Gain/loss (if sold to MP):  {int(mealPrice * netto - totalPrice)}"""

        return priceLabelText

    def _checkName(self, itemName):
        """Check if the name is generic or detail (eg. Red Meat or Lamb Meat)"""
        if itemName == 'Red Meat':
            itemName = 'Wolf Meat'
        if itemName == 'Flour':
            itemName = 'Barley Flour'
        if itemName == 'Grain':
            itemName = 'Barley'
        if itemName == 'Dough':
            itemName = 'Barley Dough'
        return itemName

    def _calculateMeal(self):
        """Calculate gain/loss on 1 meal."""
        checkIng = []
        ingQty = []
        itemsPrice = []
        itemsQty = []
        mealPrice = 0
        totalPrice = 0
        mpItems = self.allItems
        # Non-market ingredients
        npcPrices = {
            'Salt': 20,
            'Sugar': 20,
            'Leavening Agent': 20,
            'Cooking Oil': 20,
            'Deep Frying Oil': 40,
            'Cooking Wine': 40,
            'Base Sauce': 40,
            'Mineral Water': 30,
            'Vegetable': 850,
            'Fruit': 650
            }

        # Check price of the main meal
        mealName = self.allRecipes[self.cookingList.currentRow()][0]
        if mealName != '':
            for mpItem in range(len(mpItems)):
                if mealName == mpItems[mpItem][6]:
                    a = 'eu'                    # region
                    b = mpItems[mpItem][5]      # mainKey
                    c = mpItems[mpItem][9]      # subKey
                    mealPrice = self._priceCheck(a, b, c)

        # Make a list of ingredients
        ing1Qty = self.allRecipes[self.cookingList.currentRow()][4]
        ing1Name = self.allRecipes[self.cookingList.currentRow()][5]
        if ing1Name != '':
            item1 = self._checkName(ing1Name)
            checkIng.append(item1)
            ingQty.append(ing1Qty)

        ing2Qty = self.allRecipes[self.cookingList.currentRow()][6]
        mat2Name = self.allRecipes[self.cookingList.currentRow()][7]
        if mat2Name != '':
            item2 = self._checkName(mat2Name)
            checkIng.append(item2)
            ingQty.append(ing2Qty)

        ing3Qty = self.allRecipes[self.cookingList.currentRow()][8]
        mat3Name = self.allRecipes[self.cookingList.currentRow()][9]
        if mat3Name != '':
            item3 = self._checkName(mat3Name)
            checkIng.append(item3)
            ingQty.append(ing3Qty)

        ing4Qty = self.allRecipes[self.cookingList.currentRow()][10]
        mat4Name = self.allRecipes[self.cookingList.currentRow()][11]
        if mat4Name != '':
            item4 = self._checkName(mat4Name)
            checkIng.append(item4)
            ingQty.append(ing4Qty)

        ing5Qty = self.allRecipes[self.cookingList.currentRow()][12]
        mat5Name = self.allRecipes[self.cookingList.currentRow()][13]
        if mat5Name != '':
            item5 = self._checkName(mat5Name)
            checkIng.append(item5)
            ingQty.append(ing5Qty)

        # Check prices for all the ingredients
        count = 0
        for ing in checkIng:
            for mpItem in range(len(mpItems)):
                if ing == mpItems[mpItem][6]:
                    a = 'eu'                    # region
                    b = mpItems[mpItem][5]      # mainKey
                    c = mpItems[mpItem][9]      # subKey
                    price = int(self._priceCheck(a, b, c))
                    qty = int(ingQty[count])
                    totalPrice += price * qty
                    count += 1
            for key in npcPrices.keys():
                if ing == key:
                    price = npcPrices[key]
                    qty = int(ingQty[count])
                    totalPrice += price * qty
                    count += 1

        # Return the price of main meal and cost of all ingredients
        return mealPrice, totalPrice

    def _priceCheck(self, a, b, c):
        """Check the market price of an item."""
        priceCheck = self.pc.priceCheck(a, b, c)

        return priceCheck[7]

    def gotoMain(self):
        widget.setCurrentIndex(0)


class AlchemyWindow(QMainWindow):
    """A class to manage the cooking window."""
    def __init__(self):
        super(AlchemyWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/alchemyWindow.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)
        self.recipesButton.clicked.connect(self.showRecipes)

    def showRecipes(self):
        """Load all the recipes to the view."""
        import modules.alchemy as alchemy

        self.allRecipes = alchemy.importAll()

        for row in range(len(self.allRecipes)):
            self.alchemyList.insertItem(row, self.allRecipes[row][0])

        self.alchemyList.currentRowChanged.connect(
            lambda: self.infoLabel.setText(
                f"""Effect:
{self.allRecipes[self.alchemyList.currentRow()][14]}\n
Ingredients:
{self.allRecipes[self.alchemyList.currentRow()][4]} {self.allRecipes[self.alchemyList.currentRow()][5]}
{self.allRecipes[self.alchemyList.currentRow()][6]} {self.allRecipes[self.alchemyList.currentRow()][7]}
{self.allRecipes[self.alchemyList.currentRow()][8]} {self.allRecipes[self.alchemyList.currentRow()][9]}
{self.allRecipes[self.alchemyList.currentRow()][10]} {self.allRecipes[self.alchemyList.currentRow()][11]}
{self.allRecipes[self.alchemyList.currentRow()][12]} {self.allRecipes[self.alchemyList.currentRow()][13]}\n
Skill level required:   {self.allRecipes[self.alchemyList.currentRow()][2]}\n
Expirience:     {self.allRecipes[self.alchemyList.currentRow()][1]}
                """
                )
            )

    def gotoMain(self):
        widget.setCurrentIndex(0)


class ProcessingWindow(QMainWindow):
    """A class to manage the cooking window."""
    def __init__(self):
        super(ProcessingWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/processingWindow.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)

    def showRecipes(self):
        """Load all the recipes to the view."""
        import modules.processing as proc

        self.allRecipes = proc.importAll()

        for row in range(len(self.allRecipes)):
            self.processingList.insertItem(row, self.allRecipes[row][0])

        self.processingList.currentRowChanged.connect(
            lambda: self.infoLabel.setText(
                f"""Effect:
{self.allRecipes[self.processingList.currentRow()][14]}\n
Ingredients:
{self.allRecipes[self.processingList.currentRow()][4]} {self.allRecipes[self.processingList.currentRow()][5]}
{self.allRecipes[self.processingList.currentRow()][6]} {self.allRecipes[self.processingList.currentRow()][7]}
{self.allRecipes[self.processingList.currentRow()][8]} {self.allRecipes[self.processingList.currentRow()][9]}
{self.allRecipes[self.processingList.currentRow()][10]} {self.allRecipes[self.processingList.currentRow()][11]}
{self.allRecipes[self.processingList.currentRow()][12]} {self.allRecipes[self.processingList.currentRow()][13]}\n
Skill level required:   {self.allRecipes[self.processingList.currentRow()][2]}\n
Expirience:     {self.allRecipes[self.processingList.currentRow()][1]}
                """
                )
            )


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

        #set size of the table
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 195)
        self.tableWidget.setColumnWidth(2, 190)
        self.tableWidget.setColumnWidth(3, 30)
        self.tableWidget.setColumnWidth(4, 180)
        self.tableWidget.setColumnWidth(5, 30)

        # filter buttons
        self.allButton.clicked.connect(self.showAll)
        self.balenosButton.clicked.connect(self.showBalenos)
        self.calpheonButton.clicked.connect(self.showCalpheon)
        self.drieghanButton.clicked.connect(self.showDrieghan)
        self.kamasylviaButton.clicked.connect(self.showKamasylvia)
        self.mediahButton.clicked.connect(self.showMediah)
        self.odyllitaButton.clicked.connect(self.showOdyllita)
        self.serendiaButton.clicked.connect(self.showSerendia)
        self.valenciaButton.clicked.connect(self.showValencia)

        # return to Main window
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


class PriceCheckWindow(QMainWindow):
    """A class to manage the price check window."""
    def __init__(self):
        super(PriceCheckWindow, self).__init__()
        loadUi("BDO_app/pyqt5_ui/priceCheckWindow.ui", self)

        import modules.priceCheck as pc

        self.allItems = pc.importAll()

        for row in range(len(self.allItems)):
            self.itemsList.insertItem(row, self.allItems[row][13])

        self.itemsList.currentRowChanged.connect(
            lambda: self.infoLabel.setText(self._checkItem())
            )

        self.mainButton.clicked.connect(self.gotoMain)


    def _checkItem(self):
        import modules.priceCheck as pc

        region = ['eu', 'na']

        a = region[0]                                       # region
        b = self.allItems[self.itemsList.currentRow()][5]   # mainKey
        c = self.allItems[self.itemsList.currentRow()][9]   # subKey
        d = pc.priceCheck(a, b, c)

        checkItem = ("Price: " + d[7])

        return checkItem

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
    alchemyWindow = AlchemyWindow()
    processingWindow = ProcessingWindow()
    priceCheckWindow = PriceCheckWindow()

    widget.addWidget(mainWindow)            # index 0
    widget.addWidget(kutumVsNouverWindow)   # index 1
    widget.addWidget(cookingWindow)         # index 2
    widget.addWidget(nodesWindow)           # index 3
    widget.addWidget(alchemyWindow)         # index 4
    widget.addWidget(processingWindow)      # index 5
    widget.addWidget(priceCheckWindow)      # index 6

    widget.setFixedWidth(1200)
    widget.setFixedHeight(800)
    widget.show()
    sys.exit(app.exec_())
