import csv

kutum = []  # [level, AP min, AP max, bonus AP]
nouver = [] # [level, AP min AP max, bonus AP]
bonus = []  # [AP, extra AP]


def openCsv():
    """Open and import kutum, nouver and bonus AP files."""
    kut = 'BDO_app/modules/kutVsNou/kutum.csv'
    nou = 'BDO_app/modules/kutVsNou/nouver.csv'
    bon = 'BDO_app/modules/kutVsNou/bonus_ap.csv'
    # global kutum, nouver, bonus

    # read kutum file
    with open(kut) as k:
        kutum.clear()
        readKutum = csv.reader(k)
        kutumRow = next(readKutum)
        for ku in readKutum:
            kutum.append(ku)

    # read nouver file
    with open(nou) as n:
        nouver.clear()
        no_reader = csv.reader(n)
        no_header_row = next(no_reader)
        for no in no_reader:
            nouver.append(no)

    # read bonus AP file
    with open(bon) as b:
        bonus.clear()
        bo_reader = csv.reader(b)
        bo_header_row = next(bo_reader)
        for bo in bo_reader:
            bonus.append(bo)


def calculateCurrent(totalAp, weapon):
    """Calculate current weapon AP."""
    base = _baseAp(totalAp, weapon)
    wLevel, minAp, maxAp, monsterAp = weapon
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(checkBonus(totalAp))
    pve = totalAp + bonusAp + int(monsterAp)
    pvp = totalAp + bonusAp
    return pve, pvp


def calcuclateAll(totalAp, weapon):
    """Calculate additional Kutum/Nouver levels."""
    base = _baseAp(totalAp, weapon)
    allAp = []
    weap = [kutum, nouver]
    level = [18, 19, 20]
    for w in range(len(weap)):
        for l in range(len(level)):
            lev = int(level[l])
            weapName = weap[w]
            ap = _weaponPve(base, weapName, lev)
            allAp.append(str(int(ap)))
    for w in range(len(weap)):
        for l in range(len(level)):
            lev = int(level[l])
            weapName = weap[w]
            ap = _weaponPvp(base, weapName, lev)
            allAp.append(str(int(ap)))
    return allAp


def _baseAp(totalAp, weapon):
    """Calculate base AP (no off-hand weapon)."""
    baseAp = totalAp - (int(weapon[1]) + int(weapon[2]))/2
    return baseAp


def _weaponPve(base, weapName, lev):
    """Calculate all PvE AP."""
    wLevel, minAp, maxAp, monsterAp = weapName[lev]
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(_checkBonus(totalAp))
    weaponPve = totalAp + bonusAp + int(monsterAp)
    return weaponPve


def _weaponPvp(base, weapName, lev):
    """Calculate all PVP AP."""
    wLevel, minAp, maxAp, monsterAp = weapName[lev]
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(_checkBonus(totalAp))
    weaponPvp = totalAp + bonusAp
    return weaponPvp


def _checkBonus(totalAp):
    """Check bonus AP."""
    if totalAp < int(bonus[0][0]):
        return 0
    elif totalAp > int(bonus[-1][0]):
        return bonus[-1][1]
    else:
        for bo in range(len(bonus)-1):
            b1 = int(bonus[bo][0])
            b2 = int(bonus[bo+1][0])
            try:
                if b1 <= totalAp < b2:
                    return bonus[bo][1]
            except:
                break
