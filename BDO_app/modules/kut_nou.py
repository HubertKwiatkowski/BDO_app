import csv
from tkinter import *

kutum = [] # [level, AP min, AP max, bonus AP]
nouver = [] # [level, AP min AP max]
bonus = [] # [AP, extra AP]

def open_kutum_nouver(apLevel, kutLevel, nouLevel):
    """Open kutum, nouver and bonus AP files."""
    kut = 'modules/kut_nou/kutum.csv'
    nou = 'modules/kut_nou/nouver.csv'
    bon = 'modules/kut_nou/bonus_ap.csv'
    global kutum, nouver, bonus

    # read kutum file
    with open(kut) as k:
        kutum.clear()
        ku_reader = csv.reader(k)
        ku_header_row = next(ku_reader)
        for ku in ku_reader:
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

    _weapon_input(apLevel, kutLevel, nouLevel)

def _weapon_input(apLevel, kutLevel, nouLevel):
    """Input boss weapon level."""
    # Count kutum total ap
    k_level, k_min_ap, k_max_ap, k_bonus_ap = kutum[int(kutLevel)]
    k_ap = apLevel + round((int(k_min_ap) + int(k_max_ap))/2)
    k_total_ap = int(_chceck_bonus(k_ap)) + k_ap + int(k_bonus_ap)
    # Count nouver total ap
    n_level, n_min_ap, n_max_ap, n_bonus_ap = nouver[int(nouLevel)]
    try:
        n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2) + int(n_bonus_ap)
    except:
        n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2)
    n_total_ap = int(_chceck_bonus(n_ap)) + n_ap
    maximum = max(k_total_ap, n_total_ap)
    print(maximum)

def _chceck_bonus(ap):
    """Check bonus AP."""
    if ap < int(bonus[0][0]):
        return 0
    elif ap > int(bonus[-1][0]):
        return bonus[-1][1]
    else:
        for bo in range(len(bonus)-1):
            b1 = int(bonus[bo][0])
            b2 = int(bonus[bo+1][0])
            try:
                if b1 <= ap < b2:
                    return bonus[bo][1]
            except:
                break
