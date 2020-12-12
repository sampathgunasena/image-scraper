import requests
from selenium import webdriver
import bs4 as bs

url = "https://www.yourURL.com/"


driver = webdriver.Chrome()
driver.get(url2)
soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
driver.close()
l = soup.find_all("a", class_="gal_title expp")
print(len(l))

for i in range(0,len(l),2):

    print(l[i]["title"])

##stages = driver.find_elements_by_class_name('expp')
##driver.close()
