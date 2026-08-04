from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Launch Chrome
driver = webdriver.Chrome()

# Open Website
driver.get("https://docs.cyberark.com/pam-self-hosted/10.10/en/content/pas%20inst/endoflifepolicy.htm")


# Wait for page to load
time.sleep(5)

# Locate the first table using XPath
table = driver.find_element(By.XPATH, "//table")

# Get all rows
rows = table.find_elements(By.XPATH, ".//tr")

data = []

for row in rows:

    columns = row.find_elements(By.XPATH, "./th | ./td")

    row_data = [column.text for column in columns]

    data.append(row_data)

# Convert into DataFrame
df = pd.DataFrame(data)

print(df)

# Save CSV
df.to_csv("CyberArk_EOL_Table.csv", index=False, header=False)

print("Table Saved Successfully!")

driver.quit()