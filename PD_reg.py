import pandas as pd




def load_data(file_pathF3):
    with open(file_pathF3, 'r') as f:
        line = f.readline()
        while line:
            data = line.split(',')
            regulation_time = float(data[0])
            min_temperature = float(data[2])
            max_temperature = float(data[3])
            return regulation_time, min_temperature, max_temperature


def load_temperatures(file_pathF5):
    df = pd.read_excel(file_pathF5, header=0)
    temperatures = df[1].values.tolist()
    return temperatures

def pd_regulator(current_temperature, desired_temperature, prev_error, prev_temperature, Kp, Kd, interval):
    error = desired_temperature - current_temperature
    error_derivative = (error - prev_error) / interval
    control_signal = Kp * error + Kd * error_derivative
    prev_error = error
    prev_temperature = current_temperature
    return control_signal, prev_error, prev_temperature


def process_temperatures(file_path, file_pathF3, F6_file_path, Kp, Kd):
    regulation_time, min_temp, max_temp = load_data(file_pathF3)
    temperatures = load_temperatures(file_path)
    prev_error = max_temp - temperatures[0]
    prev_temperature = temperatures[0]
    time = 0
    with open(F6_file_path, 'w') as f:
        for i, temperature in enumerate(temperatures):
            time += 1
            if time >= regulation_time:
                desired_temperature = min_temp
            else:
                desired_temperature = max_temp
            control_signal, prev_error, prev_temperature = pd_regulator(
                temperature, desired_temperature, prev_error, prev_temperature, Kp, Kd, time)
            if control_signal > 0:
                f.write('1 %d\n' % (i * time))


process_temperatures('data/F5.xlsx', 'data/F3.txt', 'data/F6.txt', 0.5, 0.5)
