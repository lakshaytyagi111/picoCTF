from bs4 import BeautifulSoup
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://mail.google.com/"
def internet_connection():
    try:
        response = requests.get("https://google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False    
if internet_connection():
    page = requests.get(url, timeout=5)
else:
    print("The Internet is not connected.")
    exit()

def scrape_emails():
    emails = re.findall(r'\btr class="zA zE"\b', soup.get_text())
    
    return emails

WEBDRIVER_PATH = '/usr/bin/geckodriver'

def get_page_content(url):
    # Create a new instance of Firefox WebDriver
    driver = webdriver.Firefox(webdriver.FirefoxProfile())
    
    # Navigate to the specified URL
    driver.get(url)
    
    # Wait for user interaction
    input("Press Enter when you are done interacting with the page...")
    
    # Get the page source
    page_content = driver.page_source
    
    # Close the browser
    driver.quit()
    
    return page_content

# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
# emails = scrape_emails()
page_content = get_page_content(url)
print(len(re.findall(r'\btr class="zA zE"\b', page_content)))
print(re.findall(r'\btr class="zA zE"\b', page_content))
# for email in emails:
#     print(email)
# if(classi.contains(zE)):
    