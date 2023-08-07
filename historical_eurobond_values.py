from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
import csv
from pathlib import Path
from datetime import datetime

date = datetime.now().strftime("%d-%m-%Y")
# define target file to write into
dir_path = Path("./data/")
file_name = "isbank_eurobond_data_" + date + ".csv"
file_path = dir_path.joinpath(file_name)

# Create webdriver options and the driver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# Get the website
driver.get(
    "https://www.isbank.com.tr/fiyatoran/FiyatTabloGosterV2.asp?trkd=*EUB&amp;tip=HTML"
)


def append_data(rows, cols):
    for r in range(2, rows):
        row = []
        for p in range(1, cols):
            # obtaining the text from each column of the table
            row.append(find_item(r, p))
        data.append(row)


def find_item(i, j):
    return driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[" + str(i) + "]/td[" + str(j) + "]",).text


def find_num_of_cols():
    return len(driver.find_elements(By.XPATH, "/html/body/form/table/tbody/tr[1]/td"))


def find_num_of_rows():
    return len(driver.find_elements(By.XPATH, "/html/body/form/table/tbody/tr"))


header_row = []
for p in range(1, find_num_of_cols() - 1):
    header_row.append(find_item(1, p))

data = []
while True:
    try:
        wait(driver, 5).until(EC.element_to_be_clickable((By.NAME, "WSUB")))
        append_data(find_num_of_rows() - 1, find_num_of_cols() - 1)
        driver.find_element("name", "WSUB").click()
    except TimeoutException:
        break

# We are on the last page.
append_data(find_num_of_rows(), find_num_of_cols())

# Write into the csv file
with open(file_path, "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header_row)
    for row in data:
        csv_writer.writerow(row)
