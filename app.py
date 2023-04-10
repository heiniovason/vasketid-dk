from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# vasketid.dk - login
username = ""
password = ""

driver = webdriver.Chrome("chromedriver")
driver.get("https://vasketid.dk")

# Target org login iframe
iframe_path = "/html/body/div[1]/iframe[1]"
iframe_elem = driver.find_element(By.XPATH, iframe_path)
driver.switch_to.frame(iframe_elem)

username_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input"
username_elem = driver.find_element(By.XPATH, username_path) 
username_elem.send_keys(username)

passw_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input"
passw_elem = driver.find_element(By.XPATH, passw_path)
passw_elem.send_keys(password)

submit_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[4]/td[2]/button"
submit_elem = driver.find_element(By.XPATH, submit_path)
submit_elem.click()

time.sleep(3)

# Target <frame 1> inside <frameset>
frame_path = "/html/frameset/frame[1]"
frame_elem = driver.find_element(By.XPATH, frame_path)
driver.switch_to.frame(frame_elem)

login_link_path = "/html/body/center/table/tbody/td[2]/a" # WRONG PATH!!!
link_elem = driver.find_element(By.XPATH, login_link_path)
link_elem.click()

time.sleep(3)

