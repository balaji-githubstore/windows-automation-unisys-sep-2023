import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

option = WindowsOptions()
option.app = r'C:\Windows\system32\notepad.exe'

driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)
driver.implicitly_wait(20)
# driver.find_element(AppiumBy.XPATH,"//*[@Name='Text Editor']").send_keys("hello 123")

#click on element
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# actions.w3c_actions.pointer_action.click(driver.find_element(AppiumBy.XPATH,"//*[@Name='Help']"))
actions.w3c_actions.pointer_action.move_to(driver.find_element(AppiumBy.XPATH,"//*[@Name='Help']"))
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(2)
actions.perform()


# driver.find_element(AppiumBy.XPATH,"//MenuItem[@Name='File']").click()
#
# driver.find_element(AppiumBy.XPATH,"//MenuItem[contains(@Name,'Save As')]").click()
# # "Ctrl+Shift+S"
# # AcceleratorKey
# # print(driver.page_source)
# # driver.find_element(AppiumBy.XPATH,"//MenuItem[contains(@AcceleratorKey,'Shift')]").click()
# # driver.find_element(AppiumBy.XPATH,"//Edit[@Name='File name:']").send_keys(r"c:\mine\demo.txt")
# driver.find_element(AppiumBy.XPATH,"//Edit[@ClassName='Edit']").send_keys(r"c:\mine\demo.txt")
#
# # driver.find_element(AppiumBy.CLASS_NAME,'Edit').send_keys(r"c:\mine\demo.txt")
# driver.find_element(AppiumBy.XPATH,"//Button[@Name='Save']").click()
#
time.sleep(5)
driver.quit()




