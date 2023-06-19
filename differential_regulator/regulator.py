class DifferentialRegulator:
    COEFFICIENT = 0.1

    def __init__(self, temp_max, temp_min, time0=0, temp0=0, time1=None, temp1=None):
        """
        :param time0: time of the begining
        :param temp0: temperature of the begining
        :param time1: time of the end
        :param temp1: temperature of the end
        """
        self.temp_delta = temp_max - temp_min
        self.temp1 = temp1
        self.temp0 = temp0
        self.time1 = time1
        self.time0 = time0

    def derivative(self):
        """
        calculate derivative of the given process
        :return: derivative of the given process dT / dt
        """
        return (self.temp1 - self.temp0) / (self.time1 - self.time0)

    def regulate(self):
        """
        the raising time should be bigget tha the dt by the ten times
        it defines by the COEFFICIENT from the defintions
        :return: the 0 if everything is OK, 1 if refrigerator must be switched on
        """
        if abs(self.derivative()) > self.COEFFICIENT * self.temp_delta / (self.time1 - self.time0):
            return 1
        else:
            return 0

if __name__ == "__main__":
    # пример вызова:
    regulator = DifferentialRegulator(100, 90)
    regulator.time0 = 0.00036331844427417437;
    regulator.temp0 = 300.18165921814057
    regulator.time1 = 0.0007488687355783341;
    regulator.temp1 = 300.37443433279174
    print(regulator.regulate())