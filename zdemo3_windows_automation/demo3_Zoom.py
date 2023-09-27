import time

from appium import webdriver
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy

option = WindowsOptions()
option.app = r'C:\Users\Balaji_Dinakaran\AppData\Roaming\Zoom\bin\Zoom.exe'


driver=webdriver.Remote(command_executor='http://localhost:4723/wd/hub',options=option)
driver.implicitly_wait(20)

#click on sign in
#enter username as bala1233455@gmail.com
#enter passwords as welcome1334
#click login

