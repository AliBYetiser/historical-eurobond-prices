#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
from pathlib import Path
from datetime import datetime
from selenium.webdriver.chrome.service import Service


def append_data(rows, cols):
    for r in range(1, rows):
        row = []
        for p in range(1, cols):
            # obtaining the text from each column of the table
            row.append(find_item(r, p))
        data.append(row)


def find_header(j):
    return driver.find_element(
        By.XPATH,
        "/html/body/form/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[6]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/table/thead/tr/th["
        + str(j)
        + "]",
    ).text.replace(",", ".")


def find_item(i, j):
    return driver.find_element(
        By.XPATH,
        "/html/body/form/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[6]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/table/tbody/tr["
        + str(i)
        + "]/td["
        + str(j)
        + "]",
    ).text.replace(",", ".")


def find_num_of_cols():
    return len(
        driver.find_elements(
            By.XPATH,
            "/html/body/form/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[6]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td",
        )
    )


def find_num_of_rows():
    return len(
        driver.find_elements(
            By.XPATH,
            "/html/body/form/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div[1]/div[6]/div/div[1]/div/div/div/div[1]/div/div/div/div/div[2]/div/table/tbody/tr",
        )
    )


# define target file to write into
dir_path = Path("./data/ziraatbank/")
date = datetime.now().strftime("%d-%m-%Y")
file_name = "ziraatbank_eurobond_" + date + ".csv"
file_path = dir_path.joinpath(file_name)

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
driver.get("https://www.ziraatbank.com.tr/tr/bireysel/yatirim/eurobond")
time.sleep(3)
driver.find_element("id", "accordion1").click()
time.sleep(2)


header_row = []
for p in range(1, find_num_of_cols() + 1):
    header_row.append(find_header(p))

data = []
append_data(find_num_of_rows() + 1, find_num_of_cols() + 1)

# Write into the csv file
with open(file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)
