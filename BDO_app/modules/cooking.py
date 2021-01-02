import csv
import modules.priceCheck as pc


def openCsv():
    """Open recipes csv."""
    csvFile = 'BDO_app/modules/crafting/cookingRecipes.csv'
    return csvFile

def importAll():
    """Import all the recipes."""
    csvFile = openCsv()
    allRecipes = []     # mealName, Xp, skillLevelRequired, craftStep,
                        # ing1Qty, ing1Name, ing2Qty, ing2Name, ing3Qty, ing3Name,
                        # ing4Qty, ing4Name, ing5Qty, ing5Name, usage

    with open(csvFile) as c:
        readRecipe = csv.reader(c)
        recipeRow = next(readRecipe)
        count = 0
        for row in readRecipe:
            allRecipes.append(row)
            count += 1

    return allRecipes

def checkPrice():
    """Check price of a single meal/ingredient."""
    pass
