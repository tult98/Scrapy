from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv

# csv_file = open('data.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['image_url'])


# access the browser driver 
chrome_options = Options()
chrome_options.headless = True
driver = webdriver.Chrome(
    executable_path="./chromedriver.exe", options=chrome_options)

# scroll the webpage 
driver.get(
    "https://vwin99.net/mrcong-mu-fei-fei-anh-nung-gai-xinh-them-du-la-day-chu-dau/")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
page_source = driver.page_source

 
soup = BeautifulSoup(page_source, 'lxml')
# print(soup.prettify())
# get the image_url
entry_content = soup.find('div', class_="entry-content")
# print(entry_content.prettify())

images_content = entry_content.find_all('p')

for image_content in images_content:
    print(image_content)
    print('\n')

driver.quit()
# print(entry_content.prettify())



