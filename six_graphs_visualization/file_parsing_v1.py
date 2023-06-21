import pandas as pd
import math


def parse_file(path):
    df = pd.DataFrame(columns=['time', 'change_state_true', 'change_state_done', 'state_true', 'temp_true', 'temp_seeming'])

    with open(path, 'r') as file:
        for line in file:
            if 'time' in line:
                values = {}
                tokens = line.split()
                for token in tokens:
                    key, value = token.split('=')
                    values[key] = value
                if values['time'] in df['time'].values:
                    df.loc[df['time'] == values['time'], values.keys()] = values.values()
                else:
                    df = df.append(values, ignore_index=True)
    return df

def get_values_for_time(df, time_value):
    if str(time_value) in df['time'].values:
        row = df[df['time'] == str(time_value)]
        required_values = row.iloc[0].to_dict()
        return required_values
    else:
        return None


# df = pd.DataFrame(columns=['time', 'change_state_true', 'change_state_done', 'state_true', 'temp_true', 'temp_seeming'])
# df = parse_file(df)
# print(df)
