# imports

import csv
import time
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np


# create today date

date = datetime.datetime.now()
date2 = date2 = date.strftime("%d %b, %Y")

# lists

week_first_day = []
week_last_day = []
general_results = []

# saves

date6 = None

# read files from first and last week day

date3 = date - timedelta(days = 7)
date4 = date3.strftime("%d %b, %Y")
first_week_day = pd.read_csv(f"{date4}.csv")
last_week_day = pd.read_csv(f"{date2}.csv")

print(first_week_day) # checking info
print(last_week_day) # checking info

# read info from file

week_first_day = first_week_day["Sales"].tolist()
week_last_day = last_week_day["Sales"].tolist()


# saving week stats

def save_week_stats():
    global week_first_day
    global week_last_day
    global general_results
    for week_stats in range(len(week_last_day)):
        result = week_last_day[week_stats] - week_first_day[week_stats]
        general_results.append(result)


# checking for equal numbers of shops

def checking_shops():
    global week_first_day
    global date6
    for x in range(-6, 0):
        try:
            y = abs(x)
            date5 = date - timedelta(days = y)
            date6 = date5.strftime("%d %b, %Y")
            new_first_day = pd.read_csv(f"{date6}.csv")
            week_first_day = new_first_day["Sales"].tolist()
            if len(week_last_day) == len(week_first_day):
                break
        except ValueError:
            continue
    save_week_stats()


# checking with what function starting

if len(week_last_day) == len(week_first_day):
    save_week_stats()
elif len(week_last_day) > len(week_first_day):
    checking_shops()

print(first_week_day) # checking info
print(last_week_day) # checking info

# read and save new file without sales per day

input_file = (f"{date2}.csv")
output_file = (f"{date2}weekstats.csv")
column_index = 2  

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in rows:
        del row[column_index]
        writer.writerow(row)

# adding new info and saving file

file = pd.read_csv(f"{date2}weekstats.csv")
file["Week Sales"] = general_results
file.to_csv(f"{date2}weekstats.csv", index = False, encoding='utf-8')

# info to mail sending

def info_mail_sending():
    global date6

    if date6 > date4:
        info_true = f"Statistics from {date6}"

    return info_true