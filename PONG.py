__author__ = "reza0310"

from kivy.clock import Clock

from random import randint

from structures import Balle
import framework
import globals


class Coeur:

    def initialiser(self):
        self.balle = Balle()
        globals.hud.bind((250, 250), (500, 500), "globals.jeu.balle.descendre_raquette_gauche()")
        globals.hud.bind((750, 250), (500, 500), "globals.jeu.balle.descendre_raquette_droite()")
        globals.hud.bind((250, 750), (500, 500), "globals.jeu.balle.monter_raquette_gauche()")
        globals.hud.bind((750, 750), (500, 500), "globals.jeu.balle.monter_raquette_droite()")
        self.event = Clock.schedule_interval(self.actualiser, 1/globals.FPS)  # 60 fps

    def actualiser(self, dt):
        self.balle.actualiser()
