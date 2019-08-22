""" This program is to add two sunscreens to the cart based on the following condition:
First, select the least expensive sunscreen that is SPF-50. For your second sunscreen, 
select the least expensive sunscreen that is SPF-30. Click on the cart when you are done."""

import time
from operator import itemgetter
from selenium import webdriver

class AddSunscreenCondition():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

#Navigate to Sunscreen page. 
    def goToSunscreen(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/sunscreen")
        time.sleep(5)

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
        list_of_prices = []
        prices = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::p[contains(text(),'rice')]")
        for each_val in prices:
            each_text = each_val.text
            price = each_text.split(" ")[-1]
            list_of_prices.append(price)
        return list_of_prices

#Get list of buttons        
    def getButtons(self):
        self.list_of_buttons = self.driver.find_elements_by_xpath("//button[contains(text(),'Add')]")
        return self.list_of_buttons

#Combine the names of cream and prices into one list    
    def combinedList(self):
        cream_price = dict(zip(self.list_of_sunscreen, list_of_prices))
        return cream_price

#Find the names of Sunscreen with SPF-30 and SPF-50 and sort them
    def findCreams(self):
        spf30_list_init = []
        spf50_list_init = []
        
        for key,val in cream_price.items():
            each_name = {'name': key, 'value': val}

            if 'spf-30'.lower() in key.lower():
                spf30_list_init.append(each_name)
            elif 'spf-50'.lower() in key.lower():
                spf50_list_init.append(each_name)
     
        self.spf30_list = sorted(spf30_list_init, key=itemgetter('value'))
        self.spf50_list = sorted(spf50_list_init, key=itemgetter('value'))
      #  print("The list of creams having SPF-30 is ", self.spf30_list)
      #  print("The list of creams having SPF-50 is ",self.spf50_list)

        return self.spf30_list, self.spf50_list

#Add the creams to the cart    
    def addToCart(self):
        to_click = []
        
        if len(self.spf30_list) > 0:
            to_click.append(self.spf30_list[0]['name'])
        if len(self.spf50_list) > 0:
            to_click.append(self.spf50_list[0]['name'])
        
        if len(to_click) > 0:
            for i in range(len(self.list_of_sunscreen)):
                if self.list_of_sunscreen[i] in to_click:
                    self.list_of_buttons[i].click()

#Check Cart
    def clickCart(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Cart -')]").click()
        time.sleep(3)

#Close browser
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    sunscreen_object = AddSunscreenCondition()
    sunscreen_object.setUp()
    sunscreen_object.goToSunscreen()
    list_of_sunscreen = sunscreen_object.getSunscreens()
    list_of_prices = sunscreen_object.getPrices()
    print("The list of Sunscreens is ", list_of_sunscreen)
    print("The list of prices is ", list_of_prices)
    cream_price = sunscreen_object.combinedList()
    print("The combined list is ",cream_price)
    sunscreen_object.getButtons()
    spf30_list_cream, spf50_list_cream = sunscreen_object.findCreams()
    
    print("The list of creams having SPF-30 is ", spf30_list_cream)
    print("The list of creams having SPF-50 is ", spf50_list_cream)
    sunscreen_object.addToCart()
    sunscreen_object.clickCart()
    sunscreen_object.tearDown()






