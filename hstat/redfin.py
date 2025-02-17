from util import HStatUser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from humanize import humanize_send



def search_redfin(driver: HStatUser, address: str):
    
    driver.open_site('https://redfin.com')
    
    search_bar = driver.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='search-box-input']")))

    humanize_send(search_bar,address)

    search_bar.send_keys(Keys.RETURN)

