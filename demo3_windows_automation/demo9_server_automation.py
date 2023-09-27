from appium.webdriver.appium_service import AppiumService

service=AppiumService()

service.start(args=['-p','4723','-a','127.0.0.1',"--base-path",'/wd/hub'])

# service.start(args=["--base-path",'/wd/hub'])
# launch app
#automate app

print(service.is_running)
print(service.is_listening)

# should run always
service.stop()

