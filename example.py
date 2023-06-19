from differential_regulator.regulator import DifferentialRegulator

if __name__ == "__main__":
    # пример вызова:
    regulator = DifferentialRegulator(100, 90)
    regulator.time0 = 0.00036331844427417437;
    regulator.temp0 = 300.18165921814057
    regulator.time1 = 0.0007488687355783341;
    regulator.temp1 = 300.37443433279174
    print(regulator.regulate())