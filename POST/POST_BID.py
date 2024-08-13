from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
# import globalVars

def post_bid(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Bid-post_api_Bid_Create")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Create"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"bidAmount": 100,"needInsurance": true,"notes": "string","projectJobID": 270,"userID": 284,"createdDate": "2024-08-09T11:47:27.744Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Create"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Bid/Create\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Bid/Create\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Bid/Create\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Bid/Create\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Bid-post_api_Bid_Rebid")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Rebid"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"bidAmount": 100,"needInsurance": true,"notes": "string","projectJobID": 270,"userID": 284,"createdDate": "2024-08-09T11:47:27.744Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Rebid"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Bid-post_api_Bid_Rebid"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Bid/Rebid\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Bid/Rebid\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Bid/Rebid\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Bid/Rebid\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    test1()
    test2()