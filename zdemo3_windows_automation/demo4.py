import os
import time


from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

os.system('start chrome.exe --remote-debugging-port=9222')

option = WindowsOptions()
option.app = r"C:\Users\Balaji_Dinakaran\AppData\Local\GitHubDesktop\GitHubDesktop.exe"

driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',
                          options=option)
# driver.implicitly_wait(20)

wait = WebDriverWait(driver, 20)

#click on sign in to github enterprise
# wait.until(expected_conditions.visibility_of_element_located
#            ((AppiumBy.XPATH,"//*[@Name='Sign in to GitHub Enterprise']"))).click()
time.sleep(5)
wait.until(expected_conditions.presence_of_element_located
           ((AppiumBy.XPATH, "//Button[contains(@Name,'Sign in to GitHub')]"))).click()
time.sleep(5)
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
# chrome_driver = "C:\chromedriver.exe"
driver1 = webdriver.Chrome(options=chrome_options)
print(driver1.window_handles)

for window in driver1.window_handles:
    driver1.switch_to.window(window)
    if  driver1.title=="Authorize application":
        break

#driver1 will point to Authorize application tab
print(driver1.current_url)
print(driver1.title)
print(driver1.find_element(AppiumBy.XPATH,'//h2').text)

driver1.find_element(AppiumBy.XPATH,"//button[@name='authorize' and @value='0']").click()

time.sleep(5)
driver.quit()

