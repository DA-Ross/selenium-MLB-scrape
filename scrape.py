import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from datetime import date
import time


url = "https://swishanalytics.com/optimus/mlb/batter-vs-pitcher-stats?date=" + str(date.today())

# Setup ChromeDriver using webdriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get(url)

    # Wait for the table to be present
    time.sleep(3)

    # Create empty array to load data 
    final_data = []


    id = 0
    
    # Iterate over each row of the table
    rows = driver.find_elements(By.XPATH, '//*[@id="stat-table"]/tbody/tr')
    for row in rows[0:]: 
        # Skip the header row
        try:
            id = id
            batter = row.find_element(By.XPATH, './td[1]/span[1]').text
            pitcher = row.find_element(By.XPATH, './td[2]/span').text
            pa = row.find_element(By.XPATH, './td[3]').text
            ab = row.find_element(By.XPATH, './td[4]').text
            hits = row.find_element(By.XPATH, './td[5]').text
            singles = row.find_element(By.XPATH, './td[6]').text
            doubles = row.find_element(By.XPATH, './td[7]').text
            triples = row.find_element(By.XPATH, './td[8]').text
            hr = row.find_element(By.XPATH, './td[9]').text
            bb = row.find_element(By.XPATH, './td[10]').text
            so = row.find_element(By.XPATH, './td[11]').text
            avg = row.find_element(By.XPATH, './td[12]').text
            obp = row.find_element(By.XPATH, './td[13]').text
            slg = row.find_element(By.XPATH, './td[14]').text

            data = {
                "ID": id,
                "Batter": batter,
                "Pitcher": pitcher,
                "PA": pa,
                "AB": ab,
                "Hits": hits,
                "1B": singles,
                "2B": doubles,
                "3B": triples,
                "HR": hr,
                "BB": bb,
                "SO": so,
                "AVG": avg,
                "OBP": obp,
                "SLG": slg
            }
            
            final_data.append(data)
            id += 1
        except Exception as e:
            print(f"Error processing row: {e}")

finally:
    # Save the data to a JSON file
    with open("data.json", "w") as f:
        json.dump(final_data, f, indent=4)

    # Close the WebDriver
    driver.quit()
