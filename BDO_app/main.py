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
        loadUi("BDO_app/pyqt5_ui/mainWindow.ui",self)

        self.kutVsNouButton.clicked.connect(self.gotoKutVsNou)

    def gotoKutVsNou(self):
        widget.setCurrentIndex(1)

class KutumVsNouverWindow(QMainWindow):
    def __init__(self):
        super(KutumVsNouverWindow, self).__init__()
        import modules.kutVsNou
        loadUi("BDO_app/pyqt5_ui/kutVsNou.ui", self)

        self.mainButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
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
