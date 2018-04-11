

# write a class TempTracker with these methods:
    # insert, get_max, get_min, get_mean, get_mode

# optimize for space and time, favor speeding up the 'getter' methods (ie get_max, get_min, get_mean, get_mode)
# over the insert method fahrenheit

class TempTracker(object):

    def __init__(self):
        # mode
        self.occurences = [0] * 111
        self.max_occurences = 0
        self.mode = None

        # mean
        self.number_of_readings = 0
        self.total_sum = 0.0
        self.mean = None

        # min & max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

        # historical temps
        self.historical_temps = []

    def insert(self, temperature):
        # mode
        self.occurences[temperature] += 1
        self.historical_temps.append(temperature)
        if self.occurences[temperature] > self.max_occurences:
            self.mode = temperature
            self.max_occurences = self.occurences[temperature]


        # mean
        self.number_of_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.number_of_readings

        # min and max
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode



temp = TempTracker()

temp.insert(60)
temp.insert(80)
print temp.historical_temps