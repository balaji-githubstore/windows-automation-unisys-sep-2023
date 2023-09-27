import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

option = WindowsOptions()
option.app = r"Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
driver = webdriver.Remote(command_executor='http://localhost:7676/wd/hub', options=option)

driver.find_element(AppiumBy.XPATH, "//Button[@AutomationId='TogglePaneButton']").click()

wait = WebDriverWait(driver, 20)
elements = wait.until(expected_conditions.presence_of_all_elements_located((AppiumBy.XPATH, "//ListItem")))

print(len(elements))

print(elements[0].text)
print(elements[0].get_attribute("Name"))

for i in range(0, len(elements)):
    print(elements[i].text)
    print(elements[i].get_attribute("Name"))
    print(elements[i].get_attribute("AutomationId"))
#     when name is matching click on Area Converter then click it
    if elements[i].get_attribute("AutomationId")=='Area':
        elements[i].click()
        break

time.sleep(2)
driver.quit()
