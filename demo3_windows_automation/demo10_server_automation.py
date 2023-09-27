from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#appium server start
service=AppiumService()
service.start(args=['-p','4723','-a','127.0.0.1',"--base-path",'/wd/hub'])

# open calculator app
option = WindowsOptions()
option.app = r"Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=option)

driver.find_element(AppiumBy.XPATH, "//Button[@AutomationId='TogglePaneButton']").click()

wait = WebDriverWait(driver, 20)
elements = wait.until(expected_conditions.presence_of_all_elements_located((AppiumBy.XPATH, "//ListItem")))

print(len(elements))

print(elements[0].text)
print(elements[0].get_attribute("Name"))

# close app
driver.quit()

#appium server stop
# should run always
service.stop()

