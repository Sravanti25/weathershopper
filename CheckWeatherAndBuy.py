"""This program is to read the temperature listed on the page and 
Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees. """

import time
from selenium import webdriver

class CheckWeatherAndBuy:

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    
#Navigate to weather Shopper page

    def goToURL(self):
        self.driver.get("https://weathershopper.pythonanywhere.com/")
        time.sleep(4) 

#Read the temperature
    def readTemp(self):
        temperature_text = self.driver.find_element_by_xpath("//span[@id='temperature']").text
        temp_val = temperature_text.split(" ")[0]
        self.temperature = int(temp_val)
        return self.temperature

#Depending on temperature choose sunscreen or Moisturizer
    def chooseCream(self):
        sunscreen = self.driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
        moisturizer = self.driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]")

        if self.temperature < 19:
            moisturizer.click()
            print("We have to buy Moisturizer")
            print("We are on the following page - ", self.driver.find_element_by_xpath("//h2").text)

        elif self.temperature > 34:
            sunscreen.click()
            print("We have to buy Sunscreen")
            print("We are on the following page - ", self.driver.find_element_by_xpath("//h2").text)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    weather_obj = CheckWeatherAndBuy()
    weather_obj.setUp()
    weather_obj.goToURL()
    temperature = weather_obj.readTemp()
    print("The temperature is ", temperature)
    weather_obj.chooseCream()