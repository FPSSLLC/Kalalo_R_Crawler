# import undetected_chromedriver as UC
from selenium import webdriver
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os, atexit

load_dotenv(find_dotenv())

https_proxy = os.environ.get("PROXY_HTTPS")
selenium_grid = os.environ.get("SELENIUM_GRID")

class Browser:
    def __init__(self):
        self.headless=True
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability('browserName', "chrome")
        chrome_options.add_argument(f'--proxy-server=https://{https_proxy}')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        chrome_options.add_experimental_option("useAutomationExtension", False) 
        chrome_options.add_argument('--window-size=1920x1080')
        
        if self.headless:
            chrome_options.add_argument('--headless')

        try:
            self.driver = webdriver.Remote(command_executor=selenium_grid, options=chrome_options)
        except Exception as e:
            service = Service(executable_path=ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service,options=chrome_options)

        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        
        atexit.register(self.close)

    def close(self):
        self.driver.quit()