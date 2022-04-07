from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("http://google.com")

sb = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')


sb.send_keys('fuck')
x = sb.get_attribute('value')


y = driver.page_source

if x in y:
    print('Your word is {0}'.format(x))
else:
    print('You\'ve failed yet again')



    
