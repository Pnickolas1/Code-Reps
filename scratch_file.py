

class Starship(object):

    sound = "Vrrrrrrrrrrrrrrrrrrrrr"

    def __init__(self):
        self.engines = False
        self.engine_speed = 0
        self.shields = True

    def engage(self):
        self.engines = True

    def warp(self, factor):
        self.engine_speed = 2
        self.engine_speed *= factor

    @classmethod
    def make_sound(cls):
        print(cls.sound)

    @staticmethod
    def beep():
        print("Beep boop beep")

use_enterprise = Starship()
use_enterprise.make_sound()
Starship.make_sound()

