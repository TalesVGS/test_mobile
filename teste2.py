# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.crunchyroll.crunchyroid",
	"appium:appActivity": "com.ellation.crunchyroll.presentation.startup.StartupActivity",
	"appium:noReset": True,
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
el5.click()
el6 = WebDriverWait(driver, 20).until(lambda x: x.find_element(by=AppiumBy.ID, value="com.crunchyroll.crunchyroid:id/search_toolbar_input"))
el6.click()
el6.send_keys("One Piece")
el7 = WebDriverWait(driver, 20).until(lambda x: x.find_element(by=AppiumBy.XPATH, value="(//android.widget.TextView[@resource-id=\"movie_title\"])[1]"))
el7.click()
el8 = WebDriverWait(driver, 20).until(lambda x: x.find_element(by=AppiumBy.ID, value="com.crunchyroll.crunchyroid:id/toggle_watchlist_icon"))
el8.click()
el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el9.click()
el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Navigate up")
el10.click()
el11 = WebDriverWait(driver, 20).until(lambda x: x.find_element(by=AppiumBy.XPATH, value="(//android.widget.ImageView[@resource-id=\"com.crunchyroll.crunchyroid:id/bottom_navigation_tab_item_icon\"])[2]"))
el11.click()

driver.quit()
