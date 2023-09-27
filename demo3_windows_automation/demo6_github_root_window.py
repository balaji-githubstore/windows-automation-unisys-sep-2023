import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait

# driver1=webdriver.Chrome()
# driver1.maximize_window()



option = WindowsOptions()
option.app = r"C:\Users\Balaji_Dinakaran\AppData\Local\GitHubDesktop\GitHubDesktop.exe"
# # option.set_capability("platformName","windows")
# # option.set_capability("noReset",True)
# option.set_capability("app",r"C:\Users\Balaji_Dinakaran\AppData\Local\GitHubDesktop\GitHubDesktop.exe")
#
#
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=option)
# # driver.implicitly_wait(20)
#
wait = WebDriverWait(driver, 20)

print(driver.page_source)
#click on sign in with browser --> assume it opens new window

#reinitialize session with Root level
option = WindowsOptions()
option.set_capability("app","Root")
# option.app_top_level_window=hex(3604D6)
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=option)

print(driver.page_source)

print(len(driver.find_elements(AppiumBy.XPATH,"//Window[@Name='Zoom']")))

driver.find_element(AppiumBy.XPATH,"(//Window[@Name='Zoom'])[1]//*[@Name='Sign In']").click()
time.sleep(5)
driver.quit()
#
# #enter ae address
# wait.until(expected_conditions.visibility_of_element_located
#            ((AppiumBy.XPATH, "//*[contains(@Name,'Sign in to GitHub')]"))).send_keys(Keys.Enter)
#
# # Address and search bar
#
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # connect existing browser
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# #Change chrome driver path accordingly
# chrome_driver = "C:\chromedriver.exe"
# driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)








