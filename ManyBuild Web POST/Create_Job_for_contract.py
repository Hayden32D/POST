from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import globalVars

def createJob(driver):
    wait = WebDriverWait(driver, 15)

    def run_create_job():
        jobID = None
        try:
            open_tab_button = wait.until(EC.element_to_be_clickable((By.ID, "operations-Job-post_api_Job_create")))
            open_tab_button.click()

            try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
            try_it_out_button.click()

            text_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-post_api_Job_create"]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/textarea')))
            text_field.clear()
            text_to_write = '{"bidEndDate": "2024-08-10T17:20:36.505Z","bidStartDate": "2024-08-09T17:20:36.505Z","budget": 1000,"coverPhoto": "3fa85f64-5717-4562-b3fc-2c963f66afa6","jobDetails": "test job for testing","jobEndDate": "2024-08-12T17:20:36.505Z","jobStartDate": "2024-08-11T17:20:36.505Z","rush": false,"title": "Job for API","userID": 279,"createdDate": "2024-08-09T17:20:36.505Z","projectID": 442,"locationIds": "1"}'
            text_field.send_keys(text_to_write)

            execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
            execute_button.click()

            status_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-post_api_Job_create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[1]')))
            status_text = status_element.get_attribute('textContent')
            #print(status_text) #line for debugging
            #print 200
            status_num = int(status_text[0:3])

            if status_num == 200:

                jobIDelement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="operations-Job-post_api_Job_create"]/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]/div[1]/div/pre')))
                jobID = jobIDelement.get_attribute('textContent')
                # print("JobID: " + jobID) #Debugging purposes
                close_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="operations-Job-post_api_Job_create"]/div[1]/button[1]/div')))
                close_tab.click()

            else:
                exit(0)

        except Exception as e:
            print(e)

        return jobID
        

    return run_create_job()