import csv
import modules.priceCheck as pc


def openRecipes():
    """Open recipes csv."""
    recipesFile = 'BDO_app/modules/crafting/cookingRecipes.csv'
    return recipesFile

def importAll():
    """Import all the recipes."""
    recipesCsv = openRecipes()
    allRecipes = []     # mealName, Xp, skillLevelRequired, craftStep,
                        # ing1Qty, ing1Name, ing2Qty, ing2Name, ing3Qty, ing3Name,
                        # ing4Qty, ing4Name, ing5Qty, ing5Name, usage

    with open(recipesCsv) as c:
        readRecipe = csv.reader(c)
        recipeRow = next(readRecipe)
        count = 0
        for row in readRecipe:
            allRecipes.append(row)
            count += 1

    return allRecipes
