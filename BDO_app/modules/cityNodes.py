import csv
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


cityNodes = []
workingNodes = []
city = ''

def openCsv():
    """Open and import nodes csv."""
    csvFile = 'BDO_app/modules/nodes/cityNodes.csv'
    return csvFile


def filterAll():
    city = openCsv()

    with open(city) as c:
        cityNodes.clear()
        readCity = csv.reader(c)
        cityRow = next(readCity)
        count = 0
        for row in readCity:
            if row != ['', '', '', '', '', '']:
                if row[0] == '':
                    row[0] = cityNodes[(count-1)][0]
                if row[1] == '':
                    row[1] = cityNodes[(count-1)][1]
                if row[2] == '':
                    row[2] = cityNodes[(count-1)][2]
                if row[3] == '':
                    row[3] = cityNodes[(count-1)][3]
                cityNodes.append(row)
                count += 1

def filterBalenos():
    city = openCsv()

    with open(city) as c:
        cityNodes.clear()
        readCity = csv.reader(c)
        cityRow = next(readCity)
        count = 0
        for row in readCity:
            if row[0] == 'Balenos':
                if row != ['', '', '', '', '', '']:
                    if row[0] == '':
                        row[0] = cityNodes[(count-1)][0]
                    if row[1] == '':
                        row[1] = cityNodes[(count-1)][1]
                    if row[2] == '':
                        row[2] = cityNodes[(count-1)][2]
                    if row[3] == '':
                        row[3] = cityNodes[(count-1)][3]
                    cityNodes.append(row)
                    count += 1
