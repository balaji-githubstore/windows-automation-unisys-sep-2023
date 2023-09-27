import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

option = WindowsOptions()
option.app = r"C:\Users\Balaji_Dinakaran\AppData\Local\GitHubDesktop\GitHubDesktop.exe"


driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=option)
# driver.implicitly_wait(20)

wait = WebDriverWait(driver, 20)

#click on sign in to github enterprise
# wait.until(expected_conditions.visibility_of_element_located
#            ((AppiumBy.XPATH,"//*[@Name='Sign in to GitHub Enterprise']"))).click()

wait.until(expected_conditions.visibility_of_element_located
           ((AppiumBy.NAME, 'Sign in to GitHub Enterprise'))).click()

#enter ae address
wait.until(expected_conditions.visibility_of_element_located
           ((AppiumBy.XPATH, "//Edit[contains(@Name,'Enterprise')]"))).send_keys("appium.com")

#click on cancel
wait.until(expected_conditions.visibility_of_element_located
           ((AppiumBy.NAME, 'Cancel'))).click()

# https://github.com/appium/appium-windows-driver/blob/master/README.md
driver.execute_script("windows: deleteFolder",{"remotePath":r"C:\Mine\Demo\Helloi"})

driver.execute_script("windows: launchApp")


