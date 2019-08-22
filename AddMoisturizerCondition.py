""" This program is to add two moisturizers to the cart based on the following condition:
select the least expensive mositurizer that contains Aloe. 
For your second moisturizer, select the least expensive moisturizer that contains almond. """

import time
from operator import itemgetter
from selenium import webdriver

class AddMoisturizerCondition():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

#Navigate to Moisturizer page. 
    def goToMoisturizers(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/moisturizer")
        time.sleep(5)

#Get list of Moisturizers       
    def getMoisturizers(self):
        self.list_of_moisturizer = []    
        moisturizers  = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::p[contains(text(),'rice')]/preceding-sibling::p")
        for each_val in moisturizers:
            cream = each_val.text
            self.list_of_moisturizer.append(cream)
        return self.list_of_moisturizer

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
        cream_price = dict(zip(list_of_moisturizer, list_of_prices))
        return cream_price

#Find the names of Moisturizers with Aloe and Almond and sort them
    def findCreams(self):
        aloe_list_init = []
        almond_list_init = []
        
        for key,val in cream_price.items():
            each_name = {'name': key, 'value': val}

            if 'aloe'.lower() in key.lower():
                aloe_list_init.append(each_name)
            elif 'almond'.lower() in key.lower():
                almond_list_init.append(each_name)
     
        self.aloe_list = sorted(aloe_list_init, key=itemgetter('value'))
        self.almond_list = sorted(almond_list_init, key=itemgetter('value'), reverse=True)
        print("The list of creams having Aloe is ", self.aloe_list)
        print("The list of creams having Almond is ",self.almond_list)

        return self.aloe_list, self.almond_list

#Add the creams to the cart    
    def addToCart(self):
        to_click = []
        
        if len(self.aloe_list) > 0:
            to_click.append(self.aloe_list[0]['name'])
        if len(self.almond_list) > 0:
            to_click.append(self.almond_list[0]['name'])
        
        if len(to_click) > 0:
            for i in range(len(self.list_of_moisturizer)):
                if self.list_of_moisturizer[i] in to_click:
                    self.list_of_buttons[i].click()


if __name__ == '__main__':
    mois_object = AddMoisturizerCondition()
    mois_object.setUp()
    mois_object.goToMoisturizers()
    list_of_moisturizer = mois_object.getMoisturizers()
    list_of_prices = mois_object.getPrices()
    print("The list of moisturizers is ", list_of_moisturizer)
    print("The list of prices is ", list_of_prices)
    cream_price = mois_object.combinedList()
    print("The combined list is ",cream_price)
    mois_object.getButtons()
    mois_object.findCreams()
    mois_object.addToCart()






