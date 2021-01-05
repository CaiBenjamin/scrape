from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import bs4
from urllib.request import urlopen
import time
import requests

import sys, os, django    
sys.path.append('/Users/benjamincai/webapp4/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

from scrape.models import pc_parts

#get build urls return list of strings end of the build url
def get_builds(url_page):
        url = url_page
        driver = webdriver.Chrome('./chromedriver')
        driver.get(url)
        time.sleep(20)
        html = driver.page_source
        driver.close()

        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('a'):
                link = link.get('href')
                if(link != None and link[0:3] == "/b/"):
                        build_links.append(link)

#find each part on the build page and return date
def find_p_page():
        build_html = requests.get(build_url).text
        soup = BeautifulSoup(build_html, 'html.parser')
        for tag in soup("img"):
            tag.decompose()

        for tag in soup("class"):
            tag.decompose()

        for link in soup.find_all('a'):
        #       temp = link
                link = link.get('href')
                if(link != None and link[0:9] == "/product/"):
                        # print(link)
                        product_links.append(link)

        link = soup.find_all('div', class_="group__content")
        # with open("read.txt", "w") as text_file:
        #         text_file.write(html)
        
        #three values for div group content first one should be date
        for anchor_tag in link:
                if(anchor_tag != None and isinstance(anchor_tag.contents[0], bs4.element.NavigableString)):
                        date = anchor_tag.contents
                        break
        return date

#Get the date from the build page
def find_date(build_url):
        build_html = requests.get(build_url).text
        soup = BeautifulSoup(build_html, 'html.parser')
        link = soup.find_all('div', class_="group__content")
        # with open("read.txt", "w") as text_file:
        #         text_file.write(html)
        
        #three values for div group content first one should be date
        for anchor_tag in link:
                if(anchor_tag != None and isinstance(anchor_tag.contents[0], bs4.element.NavigableString)):
                        date = anchor_tag.contents
                        break
        return date

#Look for cpu on the product page
def find_parts_page(p_url):
        product_html = requests.get(p_url).text
        soup = BeautifulSoup(product_html, 'html.parser')
        p_array = []
        for link in soup.find_all('a'):
                temp = link
                link = link.get('href')
                if(link != None and link[0:14] == "/products/cpu/"):
                        # print(temp)
                        p_array.append(temp)
        contentA = []
        for anchor_tag in p_array:
                # print(type(anchor_tag.contents[0]))
                if(anchor_tag != None and isinstance(anchor_tag.contents[0], bs4.element.NavigableString)):
                        contentA.append(anchor_tag.contents)
        return(contentA)

def find_product_name(p_url):
        product_html = requests.get(p_url).text
        with open("read.txt", "w") as text_file:
                text_file.write(product_html)
        soup = BeautifulSoup(product_html, 'html.parser')

        # h1class = soup.find_all('', class_="h1")
        # print(h1class) 
        title = soup.find("meta",  property="og:title").attrs['content']
        return title

#Tuple List [part type, part name, date]


list2 = [1001,1002,1003]

for i in list2:
        print(i)
        add_cpus = []
        #First get the /b builds links and put them into an Array
        build_links = []
        if(i == 1):
                get_builds("https://pcpartpicker.com/builds/")
        else:
                url = "https://pcpartpicker.com/builds/#page=" + str(i)
                get_builds(url)
        build_links = list(set(build_links))
        print(build_links)

        #go through parts and store urls in a hash
        unique_urls = set()
        for i in pc_parts.objects.all():
                unique_urls.add(i.unique_url)

        for link in build_links:
                if(not link in unique_urls):
                        build_url = "https://pcpartpicker.com/" + link
                        print(build_url)
                        #product links on the page
                        product_links = []
                        #add to product links
                        # find_p_page()
                        # time.sleep(5)
                        list(set(product_links))
                        time.sleep(40)
                        date = find_p_page()
                        # time.sleep(5)
                        time.sleep(40)
                        p_url = "https://pcpartpicker.com/" + product_links[0]
                        cpu_part = find_parts_page(p_url)
                        time.sleep(40)
                        cpu_name = find_product_name(p_url)

                        type_name_date = [cpu_part, cpu_name,date]
                        add_cpus.append(type_name_date)

                        q = pc_parts(unique_url = link , part_type = cpu_part , part_name = cpu_name, pub_date = date)
                        q.save()



#find <td class="td__component" colspan="2"><h4>Video Card</h4></td>
#find <a href="/product/Nsbkcf/zotac-geforce-gtx-1070-ti-8gb-amp-extreme-video-card-zt-p10710b-10p">
# Zotac GeForce GTX 1070 Ti 8 GB AMP Extreme</a>