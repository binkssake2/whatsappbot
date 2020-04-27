#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver = r"C:\Users\binks\Desktop\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://web.whatsapp.com/")
sleep(20)


BarraBusca = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')


BarraBusca.click()
BarraBusca.send_keys("Dan")
BarraBusca.send_keys(Keys.RETURN)
while (1):

    sendbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    sendbox.send_keys("Hola que pasa manito?")
    sendbox.send_keys(Keys.RETURN)
    sleep(2)


# In[ ]:




