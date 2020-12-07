import csv

kutum = [] # [level, AP min, AP max, bonus AP]
nouver = [] # [level, AP min AP max]
bonus = [] # [AP, extra AP]


def openCsv():
    """Open kutum, nouver and bonus AP files."""
    kut = 'BDO_app/modules/kutVsNou/kutum.csv'
    nou = 'BDO_app/modules/kutVsNou/nouver.csv'
    bon = 'BDO_app/modules/kutVsNou/bonus_ap.csv'
    global kutum, nouver, bonus # sprawdzic, czy jest to tu potrzebne

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

def weaponInput(totalAp, weaponLevel):
    """Input boss weapon level."""
    # Count kutum total ap
    k_level, k_min_ap, k_max_ap, k_bonus_ap = kutum[int(kutLevel)]
    k_ap = apLevel + round((int(k_min_ap) + int(k_max_ap))/2)
    k_total_ap = int(checkBonus(k_ap)) + k_ap + int(k_bonus_ap)
    # Count nouver total ap
    n_level, n_min_ap, n_max_ap, n_bonus_ap = nouver[int(nouLevel)]
    try:
        n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2) + int(n_bonus_ap)
    except:
        n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2)
    n_total_ap = int(checkBonus(n_ap)) + n_ap
    maximum = max(k_total_ap, n_total_ap)


def calculateCurrent(totalAp, weapon):
    base = baseAp(totalAp, weapon)
    wLevel, minAp, maxAp, monsterAp = weapon
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(checkBonus(totalAp))
    pve = totalAp + bonusAp + int(monsterAp)
    pvp = totalAp + bonusAp
    return pve, pvp


def calcuclateAll(totalAp, weapon):
    base = baseAp(totalAp, weapon)
    allAp = []
    weap = [kutum, nouver]
    level = [18, 19, 20]
    for w in range(len(weap)):
        for l in range(len(level)):
            lev = int(level[l])
            weapName = weap[w]
            ap = weaponPve(base, weapName, lev)
            allAp.append(str(int(ap)))
    for w in range(len(weap)):
        for l in range(len(level)):
            lev = int(level[l])
            weapName = weap[w]
            ap = weaponPvp(base, weapName, lev)
            allAp.append(str(int(ap)))
    return allAp


def baseAp(totalAp, weapon):
    baseAp = totalAp - (int(weapon[1]) + int(weapon[2]))/2
    return baseAp


def weaponPve(base, weapName, lev):
    wLevel, minAp, maxAp, monsterAp = weapName[lev]
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(checkBonus(totalAp))
    weaponPve = totalAp + bonusAp + int(monsterAp)
    return weaponPve


def weaponPvp(base, weapName, lev):
    wLevel, minAp, maxAp, monsterAp = weapName[lev]
    totalAp = base + (int(minAp) + int(maxAp))/2
    bonusAp = int(checkBonus(totalAp))
    weaponPvp = totalAp + bonusAp
    return weaponPvp


def checkBonus(totalAp):
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
