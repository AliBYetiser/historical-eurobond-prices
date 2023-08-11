#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import time
from pathlib import Path
from datetime import datetime
from selenium.webdriver.chrome.service import Service
import os
import sys
from pyvirtualdisplay import Display


display = Display(visible=0, size=(1024, 768))
display.start()


def append_data(rows, cols):
    for r in range(2, rows):
        row = []
        for p in range(2, cols):
            # obtaining the text from each column of the table
            row.append(find_item(r, p))
        data.append(row)


def find_item(i, j):
    return driver.find_element(
        By.XPATH,
        "/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr["
        + str(i)
        + "]/td["
        + str(j)
        + "]",
    ).text.replace(",", ".")


# define target file to write into
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
dir_path = Path(script_directory).joinpath(Path("./data/vakifbank/"))
date = datetime.now().strftime("%d-%m-%Y")
file_name_buy = "vakifbank(buy)_eurobond_" + date + ".csv"
file_name_sell = "vakifbank(sell)_eurobond_" + date + ".csv"
file_path_buy = dir_path.joinpath(file_name_buy)
file_path_sell = dir_path.joinpath(file_name_sell)

service = Service() # Service(executable_path=r"/usr/bin/chromedriver")
options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
options.add_argument("user-agent={0}".format(user_agent))
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)
# Get the website
driver.implicitly_wait(10)
driver.get(
    "https://www.vakifbank.com.tr/tahvil-bono-eurobond-hesaplama-araci.aspx?pageID=2378"
)
driver.implicitly_wait(10)
select = Select(driver.find_element(By.NAME, "ctl00$ctl10$ctl00$ddlTahvilBonoUrun"))
select.select_by_value('2')
driver.implicitly_wait(10)
select_action = Select(driver.find_element(By.NAME, "ctl00$ctl10$ctl00$ddlTahvilIslemTipi"))
select_action.select_by_value('1')
driver.implicitly_wait(10)

cols = len(driver.find_elements(By.XPATH,"/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr[1]/td"))+1
rows = len(driver.find_elements(By.XPATH,"/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr"))+1
header_row = []
for p in range(2, cols):
    header_row.append(find_item(1, p))

data = []
print("num of cols: " + str(cols))
print("num of rows: " + str(rows))
append_data(rows, cols)
time.sleep(1)
# Write into the csv file
with open(file_path_buy, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)

driver.implicitly_wait(10)
select_name = Select(driver.find_element(By.NAME, "ctl00$ctl10$ctl00$ddlTahvilIslemTipi"))
select_name.select_by_value('2')
driver.implicitly_wait(10)
data = []
rows = len(driver.find_elements(By.XPATH,"/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr"))+1
print("sell rows: " +str(rows))

append_data(rows, cols)
time.sleep(1)

# Write into the csv file
with open(file_path_sell, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)

