import pygame
import csv
import sys
import math

SCR_WIDTH, SCR_HEIGHT = 800, 800
kutum = [] # [level, AP min, AP max, bonus AP]
nouver = [] # [level, AP min AP max]
bonus = [] # [AP, extra AP]

class BDO_app:
    """A class to manage the app."""
    def __init__(self):
        """Initialize the app."""
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pygame.display.set_caption("BDO_app")

    def run_app(self):
        """Main loop of the app."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.open_kutum_nouver()
                self._weapon_level()

    def _update_screen(self):
        pass

    def open_kutum_nouver(self):
        """Open kutum, nouver and bonus AP files."""
        kut = 'docs/kut_vs_nou/kutum.csv'
        nou = 'docs/kut_vs_nou/nouver.csv'
        bon = 'docs/kut_vs_nou/bonus_ap.csv'
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

    def _weapon_level(self):
        """Input boss weapon level."""
        print('AP level without offhand weapon')
        ap = int(input('_> '))
        while True:
            print('Kutum weapon level? (0-20)')
            k_level = int(input('_> '))
            if 0 <= k_level <= 20:
                break
        while True:
            print('Nouver weapon level? (0-20)')
            n_level = int(input('_> '))
            if 0 <= n_level <= 20:
                break
        # Count kutum total ap
        k_level, k_min_ap, k_max_ap, k_bonus_ap = kutum[k_level]
        k_ap = ap + round((int(k_min_ap) + int(k_max_ap))/2)
        k_total_ap = int(self._chceck_bonus(k_ap)) + k_ap + int(k_bonus_ap)
        print(ap, k_ap, k_bonus_ap, int(self._chceck_bonus(k_ap)))
        # Count nouver total ap
        n_level, n_min_ap, n_max_ap, n_bonus_ap = nouver[n_level]
        try:
            n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2) + int(n_bonus_ap)
        except:
            n_ap = ap + round((int(n_min_ap) + int(n_max_ap))/2)
        n_total_ap = int(self._chceck_bonus(n_ap)) + n_ap
        maximum = max(k_total_ap, n_total_ap)
        print(maximum)

    def _chceck_bonus(self, ap):
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
