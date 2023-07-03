# imports

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import sqlalchemy
import os
import datetime
from datetime import timedelta
import csv
import string


# initializations

s = Service(r"C:/Users/voisk/Documents/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service = s)
#chrome_driver_path = "C:/Users/voisk/Documents/chromedriver/chromedriver.exe"
#driver = webdriver.Chrome(executable_path=chrome_driver_path)

# maximize window

driver.maximize_window()

# lists

sales = []
shop_name = []

# functions, extract info from site

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


def get_info_sales(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        div_element = soup.find("div", {"class": "wt-pt-xs-3"})
        text_content = div_element.text
        text_filter = text_content.replace("Sales", "")
        text_filter_to_int = int(text_filter)
        sales.append(text_filter_to_int)
    except: 
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            div_element = soup.find("span", {"class": "wt-text-caption wt-no-wrap"})
            text_content = div_element.text
            text_filter = text_content.replace("Sales", "")
            text_filter2 = text_filter.replace(",", "")
            text_filter_to_int = int(text_filter2)
            sales.append(text_filter_to_int)
        except:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                div_element = soup.find("h2", {"class": "wt-text-body-01 wt-pb-xs-4"})
                text_content = div_element.text
                text_filter = text_content.replace("Sorry, the page you were looking for was not found.", "")
                text_filter2 = 0
                sales.append(text_filter2)
            except:
                print("Unknown error from 'get_info_sales'.")


def get_info_shop_name(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        div_element = soup.find("h1", {"class": "wt-text-heading-01 wt-text-truncate"})
        text_content = div_element.text
        shop_name.append(text_content)
    except:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            div_element = soup.find("h2", {"class": "wt-text-body-01 wt-pb-xs-4"})
            text_content = div_element.text
            text_content = "Deleted"
            shop_name.append(text_content)
        except:
            print("Unknown error from 'get_info_shop_name'.")


# store url 507/507 (update here)

get_info_sales("https://www.etsy.com/shop/unidragonpuzzle?ref=l2-about-shopname")
get_info_shop_name("https://www.etsy.com/shop/unidragonpuzzle?ref=l2-about-shopname")
get_info_sales("https://www.etsy.com/shop/GretaOtoDesign?ref=simple-shop-header-name&listing_id=733759013")
get_info_shop_name("https://www.etsy.com/shop/GretaOtoDesign?ref=simple-shop-header-name&listing_id=733759013")
get_info_sales("https://www.etsy.com/shop/DepleeStore?ref=simple-shop-header-name&listing_id=1370824318")
get_info_shop_name("https://www.etsy.com/shop/DepleeStore?ref=simple-shop-header-name&listing_id=1370824318")
get_info_sales("https://www.etsy.com/shop/OakyLux?ref=simple-shop-header-name&listing_id=1045446537")
get_info_shop_name("https://www.etsy.com/shop/OakyLux?ref=simple-shop-header-name&listing_id=1045446537")
get_info_sales("https://www.etsy.com/shop/personalizedgiftbox?ref=simple-shop-header-name&listing_id=640786982")
get_info_shop_name("https://www.etsy.com/shop/personalizedgiftbox?ref=simple-shop-header-name&listing_id=640786982")
get_info_sales("https://www.etsy.com/shop/DukhaWallArt?ref=shop-header-name&listing_id=857423510")
get_info_shop_name("https://www.etsy.com/shop/DukhaWallArt?ref=shop-header-name&listing_id=857423510")
get_info_sales("https://www.etsy.com/shop/HUNmadeStore?ref=l2-about-shopname")
get_info_shop_name("https://www.etsy.com/shop/HUNmadeStore?ref=l2-about-shopname")
get_info_sales("https://www.etsy.com/shop/DayspringPens?ref=l2-about-shopname")
get_info_shop_name("https://www.etsy.com/shop/DayspringPens?ref=l2-about-shopname")
get_info_sales("https://www.etsy.com/shop/AlysaJewelryShop?ref=l2-about-shopname")
get_info_shop_name("https://www.etsy.com/shop/AlysaJewelryShop?ref=l2-about-shopname")


# agree cookies

agree = driver.find_element("xpath", '//button[@class="wt-btn wt-btn--filled wt-mb-xs-0"]')
try:
    agree.click()
except:
    pass

print("Today sales:", sales) # view info
print("Shop names:", shop_name) # view info

# saving file

file = pd.DataFrame()
date = datetime.datetime.now()
date2 = date.strftime("%d %b, %Y")
file.to_csv(f"{date2}.csv", index = False, encoding='utf-8')

# info to file

header = ["Shop name", "Sales", "Sales per day"]
data = []

with open(f"{date2}.csv", "w", encoding = "utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)


def write_info_to_file():
    data.clear()
    data.append(shop_name[0])
    data.append(sales[0])
    shop_name.pop(0)
    sales.pop(0)
    with open(f"{date2}.csv", "a", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(data)
        

# starting def write info to file

deleting = 0
while deleting < len(sales):
   write_info_to_file()

# day statistics

day_file = pd.read_csv(f"{date2}.csv")

day_sales_list = day_file.Sales

sales_from_day = []

for day_sale in day_sales_list:
    sales_from_day.append(day_sale)

# one day sales

general_sales_stats = []

# creating yesterday date

date3 = date - timedelta(days = 1)
date4 = date3.strftime("%d %b, %Y")
data_from_yesterday = pd.read_csv(f"{date4}.csv")

# saving yesterday sales to list

yesterday_list = []
yesterday_list = data_from_yesterday["Sales"].to_list()

# saving sales statistic to list

for day_results in range(len(sales_from_day)):
    general_results = sales_from_day[day_results] - yesterday_list[day_results]
    general_sales_stats.append(general_results)

print("Sales differents:", general_sales_stats) # view info
print("Yesterday sales:", yesterday_list) # view info

# add new list with day sales to file

day_file["Sales per day"] = general_sales_stats

# finish saving

day_file.to_csv(f"{date2}.csv", index = False, encoding='utf-8')
