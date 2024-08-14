from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars
import Create_Job_for_contract

def post_contract(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:

            jobID = Create_Job_for_contract.createJob(driver)

            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Contract-post_api_Contract_create")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()


            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_create"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"projectJobsID": ' + jobID + ',"contractorID": 305,"description": "none", "paymentProportionID": 1, "contractorFilterTypeID": 1110, "isLabor": true,"isMaterial": true,"isEquipment": true, "createdDate": "2024-08-09T14:10:08.128Z","createdBy": 284}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_create"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Contract/create\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Contract/create\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Contract/create\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Contract/create\n")
                return 500
            else:
                print("Error")

            return jobID

        except Exception as e:
            print(e)

    jobID = test1()

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Contract-post_api_Contract_generate")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_generate"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"projectJobContractID": ' + jobID + ',"projectJobsID": 359,"createdBy": 284,"createdDate": "2024-08-09T18:34:18.417Z","contractHTML": "string"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_generate"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Contract-post_api_Contract_generate"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Contract/generate\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Contract/generate\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Contract/generate\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Contract/generate\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    