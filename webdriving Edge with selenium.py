from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("http://omegle.com")

text = driver.find_element_by_id('textbtn')
text.click()

awk1 = driver.find_element_by_xpath('/html/body/div[7]/div/p[1]/label')
awk1.click()

time.sleep(1)

awk2 = driver.find_element_by_xpath('/html/body/div[7]/div/p[2]/label')
awk2.click()

time.sleep(1)

awk3 = driver.find_element_by_xpath('/html/body/div[7]/div/p[3]/input')

time.sleep(1)

awk3.click()

time.sleep(2)

chat = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/table/tbody/tr/td[2]/div/textarea')



chat.send_keys('Hello?')
  
chat.send_keys(Keys.ENTER)







##
##google search
##search = driver.find_element_by_name('q')
##search.send_keys('fuck')
##
##search.send_keys(Keys.RETURN)




##PATH = ("C:\Users\shawn\pyprojsel\Webdriver")
##driver = webdriver.Edge(PATH)
##
##
##options = EdgeOptions()
##driver = webdriver.Edge(options=options)
##
##
##driver.get('http://google.com")
##
##
##driver.quit()
##
##
##









##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##import time
##
##
##PATH = "C:\Users\shawn\pyprojsel\Webdriver\msedgedriver.exe"
##driver = webdriver.Edge(PATH)
##
##driver.get("https://stangricki.github.io/Website-Mizuxe/index.html")
##print(driver.title)
##
##print(driver.get_cookie)
##
##search = driver.find_element_by_id('newsletter')
##
##search.send_keys("standard_user")
##search.send_keys(Keys.RETURN)
