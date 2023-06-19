# imports

import csv
import time
import datetime
from datetime import timedelta
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta

# create today date

date = datetime.datetime.now()
date2 = date2 = date.strftime("%d %b, %Y")

# lists

month_first_day = []
month_last_day = []
general_results = []

# saves

date6 = None

# read files from first and last month day

date3 = date.replace(day=1) - relativedelta(months=1)
date4 = date.replace(day=1) - datetime.timedelta(days=1)
str_date = date3.strftime("%d %b, %Y")
str_date2 = date4.strftime("%d %b, %Y")
day = int(str_date2.split()[0])
first_month_day = pd.read_csv(f"{str_date}.csv")
last_month_day = pd.read_csv(f"{str_date2}.csv")

print(date3) #check info
print(date4) #check info
print(first_month_day) #check info
print(last_month_day) #check info

# read info from file

month_first_day = first_month_day["Sales"].tolist()
month_last_day = last_month_day["Sales"].tolist()


# saving month stats

def save_month_stats():
    global month_first_day
    global month_last_day
    global general_results
    for month_stats in range(len(month_last_day)):
        result = month_last_day[month_stats] - month_first_day[month_stats]
        general_results.append(result)
    print(general_results) #check info


# checking for qual numbers of shops

def checking_shops():
    global month_first_day
    global day
    day2 = day - 1
    for x in range(2, day2):
        try:
            date5 = date.replace(day=x) - relativedelta(months=1)
            date6 = date5.strftime("%d %b, %Y")
            new_first_day = pd.read_csv(f"{date6}.csv")
            print(date6)
            month_first_day = new_first_day["Sales"].tolist()
            if len(month_last_day) == len(month_first_day):
                break
        except ValueError:
            continue
    save_month_stats()


# checking with what function starting

if len(month_last_day) == len(month_first_day):
    save_month_stats()
elif len(month_last_day) > len(month_first_day):
    checking_shops()

# read and save new file without sales per day

input_file = (f"{str_date2}.csv")
output_file = (f"{str_date2}monthstats.csv")
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

file = pd.read_csv(f"{str_date2}monthstats.csv")
file["Month Sales"] = general_results
file.to_csv(f"{date2}monthstats.csv", index = False, encoding='utf-8')

# info to mail sending

def info_mail_sending():
    global date6

    if date6 > date4:
        info_true = f"Statistics from {date6}"

    return info_true