__author__ = "reza0310"

from kivy.clock import Clock

import time
import os

import globals
import framework

class Balle():

    def __init__(self):
        self.x = 500
        self.y = 500
        self.yd = 500
        self.yg = 500
        self.score = [0, 0]
        self.direction_x = False
        self.direction_y = True
        self.vitesse_x = 10
        self.vitesse_y = 5

    def actualiser(self):
        globals.hud.image(500, 500, 1000, 1000, globals.images["fond"])
        globals.hud.image(self.x, self.y, 70, 100, globals.images["sprite"])
        globals.hud.image(50, self.yg, 50, 300, globals.images["sprite"])
        globals.hud.image(950, self.yd, 50, 300, globals.images["sprite"])
        globals.hud.texte(500, 900, str(self.score[0])+" VS "+str(self.score[1]), color=(1, 1, 1, 1), taille_police=100)
        
        if self.direction_y:
            self.y += self.vitesse_y
            if self.y >= 950:
                self.direction_y = False
        else:
            self.y -= self.vitesse_y
            if self.y <= 50:
                self.direction_y = True
                
        if self.direction_x:
            self.x += self.vitesse_x
            if self.x >= 890:
                self.direction_x = False
                if self.yd-195 <= self.y <= self.yd+195:
                    self.vitesse_y += 2
                else:
                    self.score[0] += 1
                    self.vitesse_y = 5
                    self.x = 500
                    self.y = 500
        else:
            self.x -= self.vitesse_x
            if self.x <= 110:
                self.direction_x = True
                if self.yg-195 <= self.y <= self.yg+195:
                    self.vitesse_y += 2
                else:
                    self.score[1] += 1
                    self.vitesse_y = 5
                    self.x = 500
                    self.y = 500

    def monter_raquette_gauche(self):
        if self.yg < 850:
            self.yg += self.vitesse_y*2

    def descendre_raquette_gauche(self):
        if self.yg > 150:
            self.yg -= self.vitesse_y*2

    def monter_raquette_droite(self):
        if self.yd < 850:
            self.yd += self.vitesse_y*2

    def descendre_raquette_droite(self):
        if self.yd > 150:
            self.yd -= self.vitesse_y*2

