from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scraper:

    def __init__(self):
        self.driver = webdriver.Safari()
        self.companies_to_search = {
            1: "https://careers.boozallen.com/jobs/search/?1485=Japan&listFilterMode=1&jobRecordsPerPage=20&",
            2: "https://www.lockheedmartinjobs.com/search-jobs/Japan",
            3: "https://www.northropgrumman.com/jobs?_job_search=Japan",
        }
        self.unstructured_data = {}

    def company_selector(self):
        for key, url in self.companies_to_search.items():
            self.get_req_titles(key, url)

    def get_req_titles(self, key, url):
        match key:
            case 1:
                ba_list = []
                self.driver.get(url)
                reqs = self.driver.find_elements(By.CLASS_NAME, "cell-title")
                for i in reqs:
                    ba_list.append(i.text)

                self.unstructured_data["Booz Allen"] = ba_list
            case 2:
                lh_list = []
                self.driver.get(url)
                reqs = self.driver.find_elements(By.CLASS_NAME, "job-title")
                for i in reqs:
                    lh_list.append(i.text)

                self.unstructured_data["Lockheed Martin"] = lh_list
                # ! CASE 3 still needs work
            # case 3:
            #     self.driver.get(url)
            #     self.driver.implicitly_wait(2)
            #     reqs = self.driver.find_elements(
            #         By.CLASS_NAME,
            #         "col-sm-9",
            #     )

            #     for i in reqs:
            #         print(i.find_element(By.TAG_NAME, "h2").text)

    def close_driver(self):
        self.driver.close()
