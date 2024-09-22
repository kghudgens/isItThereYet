from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scraper:

    def __init__(self):
        self.driver = webdriver.Safari()
        self.companiesToSearch = {
            1: "https://careers.boozallen.com/jobs/search/?1485=Japan&listFilterMode=1&jobRecordsPerPage=20&",
            2: "https://www.lockheedmartinjobs.com/search-jobs/Japan",
            3: "https://www.northropgrumman.com/jobs?_job_search=Japan",
        }

    def companySelector(self):
        for key, url in self.companiesToSearch.items():
            print(key)
            self.getReqTitles(key, url)

    def getReqTitles(self, key, url):
        match key:
            case 1:
                self.driver.get(url)
                reqs = self.driver.find_elements(By.CLASS_NAME, "cell-title")
                for i in reqs:
                    print(i.text)
            case 2:
                self.driver.get(url)
                reqs = self.driver.find_elements(By.CLASS_NAME, "job-title")
                for i in reqs:
                    print(i.text)
                    # ! CASE 3 still needs work
            case 3:
                self.driver.get(url)
                self.driver.implicitly_wait(2)
                reqs = self.driver.find_elements(
                    By.CLASS_NAME,
                    "col-sm-9",
                )

                for i in reqs:
                    print(i.find_element(By.TAG_NAME, "h2").text)

    def closeDriver(self):
        self.driver.close()
