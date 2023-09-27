from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
# chrome_driver = "C:\chromedriver.exe"
driver1 = webdriver.Chrome(options=chrome_options)

print(driver1.current_url)
print(driver1.title)
print(driver1.find_element(AppiumBy.XPATH,'//h2').text)