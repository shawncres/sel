from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

driver = webdriver.Edge()
driver.get("http://omegle.com")

class TestOmegle(unittest.TestCase):

    def test_find(self):
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
        time.sleep(5)
        if 'Stranger:' not in driver.page_source:
            chat.send_keys('Anyone there ASL?')
            chat.send_keys(Keys.ENTER)
        else:
            chat.send_keys('F24 hows it going?')
            chat.send_keys(Keys.ENTER)
        time.sleep(10)    
        self.assertTrue('Stranger:' in driver.page_source)
        time.sleep(10)
        driver.close()
        
if __name__ == '__main__':
    unittest.main()



##           assertion syntax
####class TestStringMethods(unittest.TestCase):
####
####    def test_upper(self):
####        self.assertEqual('foo'.upper(),'FOO')
####
####    def test_isupper(self):
####        self.assertTrue('FOO'.isupper())
####        self.assertFalse('Foo'.isupper())    
####
####    def test_split(self):
####        s = 'hello world'
####        self.assertEqual(s.split(), ['hello', 'world'])
####        # check that s.split fails when the separator is not a string
####        with self.assertRaises(TypeError):
####            s.split(2)
####
####
####if __name__ == '__main__':
####    unittest.main()
####
####    


    
                        
