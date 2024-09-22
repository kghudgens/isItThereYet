from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def activeDriver():
    
   driver = webdriver.Chrome()
   bAScrape(driver)
   driver.close()

def bAScrape(driver):
    driver.get("https://careers.boozallen.com/jobs/search/?1485=Japan&listFilterMode=1&jobRecordsPerPage=20&")
    print(driver.title)
    
def getTitles(driver):
    titles = driver.find_elements_by_class_name("cell-title")
    