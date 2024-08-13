import time
import newFileOpen
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os

import Create_Job_for_contract
import POST_Contract

# Initialize the WebDriver
chrome_driver_path = r'C:/webdrivers/chromedriver.exe'  # Adjust the path as necessary
service = Service(chrome_driver_path)
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')  # Uncomment for headless mode
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://wsmanybuild.azurewebsites.net/Swagger/index.html")

# Function to perform authorization
def authorize(driver, timeout=15):
    wait = WebDriverWait(driver, timeout)
    
    try:
        # Click the login button
        time.sleep(.25)
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        login_button.click()

        # Click the "Try it out" button
        try_it_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Try it out')]")))
        try_it_out_button.click()

        # Enter login details
        text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[class*='body-param']")))
        text_field.clear()
        text_to_write = '{"userName": "HDouglas+creator1@method-automation.com", "password": "Poohbear@32D"}'
        text_field.send_keys(text_to_write)

        # Execute login
        execute_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Execute')]")))
        execute_button.click()

        # Wait for the response and download the key
        download = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"download-contents")))
        download.click()

        download = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='operations-Auth-post_api_Auth_Login']/div[2]/div/div[3]/div[2]/div/div/table/tbody/tr/td[2]/div[1]/div/button")))
        download.click()

        # Open the new file to get the key
        key = newFileOpen.openNewFile()

        # Authorize with the obtained key
        authorize_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.authorize.unlocked")))
        authorize_button.click()

        time.sleep(1)
        key_input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input")))
        key_input_field.send_keys("Bearer " + key)

        final_press_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.authorize.button")))
        final_press_button.click()

        # Check if authorization was successful
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.authorize.locked")))

        close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.modal-btn.auth.btn-done.button")))
        close.click()

        close_open_tab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.opblock-summary-control")))
        close_open_tab.click()
        time.sleep(2)

        print("Authorization was successful")
        return True

    except TimeoutException:
        print("Element not found within the given time frame")
        return False
    except Exception as e:
        print("Authorization failed: ", str(e))
        return False

# Main script execution
try:
    # Authorize once
    if authorize(driver):

        POST_Contract.post_contract(driver)

except Exception as e:
    print("An error occurred: ", str(e))
