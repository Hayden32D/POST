from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars

def post_task(driver):
    wait = WebDriverWait(driver, 15)

    def test1():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Task-get_api_Task_completeddetails__jobItemID_")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_completeddetails__jobItemID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_to_write = globalVars.JOB_ITEM_ID
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_completeddetails__jobItemID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Task-get_api_Task_completeddetails__jobItemID_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Task/completeddetails/{jobItemID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Task/completeddetails/{jobItemID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Task/completeddetails/{jobItemID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Task/completeddetails/{jobItemID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test2():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Task-get_api_Task_details__taskID_")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_details__taskID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_to_write = globalVars.TASK_ID
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_details__taskID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Task-get_api_Task_details__taskID_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Task/details/{taskID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Task/details/{taskID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Task/details/{taskID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Task/details/{taskID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test3():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Task-get_api_Task_list__TemplateID_")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_list__TemplateID_"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_to_write = globalVars.TEMPLATE_ID
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task_list__TemplateID_"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Task-get_api_Task_list__TemplateID_"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Task/list/{TemplateID}\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Task/list/{TemplateID}\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Task/list/{TemplateID}\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Task/list/{TemplateID}\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test4():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Task-get_api_Task__TaskID__templatelocations")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__templatelocations"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_to_write = globalVars.TASK_ID
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__templatelocations"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__templatelocations"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Task/{TaskID}/templatelocations\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Task/{TaskID}/templatelocations\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Task/{TaskID}/templatelocations\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Task/{TaskID}/templatelocations\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    def test5():
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Task-get_api_Task__TaskID__tasklocations")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__tasklocations"]/div[2]/div/div[1]/div[2]/div/table/tbody/tr/td[2]/input')))
            text_to_write = globalVars.TASK_ID
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__tasklocations"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            print("Status for project details: " + status_text[0:3])
            status_num = int(status_text[0:3])

            close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Task-get_api_Task__TaskID__tasklocations"]/div[1]/button[1]/div')))
            close_tab.click()

            if status_num == 200:
                print("API call successful (Status 200) for /api/Task/{TaskID}/tasklocations\n")
                return 200
            elif status_num == 401:
                print("Unauthorized access (Status 401) for /api/Task/{TaskID}/tasklocations\n")
                return 401
            elif status_num == 400:
                print("Bad request (Status 400) for /api/Task/{TaskID}/tasklocations\n")
                return 400
            elif status_num == 500:
                print("Internal server error (Status 500) for /api/Task/{TaskID}/tasklocations\n")
                return 500
            else:
                print("Error")

        except Exception as e:
            print(e)

    test1()
    test2()
    test3()
    test4()
    test5()
