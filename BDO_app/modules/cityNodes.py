import csv


def openCsv():
    """Open and import nodes csv."""
    csvFile = 'BDO_app/modules/nodes/cityNodes.csv'
    return csvFile


def importAll():
    csvFile = openCsv()
    allCityNodes = []

    with open(csvFile) as c:
        readCity = csv.reader(c)
        cityRow = next(readCity)
        count = 0
        for row in readCity:
            if row != ['', '', '', '', '', '']:
                if row[0] == '':
                    row[0] = allCityNodes[(count-1)][0]
                if row[1] == '':
                    row[1] = allCityNodes[(count-1)][1]
                if row[2] == '':
                    row[2] = allCityNodes[(count-1)][2]
                if row[3] == '':
                    row[3] = allCityNodes[(count-1)][3]
                allCityNodes.append(row)
                count += 1

    return allCityNodes
