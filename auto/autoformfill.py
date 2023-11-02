from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("Hello, Google!")
search.send_keys(Keys.RETURN)