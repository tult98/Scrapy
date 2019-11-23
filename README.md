# Scrapy

# What is this?
The script to crawler image from website and write it to csv file 

The file scrape.py is script to crawler data from static website. It's mean that when you go in that website. All the DOM loaded at one time

The file scrape is script to crawler data from dynamic website. Especially lazy loading technic. When you come to a website. It not load all website's content at one time. It only loaded the content your monitor can display and when you scroll down. It keep loading html code and display content for you

The first one script only need to use bs4 library to crawler data 

The second one need to combine with selenium library to automatic interact with browser to get all the data of website 

## How to use it?
1. Run `pip install requirements.txt` to install library needed
2.Run `python filename.py` to run script
