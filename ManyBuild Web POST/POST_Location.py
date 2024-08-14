from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars

def post_Location(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Location-post_api_Location_include")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_include"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"userID": 284,"locationID": 1}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_include"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Location-post_api_Location_include"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Location/include\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Location/include\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Location/include\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Location/include\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input')))
            text_to_write1 = globalVars.USER_ID
            text_field1.send_keys(text_to_write1)

            active_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/select')))
            active_button.click()
            true_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[2]/td[2]/select/option[2]')))
            true_click.click()

            text_field2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[3]/td[2]/input')))
            text_to_write2 = globalVars.USER2_ID
            text_field2.send_keys(text_to_write2)

            text_field3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr[4]/td[2]/input')))
            text_to_write3 = globalVars.MOD_DATE
            text_field3.send_keys(text_to_write3)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Location-post_api_Location_toggle__ID___Active___ModifiedBy___ModifiedDate_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Location/toggle/{ID}/{Active}/{ModifiedBy}/{ModifiedDate}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Location/toggle/{ID}/{Active}/{ModifiedBy}/{ModifiedDate}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Location/toggle/{ID}/{Active}/{ModifiedBy}/{ModifiedDate}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Location/toggle/{ID}/{Active}/{ModifiedBy}/{ModifiedDate}\n")
                return 500
            else:
                print("Error")


        except Exception as e:
            print(e)


    def test3():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Location-post_api_Location_exclude")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_exclude"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"userID": 276,"locationID": 1,"modifiedDate": "2024-08-13T15:01:55.847Z"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Location-post_api_Location_exclude"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Location-post_api_Location_exclude"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Location/exclude\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Location/exclude\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Location/exclude\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Location/exclude\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)
        
    test1()
    test2()
    test3()
        