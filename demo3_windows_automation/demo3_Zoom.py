import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

option = WindowsOptions()
option.app = r'C:\Users\Balaji_Dinakaran\AppData\Roaming\Zoom\bin\Zoom.exe'



driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)
driver.implicitly_wait(20)
time.sleep(5)
#click on sign in
driver.find_element(AppiumBy.NAME,'Sign In').click()
#enter username as bala1233455@gmail.com
driver.find_element(AppiumBy.XPATH,"//Edit[@Name='Enter your email']").send_keys("hello12345678@gmail.com")
#enter passwords as welcome1334
driver.find_element(AppiumBy.XPATH,"//Edit[@Name='Enter your password']").click()
driver.find_element(AppiumBy.XPATH,"//Edit[@Name='Enter your password']").send_keys("hello123")

#click login
driver.find_element(AppiumBy.XPATH,'//Button[@Name="Sign In"]').click()

actual_error=driver.find_element(AppiumBy.XPATH,"//Text[contains(@Name,'Incorrect')]").text
print(actual_error)

actual_error=driver.find_element(AppiumBy.XPATH,"//Text[contains(@Name,'Incorrect')]").get_attribute("Name")
print(actual_error)

driver.quit()


