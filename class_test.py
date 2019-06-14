


class Car:

    wheels = 4

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        self._voltage = 12


    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, volts):
        print("Warning: this can cause problems!")
        self._voltage = volts

    @voltage.deleter
    def voltage(self):
        print("Warning: the radio will stop working!")
        del self._voltage
