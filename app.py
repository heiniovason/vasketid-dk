from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time

def login(config):

  #######################
  # vasketid.dk - login #
  #######################

  driver = webdriver.Chrome(config.get("driver"))
  driver.get(config.get("url_org_login"))

  # Target org login iframe
  iframe_path = "/html/body/div[1]/iframe[1]"
  iframe_elem = driver.find_element(By.XPATH, iframe_path)
  driver.switch_to.frame(iframe_elem)

  forening_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input"
  driver.find_element(By.XPATH, forening_path).send_keys(config.get("forening"))

  afdeling_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input"
  driver.find_element(By.XPATH, afdeling_path).send_keys(config.get("afdeling"))

  submit_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[4]/td[2]/button"
  driver.find_element(By.XPATH, submit_path).click()

  #time.sleep(10)

  ##############
  # sc - login #
  ##############
 
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"aLog.asp"))

  brugernavn_path = "/html/body/center/table[2]/tbody/tr[2]/td[3]/input"
  driver.find_element(By.XPATH, brugernavn_path).send_keys(config.get("brugernavn"))
  
  adgangskode_path = "/html/body/center/table[2]/tbody/tr[3]/td[3]/input"
  driver.find_element(By.XPATH, adgangskode_path).send_keys(config.get("adganskode"))
  
  submit_path = "/html/body/center/table[2]/tbody/tr[5]/td[2]/button"

  # Redirects to http://87.61.135.30/BrugerStart.asp
  driver.find_element(By.XPATH, submit_path).click()

  # Links fra menuen: /Logoff.asp, /help-sc.asp, /Info.asp, /MinKonto.asp, /Saldo.aps, /Status.asp, /Reservation.asp, /Symbol.asp, /OpenTime.asp

  time.sleep(10)
  # Ref til help-sc.asp virker åbentbart ikke ud af boksen - se js output i konsol
  #driver.get("{0}/{1}".format(config.get("sc_base_url"),"help-sc.asp"))
  #time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Info.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"MinKonto.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Saldo.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Status.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Reservation.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Symbol.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"OpenTime.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Logoff.asp"))
  time.sleep(10)

def main():

  config = {
    "forening": sys.argv[1],
    "afdeling": sys.argv[2],
    "brugernavn": sys.argv[3],
    "adganskode": sys.argv[4],
    "driver": sys.argv[5],
    "url_org_login": sys.argv[6],
    "sc_base_url": sys.argv[7]
  }

  login(config)

if __name__ == "__main__":
    main()
