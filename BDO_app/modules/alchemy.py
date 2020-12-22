import csv


def openCsv():
    """Open and import recipes csv."""
    csvFile = 'BDO_app/modules/crafting/alchemyRecipes.csv'
    return csvFile


def importAll():
    csvFile = openCsv()
    allRecipes = []

    with open(csvFile) as c:
        readRecipe = csv.reader(c)
        recipeRow = next(readRecipe)
        count = 0
        for row in readRecipe:
            if row != ['', '', '', '', '', '']:
                allRecipes.append(row)
                count += 1

    return allRecipes
