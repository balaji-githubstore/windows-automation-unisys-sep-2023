import time

from appium.options.windows import WindowsOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

option = WindowsOptions()
option.app = r'C:\Windows\system32\notepad.exe'


driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)

driver.find_element(AppiumBy.XPATH,"//MenuItem[@Name='View']").click()

print(driver.page_source)
time.sleep(5)

driver.quit()


