import os
import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiceJobLinkFetcher:
    def __init__(self, chrome_driver_path='./chromedriver.exe'):
        self.chrome_driver_path = chrome_driver_path
        self.driver = None
        self.query_list = ['ux ', 'ui ', 'ui/ ' 'ux/ ', 'ui- ' 'ux- ', 'ui| ' 'ux| ', 'user experience', 'user interface', 'interaction design', 'visual design', 'product design', 'ux/ui', 'ux designer', 'ui designer', 'Data Visualisation', 'visual']

    def initialize_driver(self):
        chrome_options = Options()
        # Uncomment the following line if you want to run Chrome in headless mode
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(self.chrome_driver_path), options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def fetch_job_links(self):
        pageNo = 1
        print("Scraping job list")
        while pageNo != 0:
            base_url = "https://www.dice.com/jobs"
            query_params = {
                "q": "ui ux designer",
                "countryCode": "US",
                "radius": "30",
                "radiusUnit": "mi",
                "page": pageNo,
                "pageSize": 100,
                "filters.employmentType": "THIRD_PARTY%7CCONTRACTS%7CPARTTIME",
                "filters.easyApply": "true",
                "language": "en"
            }
            search_link = f"{base_url}?{'&'.join([f'{key}={value}' for key, value in query_params.items()])}"
            print(f"Fetching jobs from: {search_link}")
            self.driver.get(search_link)
            try:
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#totalJobCount")))
                total_jobs = self.driver.find_element(By.CSS_SELECTOR, "#totalJobCount").get_attribute('innerText')
                total_jobs = int(''.join(filter(str.isdigit, total_jobs)))
                print(f"Total jobs found: {total_jobs}")
            except Exception:
                total_jobs = 0
                print("No new jobs found.")
                return
            
            pageNo += 1
            if pageNo > math.ceil(int(total_jobs)/100):
                pageNo = 0

            for i in range(1, 101):
                try:
                    writeFile = True
                    job_card_selector = f'.ng-star-inserted dhi-search-card:nth-child({i}) .card-header h5 a'
                    job_id_element = self.driver.find_element(By.CSS_SELECTOR, job_card_selector)
                    job_id = job_id_element.get_attribute('id')
                    job_title = job_id_element.get_attribute('innerText').lower()

                    # Fetch job description
                    job_description_selector = f'.ng-star-inserted dhi-search-card:nth-child({i}) .card-description'
                    job_description_element = self.driver.find_element(By.CSS_SELECTOR, job_description_selector)
                    job_description = job_description_element.get_attribute('innerText').lower()

                    # Check if any of the query keywords are in the job title or description
                    if not any(keyword in job_title for keyword in self.query_list): # or keyword in job_description 
                        continue

                    with open('old_id.txt', 'r') as old_id:
                        if job_id in old_id.read():
                            writeFile = False

                    if writeFile:
                        with open('new_id.txt', 'a') as new_id:
                            new_id.write(f"https://www.dice.com/job-detail/{job_id}" + '\n')
                except Exception as e:
                    print(f"Error processing job card {i} on page {pageNo}: {e}")
            
            print(f"--> Page {pageNo}")
        print("Done scraping job list")

    def run(self):
        try:
            self.initialize_driver()
            self.fetch_job_links()
        except Exception as e:
            print("An error occurred:", str(e))
        finally:
            if self.driver:
                self.driver.quit()

if __name__ == "__main__":
    fetcher = DiceJobLinkFetcher()
    fetcher.run()
