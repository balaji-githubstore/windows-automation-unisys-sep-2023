import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

option = WindowsOptions()
option.app = 'Root'

driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)
driver.implicitly_wait(20)

hexa1=driver.find_element(AppiumBy.XPATH,"//Window[@Name='Zoom']").get_attribute("NativeWindowHandle")
print(hexa1)

print(driver.page_source)

option = WindowsOptions()
option.app_top_level_window=hex(int(hexa1))
driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)

print(driver.page_source)

time.sleep(5)
driver.quit()




