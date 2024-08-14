from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars

def post_CO(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-ChangeOrder-post_api_ChangeOrder_Create")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder_Create"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"projectJobsID": 270,"title": "New wallpaper","description": " ","labor": 10,"material": 10,"amountTotal": 20,"thread": " ","newCompletionDate": "2024-08-09T12:03:05.368Z","createdDate": "2024-08-09T12:03:05.368Z","createdBy": 284}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder_Create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder_Create"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ChangeOrder/Create\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ChangeOrder/Create\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ChangeOrder/Create\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ChangeOrder/Create\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-ChangeOrder-post_api_ChangeOrder__ID__Response")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__Response"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field1.send_keys(globalVars.JOB_ID)

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__Response"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"rejectReason": "not good enough","newCompletionDate": "2024-08-09T12:10:25.771Z","signatureDocID": "3fa85f64-5717-4562-b3fc-2c963f66afa6","crStatus": " ","labor": 20,"material": 20,"amountTotal": 40,"modifiedBy": 284,"modifiedDate": "2024-08-09T12:10:25.771Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__Response"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__Response"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ChangeOrder/{ID}/Response\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ChangeOrder/{ID}/Response\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ChangeOrder/{ID}/Response\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ChangeOrder/{ID}/Response\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test3():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-ChangeOrder-post_api_ChangeOrder__ID__SendChat")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__SendChat"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_field1.send_keys(globalVars.JOB_ID)

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__SendChat"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"fromUserID": 284,"jobID": 270,"message": "hey","threadID": "1","toUserID": 305,"createdDate": "2024-08-09T13:31:50.380Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__SendChat"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-ChangeOrder-post_api_ChangeOrder__ID__SendChat"]/div[1]/button[1]')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/ChangeOrder/{ID}/SendChat\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/ChangeOrder/{ID}/SendChat\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/ChangeOrder/{ID}/SendChat\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/ChangeOrder/{ID}/SendChat\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    test1()
    test2()
    test3()