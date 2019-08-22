"""This program is to add all the Moisturizers into the cart"""

import time
from selenium import webdriver

class AllMoisturizer:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
#Navigate to weather Shopper sunscreen page

    def goToURL(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
        time.sleep(4)

#click Add button for all the creams

    def clickAddButton(self):
        list_of_add_buttons = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::button")
        for each_val in list_of_add_buttons:
            each_val.click()
        time.sleep(3)
    
#Click on Cart button to check all creams have been added

    def goToCart(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Cart ')]").click()
        time.sleep(3)

#Close the browser
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    mois_obj = AllMoisturizer()
    mois_obj.setUp()
    mois_obj.goToURL()
    mois_obj.clickAddButton()
    mois_obj.goToCart()
    mois_obj.tearDown()

    