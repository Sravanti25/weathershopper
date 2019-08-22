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
        self.list_of_prices = []
        prices = self.driver.find_elements_by_xpath("//div[contains(@class,'container')]/descendant::p[contains(text(),'rice')]")
        for each_val in prices:
            each_text = each_val.text
            price = each_text.split(" ")[-1]
            self.list_of_prices.append(price)
        return self.list_of_prices

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
        self.to_click = []
        
        if len(self.aloe_list) > 0:
            self.to_click.append(self.aloe_list[0]['name'])
        if len(self.almond_list) > 0:
            self.to_click.append(self.almond_list[0]['name'])
        
        if len(self.to_click) > 0:
            for i in range(len(self.list_of_moisturizer)):
                if self.list_of_moisturizer[i] in self.to_click:
                    self.list_of_buttons[i].click()

        print("Items added to the cart " , self.to_click)


#Check the prices
    def checkPrice(self):
        self.getPrice = []

        if len(self.aloe_list) > 0:
            self.getPrice.append(self.aloe_list[0]['value'])
        if len(self.almond_list) > 0:
            self.getPrice.append(self.almond_list[0]['value'])
 
   
        print("Prices of items" , self.getPrice)

        self.fin_tot = sum(int(i) for i in self.getPrice)

        print("The cart total is ", self.fin_tot)

#Click on Cart button to check all creams have been added

    def goToCart(self):
        self.driver.find_element_by_xpath("//button[contains(text(),'Cart ')]").click()
        time.sleep(3)

#Get the list of items added in the Checkout page
    def checkCart(self):
        self.cart_items = []
        list_of_items_cart = self.driver.find_elements_by_xpath("//table/tbody/tr/td[1]")
        for each_val in list_of_items_cart:
            each_item = each_val.text
            self.cart_items.append(each_item)
        print("The items from checkout page ",self.cart_items)

#Compare the items added to the cart and the items present in the checkout page
    def compareItems(self):
        self.to_click.sort()
        self.cart_items.sort()

        if self.to_click == self.cart_items:
            print("The items added to the card are correct")
        else:
            print("The items added are incorrect")

        total_price_text = self.driver.find_element_by_xpath("//div/descendant::p[contains(text(),'Total:')]").text
        self.total_price = total_price_text.split(" ")[-1]
        #print(self.total_price)
  
        if str(self.total_price) == str(self.fin_tot):
            print("The Cart Total is correct")
        else:
            print("The Cart total is incorrect")

#Close browser
    def tearDown(self):
        self.driver.close()

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
    mois_object.checkPrice()
    mois_object.goToCart()
    mois_object.checkCart()
    mois_object.compareItems()
    mois_object.tearDown()






