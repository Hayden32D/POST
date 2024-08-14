from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars

def post_support(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Support-post_api_Support_create")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Support-post_api_Support_create"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"title": "ticket","description": "broken test","priorityLevel": 1,"createdDate": "2024-08-14T17:42:17.160Z","createdBy": 279}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Support-post_api_Support_create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Support-post_api_Support_create"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Support/create\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Support/create\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Support/create\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Support/create\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Support-post_api_Support_respond")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Support-post_api_Support_respond"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"ticketID": 4,"response": "done","createdDate": "2024-08-14T17:46:45.783Z","createdBy": 279,"submitDate": "2024-08-14T17:46:45.783Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Support-post_api_Support_respond"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Support-post_api_Support_respond"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Support/respond\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Support/respond\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Support/respond\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Support/respond\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)

    test1()
    test2()