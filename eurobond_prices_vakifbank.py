#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import time
from pathlib import Path
from datetime import datetime
from selenium.webdriver.chrome.service import Service


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


def find_num_of_cols():
    return len(
        driver.find_elements(
            By.XPATH,
            "/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr[1]/td",
        )
    )


def find_num_of_rows():
    return len(
        driver.find_elements(
            By.XPATH,
            "/html/body/form/div[5]/div[3]/div/div[1]/div/div[1]/div/div[2]/table/tbody/tr",
        )
    )


# define target file to write into
dir_path = Path("./data/vakifbank/")
date = datetime.now().strftime("%d-%m-%Y")
file_name_buy = "vakifbank(buy)_eurobond_" + date + ".csv"
file_name_sell = "vakifbank(sell)_eurobond_" + date + ".csv"
file_path_buy = dir_path.joinpath(file_name_buy)
file_path_sell = dir_path.joinpath(file_name_sell)

service = Service(executable_path=r"/usr/bin/chromedriver")
options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"
options.add_argument("user-agent={0}".format(user_agent))
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=service, options=options)
# Get the website
driver.get(
    "https://www.vakifbank.com.tr/tahvil-bono-eurobond-hesaplama-araci.aspx?pageID=2378"
)
select_name = Select(driver.find_element("id", "ctl00_ctl10_ctl00_ddlTahvilBonoUrun"))
time.sleep(3)
select_name.select_by_value("2")
time.sleep(3)
select_action = Select(
    driver.find_element("id", "ctl00_ctl10_ctl00_ddlTahvilIslemTipi")
)
select_action.select_by_value("1")
time.sleep(3)

header_row = []
for p in range(2, find_num_of_cols() + 1):
    header_row.append(find_item(1, p))

data = []
append_data(find_num_of_rows() + 1, find_num_of_cols() + 1)

# Write into the csv file
with open(file_path_buy, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)


driver.get(
    "https://www.vakifbank.com.tr/tahvil-bono-eurobond-hesaplama-araci.aspx?pageID=2378"
)
select_name = Select(driver.find_element("id", "ctl00_ctl10_ctl00_ddlTahvilBonoUrun"))
time.sleep(3)
select_name.select_by_value("2")
time.sleep(3)
select_action = Select(
    driver.find_element("id", "ctl00_ctl10_ctl00_ddlTahvilIslemTipi")
)
select_action.select_by_value("2")
time.sleep(3)

header_row = []
for p in range(2, find_num_of_cols() + 1):
    header_row.append(find_item(1, p))

data = []
append_data(find_num_of_rows() + 1, find_num_of_cols() + 1)


# Write into the csv file
with open(file_path_sell, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)
