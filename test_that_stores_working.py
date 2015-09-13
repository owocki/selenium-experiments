## occipital imports
from common import *

## python imports
import time
import operator

## selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#set up
SLEEP_SECS = 1.5
driver = webdriver.Chrome(SETTINGS['local_webdriver_path'])  # Optional argument, if not specified will search path.
driver.get(SETTINGS['target_url']);


#landing page
ele_number = 1
click_buy_selector = "btn"
click_buy_elements = driver.find_elements_by_class_name(click_buy_selector)
click_buy_elements[ele_number].click()


# store page
ele_number = 0
product_name = 'ipad air'
product_class = "ipad-air"
product_elements = driver.find_elements_by_class_name(product_class)
product_elements[ele_number].click()

#click buy
ele_number = 0
buy_id = "buy-sensor"
buy_elements = driver.find_elements_by_id(buy_id)
buy_elements[ele_number].click()

#click add to cart
time.sleep(SLEEP_SECS)
ele_number = 0
add_to_cart_selector = "confirm"
add_to_cart_elements = driver.find_elements_by_class_name(add_to_cart_selector)
add_to_cart_elements[ele_number].click()

#shipping
#
shipping_info_ids = {
	'first_name' : 'Kevin',
	'last_name' : 'Owocki',
	'address_line1' : '122 Not a real st',
	'address_line2' : '',
	'address_city' : 'Boulder',
	'phone' : '18001234567',
}

time.sleep(SLEEP_SECS)
for key,value in shipping_info_ids.iteritems():
	ele_selector = key
	ele = driver.find_element_by_id(ele_selector)
	ele.send_keys(value)

#
shipping_info_names = {
	'email' : 'owocki@notreal.com',
}

for key,value in shipping_info_names.iteritems():
	ele_selector = key
	ele = driver.find_element_by_name(ele_selector)
	ele.send_keys(value)

#
shipping_info_next = (
	( 'address_country' , 'United States of America'),
	( 'address_state_dropdown' , 'Colorado' ),
)

for (key,value) in shipping_info_next:
	ele_selector = key
	ele = Select(driver.find_element(By.ID,ele_selector))
	ele.select_by_visible_text(value)

#
shipping_info_next = {
	'address_zip' : '80302',
}

time.sleep(SLEEP_SECS)
for key,value in shipping_info_next.iteritems():
	ele_selector = key
	ele = driver.find_element_by_id(ele_selector)
	ele.send_keys(value)

#
shipping_info_next = {
	'speed' : 'speed-std',
}

time.sleep(SLEEP_SECS)
for key,value in shipping_info_next.iteritems():
	ele_selector = key
	ele = driver.find_element_by_id(value)
	ele.click()

#click add to cart
time.sleep(SLEEP_SECS)
ele_number = 0
add_to_cart_selector = "btn-large"
add_to_cart_elements = driver.find_elements_by_class_name(add_to_cart_selector)
add_to_cart_elements[ele_number].click()


#billing
#
billing_info_ids = {
	'name' : 'Kevin Owocki',
	'cc-num' : '4242424242424242',
	'cvc' : '123',
	'exp-month' : '12',
	'exp-year' : '2019',
}

#
time.sleep(SLEEP_SECS)
for key,value in billing_info_ids.iteritems():
	ele_selector = key
	ele = driver.find_element_by_id(ele_selector)
	ele.send_keys(value)

#
for i in ['terms','email_opt_in']:
	ele = driver.find_element_by_id(i)
	ele.click()

#
billing_info_next = {
	'button' : 'charge_payment',
}

#
for key,value in billing_info_next.iteritems():
	ele_selector = key
	ele = driver.find_element_by_id(value)
	ele.click()

#Final Submit
time.sleep(SLEEP_SECS)
driver.find_element_by_id('final-confirm-button').click()

#TODO: ALert handling would go here. Maybe use dead mans snitch?

#tear down
if not SETTINGS['IS_DEBUG']:
	driver.quit()
