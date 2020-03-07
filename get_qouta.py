from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.quotationspage.com/qotd.html")
elem = driver.find_element_by_class_name("quote")
text = elem.text
driver.close()

print("Quote gotten!")
print(text)