from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os


script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://python.org")
driver.maximize_window()

search_input = driver.find_element_by_xpath('//*[@id="id-search-field"]')
search_input.send_keys("django")

button_submit = driver.find_element_by_id("submit")
button_submit.click()

func = lambda arg: driver.execute_script("return document.body.parentNode.scroll" + arg)
driver.set_window_size(func("Width"), func("Height"))
driver.find_element_by_tag_name("body").screenshot("python_org_ss.png")


driver.quit()
