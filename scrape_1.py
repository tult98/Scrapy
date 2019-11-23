from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
import csv

csv_file = open('clean_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['image_url'])

# access the browser driver 
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options = chrome_options)

count = 0

# get the number of page in website 
source = requests.get("https://vwin99.net/anh-hot-girl-18/").text
soup = BeautifulSoup(source, 'lxml')
nav_bar = soup.find('div', class_="nav-links")
nav_bar_link  = nav_bar.find_all('a')
page_number = nav_bar_link[-2].text

for i in range(int(page_number)):
    source = requests.get(f"https://vwin99.net/anh-hot-girl-18/page/{i+1}/").text
    soup = BeautifulSoup(source, 'lxml')
    content_page = soup.find("main", class_="site-main")
    articles = content_page.find_all('div', class_="inside-article")
    for article in articles:
        post_link = article.header.h2.a['href']
        # scroll to the bottom of the webpage
        # solution from here: https://stackoverflow.com/questions/51836275/finding-the-number-of-pages-on-a-website-with-soup-findall-unicode-problems 
        driver.get(post_link)
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        page_source = driver.page_source

        # get the image url
        soup = BeautifulSoup(page_source, 'lxml')
        entry_content = soup.find('div', class_="entry-content")
        images_content = entry_content.find_all('p')
        for image_content in images_content:
            images = image_content.find_all("img", class_="lazy")
            if len(images) > 0:
                for image in images: 
                    image_url = image['src']
                    if "https://" in image_url:
                        count += 1
                        csv_writer.writerow([image_url])
                        print(image_url)

csv_file.close()
print(count)
driver.quit()




