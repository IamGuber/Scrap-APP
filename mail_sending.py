# imports

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import pandas as pd
import time
import schedule


def send_email(file_path, subject, message, from_email, password, to_email):

    # create message

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # attach message

    msg.attach(MIMEText(message, 'plain'))
    
    # open and read the file in binary mode

    with open(file_path, 'rb') as attachment:
        mime_base = MIMEBase('application', 'octet-stream')
        mime_base.set_payload((attachment).read())
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', "attachment; filename= {}".format(file_path))
        msg.attach(mime_base)
        
    # create SMTP session

    smtp_session = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_session.starttls()
    
    # login with email,password sending and terminate

    smtp_session.login(from_email, password)
    text = msg.as_string()
    smtp_session.sendmail(from_email, to_email, text)
    smtp_session.quit()

# datetime for file name

date = datetime.datetime.now()
date2 = date.strftime("%d %b, %Y")
print(date2) # checking

# read file

date = datetime.datetime.now()
date2 = date.strftime("%d %b, %Y")

file = pd.read_csv(f"{date2}.csv")

# sorting and save by top sales 

file['Sales per day'] = pd.to_numeric(file['Sales per day'], errors = 'coerce')
file.sort_values(["Sales per day", "Shop name"], axis = 0, ascending = [False, True], inplace=True, na_position='first')
file.to_csv(f"{date2}(sorted).csv", index = False, encoding='utf-8')

# sending mail

send_email(f'{date2}(sorted).csv', 'ETSY SALES', 'etsy sales', 'scrapstatistics@gmail.com', 'zzdqjdfzkyqfuaap', 'domolazeriai@gmail.com')


# def schedule for sending weekly email

def send_weekly_email():

    # import .py file

    import week_stats

    # get current date

    date = datetime.datetime.now()
    date2 = date.strftime("%d %b, %Y")

    # read the file sorting and saving

    file2 = pd.read_csv(f"{date2}weekstats.csv")
    file2['Week Sales'] = pd.to_numeric(file2['Week Sales'], errors='coerce')
    file2.sort_values(["Week Sales", "Shop name"], axis = 0, ascending = [False, True], inplace = True, na_position = 'first')
    file2.to_csv(f"{date2}(sortedWeekStats).csv", index = False, encoding = 'utf-8')

    # sending mail

    info_from_week = week_stats.info_mail_sending()
    send_email(f'{date2}(sortedWeekStats).csv', 'ETSY SALES-weekstatistics', f'etsy sales-weekstatistics\n{info_from_week}', 'scrapstatistics@gmail.com', 'zzdqjdfzkyqfuaap', 'domolazeriai@gmail.com')


# schedule the email to be sent every Monday at 9:00 AM

schedule.every().monday.at("09:00").do(send_weekly_email)


def send_monthly_email():

    # import .py file

    import monthly_stats

    # get current date

    date = datetime.datetime.now()
    date2 = date.strftime("%d %b, %Y")

    # read the file sorting and saving

    file3 = pd.read_csv(f"{date2}monthstats.csv")
    file3['Month Sales'] = pd.to_numeric(file3['Month Sales'], errors='coerce')
    file3.sort_values(["Month Sales", "Shop name"], axis = 0, ascending = [False, True], inplace = True, na_position = 'first')
    file3.to_csv(f"{date2}(SortedMonthStats).csv", index = False, encoding = 'utf-8')

    # sending mail

    info_from_month = monthly_stats.info_mail_sending()
    send_email(f'{date2}(SortedMonthStats).csv', 'ETSY SALES-monthlystatistics', f'etsy sales-monthlystatistics\n{info_from_month}', 'scrapstatistics@gmail.com', 'zzdqjdfzkyqfuaap', 'domolazeriai@gmail.com')


# schedule the email to be sent every first month day

schedule.every().day.at("09:00").do(send_monthly_email)

# keep the script running to execute scheduled tasks

while True:
    schedule.run_pending()
    time.sleep(1)
