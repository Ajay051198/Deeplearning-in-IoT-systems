# Data-preprocessing steps to prepare data for DL models

# imports
import config
import os
import re
import numpy as np
from keras.preprocessing import sequence
from datetime import datetime
from tqdm import tqdm

categorizeActivites = {
    'cairo': {
        "": "Other",
        "Bed to toilet": "Use Toiltet",
        "R1 wake": "Wake",
        "R2 wake": "Wake",
        "Night wandering": "Other",
        "R1 work in office": "Work",
        "Laundry": "Work",
        "R2 take medicine": "Take_medicine",
        "R1 sleep": "Sleep",
        "R2 sleep": "Sleep",
        "Leave home": "Leave_Home",
        "Breakfast": "Eat",
        "Dinner": "Eat",
        "Lunch": "Eat",
    },
    "milan": {
        "": "Other",
        "Master_Bedroom_Activity": "Master",
        "Meditate": "Meditate",
        "Chores": "Work",
        "Desk_Activity": "Work",
        "Morning_Meds": "Take_medicine",
        "Eve_Meds": "Take_medicine",
        "Sleep": "Sleep",
        "Read": "Read",
        "Watch_TV": "Watch_TV",
        "Leave_Home": "Leave_Home",
        "Dining_Rm_Activity": "Eat",
        "Kitchen_Activity": "Cook",
        "Bed_to_Toilet": "Use Toilet",
        "Master_Bathroom": "Master_Bath_use",
        "Guest_Bathroom": "Guest_Bath_use"},

    "kyoto7": {
        "R1_Bed_to_Toilet": "Use Toilet",
        "R2_Bed_to_Toilet": "Use Toilet",
        "Meal_Preparation": "Cook",
        "R1_Personal_Hygiene": "Personal_hygiene",
        "R2_Personal_Hygiene": "Personal_hygiene",
        "Watch_TV": "Watch TV",
        "R1_Sleep": "Sleep",
        "R2_Sleep": "Sleep",
        "Clean": "Other",
        "R1_Work": "Work",
        "R2_Work": "Work",
        "Study": "Study",
        "Wash_Bathtub": "Other",
        "": "Other"},
}


def load_data(filename):
    timestamps = []
    sensors = []
    values = []
    activities = []

    activity = ''

    print('Loading File ...')
    with open(filename, 'rb') as file:
        data = file.readlines()
        for i, line in tqdm(enumerate(data), total=len(data)):
            sample = line.decode().split()
            try:
                if 'M' == sample[2][0] or 'D' == sample[2][0] or 'T' == sample[2][0]:
                    # choose only M D T sensors, avoiding unexpected errors
                    if not ('.' in str(np.array(sample[0])) + str(np.array(sample[1]))):
                        sample[1] = sample[1] + '.000000'
                    timestamps.append(datetime.strptime(str(np.array(sample[0])) + str(np.array(sample[1])),
                                                        "%Y-%m-%d%H:%M:%S.%f"))
                    sensors.append(str(np.array(sample[2])))
                    values.append(str(np.array(sample[3])))

                    if len(sample) == 4:  # if activity does not exist
                        activities.append(activity)
                    else:  # if activity exists
                        des = str(' '.join(np.array(sample[4:])))
                        if 'begin' in des:
                            activity = re.sub('begin', '', des)
                            activity = activity.rstrip()
                            activities.append(activity)
                        if 'end' in des:
                            activities.append(activity)
                            activity = ''
            except IndexError:
                print(i, line)
    file.close()

    # unique values of temperature
    temperature = []
    for element in values:
        try:
            temperature.append(float(element))
        except ValueError:
            pass

    # unique sensors
    sensorList = sorted(set(sensors))

    # mapping sensor activations
    obs2idx = {}
    count = 0

    print('Preprocessing ..')

    for key in tqdm(sensorList, total=len(sensorList)):
        if "M" or "AD" in key:
            obs2idx[key + "OFF"] = count
            count += 1
            obs2idx[key + "ON"] = count
            count += 1
        if "D" in key:
            obs2idx[key + "CLOSE"] = count
            count += 1
            obs2idx[key + "OPEN"] = count
            count += 1
        if "T" in key:
            for temp in range(0, int((max(temperature) - min(temperature)) * 2) + 1):
                obs2idx[key + str(float(temp / 2.0) +
                                  min(temperature))] = count + temp

    idx2obs = [x for x in obs2idx.keys()]

    catActivies = [categorizeActivites[filename.split(
        '/')[-1]][i] for i in activities]

    idx2act = sorted(set(catActivies))
    act2idx = {a: i for i, a in enumerate(idx2act)}

    Xi = []
    Yi = []

    for _entry, sensor in tqdm(enumerate(sensors), total=len(sensors)):
        if "T" in sensor:
            Xi.append(obs2idx[sensor + str(round(float(values[_entry]), 1))])
        else:
            Xi.append(obs2idx[sensor + str(values[_entry])])
        Yi.append(act2idx[catActivies[_entry]])

    series = Xi
    X = []
    Y = []

    for i, y in tqdm(enumerate(Yi), total=len(Yi)):
        if i == 0:
            Y.append(y)
            x = [Xi[i]]
        if i > 0:
            if y == Yi[i - 1]:
                x.append(Xi[i])
            else:
                Y.append(y)
                X.append(x)
                x = [Xi[i]]
        if i == len(Yi) - 1:
            if y != Yi[i - 1]:
                Y.append(y)
            X.append(x)

    return X, Y, (idx2act, idx2obs, act2idx, obs2idx), series


if __name__ == "__main__":
    print('Preparing data')
    name = input('Enter dataset name: ')
    file = f"./Data/{name}"
    print(f"File >> {file}")

    X, Y, enc_dec, series = load_data(file)
    print('Saving file')
    # convert to numpy arrays
    X = np.array(X, dtype=object)
    Y = np.array(Y, dtype=object)
    enc_dec = np.array(enc_dec, dtype=object)
    series = np.array(series, dtype=object)
    X = sequence.pad_sequences(X, maxlen=config.MAX_LEN, dtype=np.int32)

    save_to = f"./PP_Data/{file.split('/')[-1]}"

    np.save(save_to + '_X.npy', X)
    np.save(save_to + '_Y.npy', Y)
    np.save(save_to + '_ENCDEC.npy', enc_dec)
    np.save(save_to + '_series.npy', series)

    print('done')
