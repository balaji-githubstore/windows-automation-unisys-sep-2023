import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

option = WindowsOptions()
option.app = r'C:\Windows\system32\notepad.exe'

driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)
driver.implicitly_wait(20)
driver.find_element(AppiumBy.XPATH,"//*[@Name='Text Editor']").send_keys("hello 123")

driver.find_element(AppiumBy.XPATH,"//MenuItem[@Name='File']").click()

driver.find_element(AppiumBy.XPATH,"//MenuItem[contains(@Name,'Save As')]").click()
# "Ctrl+Shift+S"
# AcceleratorKey
# print(driver.page_source)
# driver.find_element(AppiumBy.XPATH,"//MenuItem[contains(@AcceleratorKey,'Shift')]").click()
# driver.find_element(AppiumBy.XPATH,"//Edit[@Name='File name:']").send_keys(r"c:\mine\demo.txt")
driver.find_element(AppiumBy.XPATH,"//Edit[@ClassName='Edit']").send_keys(r"c:\mine\demo.txt")
#
# driver.find_element(AppiumBy.CLASS_NAME,'Edit').send_keys(r"c:\mine\demo.txt")
driver.find_element(AppiumBy.XPATH,"//Button[@Name='Save']").click()

driver.quit()




