from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys
import time

def login_and_scrape_to_soup(config):

  # https://pypi.org/project/fake-useragent/

  #######################
  # vasketid.dk - login #
  #######################

  driver = webdriver.Chrome(config.get("SELENIUM_DRIVER"))
  driver.get(config.get("CUSTOMER_LOGIN"))

  # Target org login iframe
  iframe_path = "/html/body/div[1]/iframe[1]"
  iframe_elem = driver.find_element(By.XPATH, iframe_path)
  driver.switch_to.frame(iframe_elem)

  forening_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input"
  driver.find_element(By.XPATH, forening_path).send_keys(
    config.get("CUSTOMER")
    )

  afdeling_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input"
  driver.find_element(By.XPATH, afdeling_path).send_keys(
    config.get("DEPARTMENT")
    )

  submit_path = "/html/body/div[1]/div[1]/form/table/tbody/tr[4]/td[2]/button"
  driver.find_element(By.XPATH, submit_path).click()

  #time.sleep(10)

  ##############
  # sc - login #
  ##############
 
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"aLog.asp"))

  brugernavn_path = "/html/body/center/table[2]/tbody/tr[2]/td[3]/input"
  driver.find_element(By.XPATH, brugernavn_path).send_keys(
    config.get("RESIDENT_ACCOUNT")
    )
   
  adgangskode_path = "/html/body/center/table[2]/tbody/tr[3]/td[3]/input"
  driver.find_element(By.XPATH, adgangskode_path).send_keys(
    config.get("RESIDENT_TOKEN")
    )
  
  submit_path = "/html/body/center/table[2]/tbody/tr[5]/td[2]/button"

  # Redirects to {SC_BASE_URL}/BrugerStart.asp
  driver.find_element(By.XPATH, submit_path).click()

  # Links fra menuen: /Logoff.asp, /help-sc.asp, /Info.asp, /MinKonto.asp, /Saldo.aps, /Status.asp, /Reservation.asp, /Symbol.asp, /OpenTime.asp

  time.sleep(10)
  # Ref til help-sc.asp virker åbentbart ikke ud af boksen - se js output i konsol
  #driver.get("{0}/{1}".format(config.get("sc_base_url"),"help-sc.asp"))
  #time.sleep(5)

  soup_dict = dict()

  # Build

  driver.get("{0}/{1}".format(config.get("sc_base_url"),"Info.asp"))
  time.sleep(5)
  driver.get("{0}/{1}".format(config.get("sc_base_url"),"MinKonto.asp"))
  html = driver.page_source
  soup_min_konto = BeautifulSoup(html)
  print(soup_min_konto)
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

  return soup_dict
