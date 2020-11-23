import csv
import sys
import math
from modules.kut_nou import open_kutum_nouver as opk

from tkinter import *

root = Tk()

kutum = [] # [level, AP min, AP max, bonus AP]
nouver = [] # [level, AP min AP max]
bonus = [] # [AP, extra AP]

class BDO_app:
    """A class to manage the app."""
    def __init__(self):
        """Initialize the app."""
        global kutNouCalc
        kutNouCalc = Button(root, text="K/N calculator", command=self._opk)

    def run_app(self):
        """Main loop of the app."""
        global kutNouCalc
        kutNouCalc.grid(row=0, column=0)
        root.mainloop()

    def _opk(self):
        apLevel, kutLevel, nouLevel = self._getAll()
        # kutLevel = self._getKutum()
        # nouLevel = self._getNouver()

        totalAP = opk(apLevel, kutLevel, nouLevel)

    def _getAll(self):
        global kutNouCalc
        kutNouCalc.grid_forget()

        apLevelLabel= Label(root, text="AP without offhand")
        kutLevelLabel= Label(root, text="Kutum level")
        nouLevelLabel= Label(root, text="Nouver level")

        apE = Entry(root, width=15, borderwidth=5)
        kutE = Entry(root, width=15, borderwidth=5)
        nouE = Entry(root, width=15, borderwidth=5)

        submit = Button(root, text="Submit", command=apE.get)
        # kutSubmit = Button(root, text="Submit", command=kutE.get)
        # nouSubmit = Button(root, text="Submit", command=nouE.get)

        apLevelLabel.grid(row=0, column=0)
        apE.grid(row=0, column=1)

        kutLevelLabel.grid(row=1, column=0)
        kutE.grid(row=1, column=1)

        nouLevelLabel.grid(row=2, column=0)
        nouE.grid(row=2, column=1)

        submit.grid(row=3, column=1)

        return apE.get(), kutE.get(), nouE.get()

"""    def _getKutum(self):
        global kutNouCalc
        levelLabel= Label(root, text="Kutum level")
        e = Entry(root, width=35, borderwidth=5)
        submit = Button(root, text="Submit", command=e.get)
        kutNouCalc.grid_forget()
        levelLabel.grid(row=0, column=0)
        e.grid(row=1, column=0)
        submit.grid(row=2, column=0)
        return e.get()

    def _getNouver(self):
        global kutNouCalc
        levelLabel= Label(root, text="Nouver level")
        e = Entry(root, width=35, borderwidth=5)
        submit = Button(root, text="Submit", command=e.get)
        kutNouCalc.grid_forget()
        levelLabel.grid(row=0, column=0)
        e.grid(row=1, column=0)
        submit.grid(row=2, column=0)
        return e.get()"""
