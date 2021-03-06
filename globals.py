__author__ = "reza0310"

def initialize():
    global IP, PORT, HEADER_LENGTH, images, hud, jeu, FPS, separateur, mode, orientation, longueur_dev, largeur_dev
    from framework import HUD
    from PONG import Coeur
    IP = "127.0.0.1"
    PORT = 9999
    HEADER_LENGTH = 10
    FPS = 10
    separateur = "/"
    images = {"textinput": "data"+separateur+"input.png",
              "sprite": "data"+separateur+"sprite.png",
              "fond": "data"+separateur+"noir.jpg"}
    hud = HUD()
    jeu = Coeur()
    mode = "DEV"
    longueur_dev = 1334
    largeur_dev = 750
    orientation = "paysage"
