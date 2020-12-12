import bs4 as bs
import urllib.request
from selenium import webdriver

prefix = "https://www.yourURL.com/"


#function to gather all collection links-------------------
def col_gatherer(end_num):

    link_list = []
    
    for i in range(end_num+1):

        url = "https://www.yourURL.com/".format(i)
        driver = webdriver.Chrome()
        driver.get(url)
        soup = bs.BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()

        a_elements = soup.find_all("a", class_="gal_title expp")
        
        
        for j in range(0, len(a_elements), 2):

            link_list.append([a_elements[j]["title"], prefix + a_elements[j]["href"]])

    return link_list


#function to gather image links and download them----------------------
def img_gatherer(title, link):

    driver = webdriver.Chrome()
    driver.get(link)
    soup1 = bs.BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    a_elements = soup1.find_all("a", class_="expp")

    link_list = []
    for a in a_elements:

        link_list.append(prefix + a["href"])

##    makeFolder(title)

    for i, link1 in enumerate(link_list):

        image_page = urllib.request.urlopen(link1)
        soup2 = bs.BeautifulSoup(image_page, "html.parser")
        full_link = soup2.find("img", id="mainPhoto")["src"]
        urllib.request.urlretrieve(full_link, "images/{0}/{1}.jpg".format(title, i))

        

##full_list = col_gatherer(10)
##
##for element in full_list:
##
##    img_gatherer(element[0], element[1])






###fishing out the original link for single image----------------------------
##
##image_page = urllib.request.urlopen("https://www.imagefap.com/photo/594211267/?pgid=&gid=8738053&page=0&idx=0")
##
##soup = bs.BeautifulSoup(image_page, "html.parser")
##
##link = soup.find("img", id="mainPhoto")["src"]
##
##
###saving image from link------------------------------------------------------------------------
##
##urllib.request.urlretrieve(url, "1.jpg")
