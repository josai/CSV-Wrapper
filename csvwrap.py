import datetime
import os
import csv
import time

def write_csv(directory, filename, data, save_type):
    here = os.path.dirname(os.path.realpath(__file__))
    filename = (filename + '.csv')
    filename = filename.replace(' ', '_')

    full = here + directory + filename
    keys = []
    for key in data[0]:
        keys.append(key)
    real_file = os.path.exists(full)
    try:
        with open(full, save_type, encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            if (save_type == 'w') or (not real_file):
                writer.writeheader()
            for i in data:
                writer.writerow(i)
    except:
        os.makedirs(here + directory)
        with open(full, save_type, encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            for i in data:
                writer.writerow(i)

def read_csv(directory, filename):
    here = os.path.dirname(os.path.realpath(__file__))
    filename = filename.replace('.csv', '')
    filename = filename + '.csv'
    full = here + directory + filename
    listed = []
    with open(full, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i in reader:
            if len(i) > 0:
                listed.append(i)
    return (listed)

def unique_data(directory, filename):
    data = read_csv(directory, filename)
    unique_list = []
    for i in data:
        if i not in unique_list:
            unique_list.append(i)
    write_csv(directory, filename, unique_list, 'w')

def convert_time(string):
    string = string.replace('-', ' ')
    string = string.replace(':', ' ')
    s = string.split()
    s = [ int(x) for x in s ]
    date = datetime.datetime(s[0], s[1], s[2], s[3], s[4], s[5], 000000)
    return (date)

