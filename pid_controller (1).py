# -*- coding: utf-8 -*-
"""PID controller.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s5wSWkhfPlb3O5f_bc3UBNEFRd0tB2f6
"""

class PIDController:
    def __init__(self, Kp=0.33, Ki=0.33, Kd=0.33):
        self.Kp = Kp        # значение по умолчанию у всех весов 0.33
        self.Ki = Ki
        self.Kd = Kd

    def update(self, T_max, T_min, measurements, dt, n):

        integral = sum(measurements) / len(measurements)          # среднее значение температур
        derivative = (measurements[-1] - measurements[-2]) / dt   # производная температуры
        T_lim = (T_max-T_min) / (n*dt)                            # T_lim = (T_max - T_min) / (n*dt) , где n - количество периодов

        pr_max = self.Kp * measurements[-1] / T_max # должна быть < 1 * Kp
        i_max = self.Ki * integral / T_max  # должна быть < 1 * Ki
        d_max = self.Kd * derivative / T_lim  # должна быть < 1 * Kd

        pr_min = self.Kp * measurements[-1] / T_min # должна быть > 1 * Kp
        i_min = self.Ki * integral / T_min  # должна быть > 1 * Ki
        d_min = -self.Kd * derivative / T_lim # должна быть < 1 * Kd

        if (pr_max < 1 * self.Kp  and i_max < 1 * self.Ki and d_max < 1 * self.Kd and pr_min > 1 * self.Kp and i_min > 1 * self.Ki and d_min < 1 * self.Kd):
          return False           #ничего не меняем
        else:
          return True            #меняем значение на 1

import datetime

file_path_f3 = "F3.txt"

# файл F3 - файл с параметрами задачи
# пример файла F3:
#1.0,33,100,90,00,00
# соответствуют параметрам задачи dt(float),dt(int),Tmax,Tmin,tнаг,tубыв

with open(file_path_f3, "r") as file:
    line = file.readline().strip()  # Read the first line and remove leading/trailing whitespace

    values = line.split(",")  # Split the line by commas

    dt = float(values[0])
    T_max = float(values[2])
    T_min = float(values[3])


file_path_f5 = "F5.txt"

# файл F5 - файл с значениями температур
# пример файла F5.txt:
#datetime;Temperature
#2020-03-01 15:44:06;92.2562
#2020-03-01 15:44:07;92.0144
#2020-03-01 15:44:08;92.2413

temperature_values = []
with open(file_path_f5, "r") as file:
    next(file)  # Skip the header line

    for line in file:
        date, temperature = line.strip().split(";")
        temperature = float(temperature)
        temperature_values.append(temperature)

#print(temperature_values[-10:])
pid = PIDController()
res = pid.update(T_max,T_min, temperature_values, dt, 10 )
dt_now = datetime.datetime.now()
if (res == True):
  with open("F6.txt", "a") as myfile:
    # файл F6 - файл записи
    # пример файла F6.txt:
    #06.19.2023 07:09:41.537742; 1
    myfile.write(str(dt_now.strftime('%m.%d.%Y %H:%M:%S.%f')) + "; 1 "+ "\n")