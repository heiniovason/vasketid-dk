from dotenv import dotenv_values
#from vasketid-scraper import login_and_scrape_to_soup

config = dotenv_values(".env")

print(config)

#result = login_and_scrape_some_soup(config)

#print(result)
