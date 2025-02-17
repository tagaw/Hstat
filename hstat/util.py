from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait



class HStatUser(webdriver.Chrome):
    def __init__(self, options = None, service = None, keep_alive = True):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        super().__init__(service, keep_alive, options = chrome_options)

        self.implicitly_wait(1)
        self.wait: WebDriverWait = WebDriverWait(self,1,poll_frequency=0.1)  

    def open_site(self, address: str):
        self.get(address)

        
    
