from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def login_and_scrape_to_soup(config, headless=False):

  # TODO: Remember to choose random agent
  # https://pypi.org/project/fake-useragent/

  options = Options()
  options.headless = headless
  driver = webdriver.Chrome(
    config.get("SELENIUM_DRIVER"),
    options=options
    )

  driver.get(config.get("CUSTOMER_LOGIN"))

  #######################
  # vasketid.dk - login #
  #######################

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

  # Ref til help-sc.asp virker åbentbart ikke ud af boksen - se js output i konsol
  #driver.get("{0}/{1}".format(config.get("sc_base_url"),"help-sc.asp"))
  #time.sleep(5)

  soup_dict = dict()

  # TODO: Do async requests - blov takes 9-12 seconds to finish.
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Info.asp"))
  soup_dict["info"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"MinKonto.asp"))
  soup_dict["user_account"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Saldo.asp"))
  soup_dict["saldo"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Status.asp"))
  soup_dict["status"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Reservation.asp"))
  soup_dict["reservations"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Symbol.asp"))
  soup_dict["symbols"] = driver.page_source
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"OpenTime.asp"))
  soup_dict["opentime"] = driver.page_source

  # Log off
  driver.get("{0}/{1}".format(config.get("SC_BASE_URL"),"Logoff.asp"))
  # Kill driver instance
  driver.close()

  return soup_dict
