from selenium import webdriver
import time

user_name = "user1"
password = "123456789"
first_name = "Thanh"
last_name = "Bui"
phone_number = "0476328757"

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/register")

element = driver.find_element_by_id("username")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(password)
element = driver.find_element_by_id("firstname")
element.send_keys(first_name)
element = driver.find_element_by_id("lastname")
element.send_keys(last_name)
element = driver.find_element_by_id("phone")
element.send_keys(phone_number)
driver.find_element_by_xpath("//body/section[1]/form[1]/input[6]").click()

time.sleep(5)

driver.close()
