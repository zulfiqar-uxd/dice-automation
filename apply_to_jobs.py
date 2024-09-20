import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DiceJobApplier:
    def __init__(self, email, password, chrome_driver_path='./chromedriver.exe'):
        self.email = email
        self.password = password
        self.chrome_driver_path = chrome_driver_path
        self.driver = None

    def initialize_driver(self):
        chrome_options = Options()
        # Uncomment the following line if you want to run Chrome in headless mode
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(self.chrome_driver_path), options=chrome_options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
    
    def login(self):
        self.driver.get("https://www.dice.com/home/home-feed")
        try:
            time.sleep(3)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys(self.email)
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

            time.sleep(3)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))).send_keys(self.password)
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(3)
        except Exception as e:
            print("Error during login:", str(e))
    
    def apply_to_jobs(self):
        with open('new_id.txt', 'r') as new_id:
            for line in new_id:
                self.driver.get(line.strip())
                try:
                    time.sleep(3)
                    # First attempt easy apply btn click
                    apply_button_script = "document.querySelector('#applyButton > apply-button-wc').shadowRoot.querySelector('apply-button > div > button').click();"
                    self.driver.execute_script(apply_button_script)
                except Exception:
                    print("First attempt failed")
                    try:
                        time.sleep(3)
                        # Second attempt easy apply btn click
                        apply_button_script = "document.querySelector('#applyButton > apply-button-wc').shadowRoot.querySelector('apply-button > div > button').click();"
                        self.driver.execute_script(apply_button_script)
                    except Exception:
                        print("-x- skip to next")
                        continue

                try:
                    time.sleep(3)
                    # clicking next on apply step-1
                    self.driver.execute_script("document.querySelector('main > div.navigation-buttons.btn-right > button.seds-button-primary.btn-next').click();")
                except Exception:
                    print("-error- Can't click Next.")
                    continue

                try:
                    time.sleep(3)
                    # clicking submit on apply step-2
                    self.driver.execute_script("document.querySelector('main > div.navigation-buttons > button.seds-button-primary.btn-next').click();")
                except Exception:
                    print("-error- Can't click Submit.")
                    continue
                
                with open('old_id.txt', 'a') as old_id:
                    old_id.write(line)
                time.sleep(3)
    
    def run(self):
        try:
            self.initialize_driver()
            self.login()
            self.apply_to_jobs()
        except Exception as e:
            print("An error occurred:", str(e))
        finally:
            if self.driver:
                self.driver.quit()

if __name__ == "__main__":
    email = "mjuneja1954@gmail.com"
    password = "Driveline1507@"
    applier = DiceJobApplier(email, password)
    applier.run()
