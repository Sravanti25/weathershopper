""" Program to select most expensive sunscreen into the cart """

import time
from selenium import webdriver

class ExpSunscreen:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
#Navigate to weather Shopper sunscreen page

    def goToURL(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
        time.sleep(4)
#Get list of Sunscreen       
    def getSunscreens(self):
        self.list_of_sunscreen = []    
        sunscreens  = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::p[contains(text(),'rice')]/preceding-sibling::p")
        for each_val in sunscreens:
            cream = each_val.text
            self.list_of_sunscreen.append(cream)
        return self.list_of_sunscreen

#Get list of Prices    
    def getPrices(self):
        self.list_of_prices = []
        prices = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::p[contains(text(),'rice')]")
        for each_val in prices:
            each_text = each_val.text
            price = each_text.split(" ")[-1]
            self.list_of_prices.append(price)
        return self.list_of_prices
    
    def getButtons(self):
        buttons = []
        buttons = self.driver.find_elements_by_xpath("//button[contains(text(),'Add')]")
        return buttons

#Find most expensive sunscreen
    def findExpSunscreen(self):
        maxIndex = 0
        i = 0
        maxPrice = self.list_of_prices[0]
        for price in self.list_of_prices:
            if price > maxPrice:
                maxIndex = i
                maxPrice = price
            i = i+1
        buttons = self.getButtons()
        buttons[maxIndex].click()

    #Close browser
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    sunscreen_object = ExpSunscreen()
    sunscreen_object.setUp()
    sunscreen_object.goToURL()
    list_of_sunscreen = sunscreen_object.getSunscreens()
    list_of_prices = sunscreen_object.getPrices()
    print("The list of Sunscreens is ", list_of_sunscreen)
    print("The list of prices is ", list_of_prices)
    sunscreen_object.findExpSunscreen()
    # sunscreen_object.tearDown()