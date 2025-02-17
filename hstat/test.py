from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
from humanize import humanize_send

chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://monkeytype.com")

driver.implicitly_wait(3)

wait = WebDriverWait(driver,1)

cookies = wait.until(EC.element_to_be_clickable((By.XPATH,"//dialog[@id='cookiesModal']/div[@class='modal']/div[@class='main']/div[@class='buttons']/button[@class='rejectAll']")))
cookies.click()

zen_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@mode='zen']")))

zen_button.click()

time.sleep(0.5)

input = driver.find_element(By.ID,'wordsInput')

humanize_send(input,"You are a stinky boy stop spending your time typing lol")

input.send_keys(Keys.SHIFT,Keys.ENTER)

time.sleep(10)
driver.close()