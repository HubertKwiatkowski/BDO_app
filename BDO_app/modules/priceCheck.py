import csv, requests
from bs4 import BeautifulSoup


items = []  # chooseKey, count, grade, keyType, mainCategory, mainKey,
            #   name, pricePerOne, subCategory, subKey, totalTradeCount,
            #   mainLabel, subLabel, description
mpItems = [] # chooseKey, count, grade, keyType, mainCategory, mainKey,
            #   name, pricePerOne, subCategory, subKey, totalTradeCount


def openCsv():
    """Open csv file."""
    csvFile = 'BDO_app/modules/priceCheck/itemID.csv'
    return csvFile


def importAll():
    """Import all the items from csv file."""
    csvFile = openCsv()
    items = []  # chooseKey, count, grade, keyType, mainCategory, mainKey,
                #   name, pricePerOne, subCategory, subKey, totalTradeCount,
                #   mainLabel, subLabel, description

    with open(csvFile) as i:
        readItem = csv.reader(i)
        itemRow = next(readItem)
        for row in readItem:
            items.append(row)

    return items


def priceCheck(a, b, c):
    """Read one item from the link."""
    mpItem = []
    checkedItem = []

    url = 'http://omegapepega.com/' + a + '/' + b + '/' + c
    # url = http://omegapepega.com/region/mainKey/subKey
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find(text=True)
    splittedText = results.rsplit('\n')

    for line in splittedText:
        a = line.rstrip()
        mpItem.append(a.lstrip())

    mpItem.pop(0)
    mpItem.pop(-1)

    for i in mpItem:
        try:
            s = i.index(':')
            k = (i[:s])
            if i.endswith(','):
                v = (i[s+1:-1])
            else: v = (i[s+1:])
            checkedItem.append(v.strip())
        except:
            continue

    return checkedItem
