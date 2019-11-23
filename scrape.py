from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('data.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['image_url'])
count = 0

# get the number of page
source = requests.get("https://thiendia.com/diendan/forums/gai-goi-hang-cao-cap-ha-noi.197/").text
soup = BeautifulSoup(source, 'lxml')
last_page = soup.find('div', class_='PageNav')['data-last']

for i in range(int(last_page)):

    source = requests.get(f"https://thiendia.com/diendan/forums/gai-goi-hang-cao-cap-ha-noi.197/page-{i+1}").text
    soup = BeautifulSoup(source, 'lxml')
    
    posts = soup.find_all('div', class_='thumbnailContainer')

    for post in posts:

        # get the content of a post
        link = post.find('a', class_='PreviewTooltip')['href']
        post_source = requests.get('https://thiendia.com/diendan/' + link).text
        post_content = BeautifulSoup(post_source, 'lxml')

        # get the image_url
        source_content = post_content.find(
            'blockquote', class_="messageText SelectQuoteContainer ugc baseHtml")
        images = source_content.find_all('img', class_='bbCodeImage LbImage')
        for image in images:
            image_url = image['src']
            if "https://greenupload.com/" in image_url:
                count += 1
                print(image_url)
                csv_writer.writerow([image_url])

csv_file.close()
print(count)
