from graphics_and_games_klassen import *


class Ampel(EREIGNISBEHANDLUNG):
    def __init__(self):
        super().__init__()
        self.ampel = RECHTECK(100, 200, 0, 150, 500, "schwarz")
        self.rotes_licht = KREIS(175, 300, 50, 0, "rot")
        self.gelbes_licht = KREIS(175, 450, 50, 0, "gelb")
        self.gruenes_licht = KREIS(175, 600, 50, 0, "grün")
        self.ampeltimer = 0

    def rot(self):
        self.rotes_licht.FarbeSetzen("rot")
        self.gelbes_licht.FarbeSetzen("schwarz")
        self.gruenes_licht.FarbeSetzen("schwarz")

    def rot_gelb(self):
        self.rotes_licht.FarbeSetzen("rot")
        self.gelbes_licht.FarbeSetzen("gelb")
        self.gruenes_licht.FarbeSetzen("schwarz")

    def gelb(self):
        self.rotes_licht.FarbeSetzen("schwarz")
        self.gelbes_licht.FarbeSetzen("gelb")
        self.gruenes_licht.FarbeSetzen("schwarz")

    def gruen(self):
        self.rotes_licht.FarbeSetzen("schwarz")
        self.gelbes_licht.FarbeSetzen("schwarz")
        self.gruenes_licht.FarbeSetzen("grün")

    def AktionAusfuehren(self):
        self.ampeltimer += 1
        if self.ampeltimer  == 1:
            self.rot()
        elif self.ampeltimer == 150:
            self.rot_gelb()
        elif self.ampeltimer == 200:
            self.gruen()
        elif self.ampeltimer == 300:
            self.gelb()
        else:
            if self.ampeltimer > 350:
                self.ampeltimer = 0

    def TasteGedrueckt(self, taste):
        if taste == "w":
            self.ampel.Verschieben(0, -2)
            self.rotes_licht.Verschieben(0, -2)
            self.gelbes_licht.Verschieben(0, -2)
            self.gruenes_licht.Verschieben(0, -2)
        elif taste == "s":
            self.ampel.Verschieben(0, 2)
            self.rotes_licht.Verschieben(0, 2)
            self.gelbes_licht.Verschieben(0, 2)
            self.gruenes_licht.Verschieben(0, 2)
        elif taste == "a":
            self.ampel.Verschieben(-2, 0)
            self.rotes_licht.Verschieben(-2, 0)
            self.gelbes_licht.Verschieben(-2, 0)
            self.gruenes_licht.Verschieben(-2, 0)
        elif taste == "d":
            self.ampel.Verschieben(2, 0)
            self.rotes_licht.Verschieben(2, 0)
            self.gelbes_licht.Verschieben(2, 0)
            self.gruenes_licht.Verschieben(2, 0)
        self.gelbes_licht.H


I = Ampel()
I.Starten()
I.TaktdauerSetzen(0.01)
