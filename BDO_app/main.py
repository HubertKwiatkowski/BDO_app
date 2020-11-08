import pygame
import csv
import sys

SCR_WIDTH, SCR_HEIGHT = 800, 800
kutum = [] # [level, AP min AP max, bonus AP]
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
                self._chceck_bonus()

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

    def _chceck_bonus(self):
        """Check bonus AP.""" # needs to work with total AP after kutum/nouver
        print('AP level without offhand weapon')
        a = int(input('_> '))
        if a < int(bonus[0][0]):
            return 0
        elif a > int(bonus[-1][0]):
            return bonus[-1][1])
        else:
            for bo in range(len(bonus)-1):
                b1 = int(bonus[bo][0])
                b2 = int(bonus[bo+1][0])
                try:
                    if b1 <= a <= b2:
                        return bonus[bo][1]
                except:
                    break
