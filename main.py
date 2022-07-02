from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('chromedriver')

# Test usage of selenium
SLEEP_TIME = 5

# Set website url
url = 'https://www.coingecko.com/account/candy?locale=zh-tw'

# Access Site
try:
    driver.get(url)
    print('Successful Access Site')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Could not access' + url)
    exit(1001)

# Login
try:
    driver.find_element("id", "user_email").send_keys(os.environ.get("USEREMAIL"))     #os.environ.get("USEREMAIL")
    driver.find_element("id", "user_password").send_keys(os.environ.get("PASSWORD"))
    time.sleep(SLEEP_TIME)
    driver.find_element("xpath", '//*[@id="new_user"]/input[8]').click()
    print('Successful Login')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Cannot login')
    exit(1002)
# geetest_radar_tip

# Click cookie accept
try:
    driver.find_element("xpath", '//*[@id="cookie-notice"]/div/div/div/div/button').click()
    print('cookie accept')
    time.sleep(SLEEP_TIME)
except Exception as e:
    print('Can not accept cookie')

# Click Daily Reward
try:
    driver.find_element("xpath", '/html/body/div[3]/div[3]/div[3]/div[3]/div/form/input[1]').click()
    time.sleep(SLEEP_TIME)
    print('Successful click Daily Reward')
except Exception as e:
    print(e)
    print('Cannot access daily reward')
    exit(1003)

# Quit
driver.quit()
exit(0)


