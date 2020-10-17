import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#Gets the link for getPrices method
def getLink(search):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    link = "https://stockx.com/search?s=" + search

    driver.get(link)

    time.sleep(1)

    html = driver.execute_script("return document.documentElement.outerHTML") #This is what the browser does to execute the javascript on the site, it is a piece of code from js

    sel_soup = BeautifulSoup(html, 'html.parser')

    elink = sel_soup.find('div', class_='tile css-1bonzt1 e1yt6rrx0').find('a').get('href')

    return str(("https://stockx.com/sell" + elink))
   
def getPrices(search):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = getLink(search)

    driver.get(url)

    #so it has a second for the elements to load
    time.sleep(1)

    driver.find_element_by_xpath("/html/body/div[2]/div/div/button[2]").click()

    html = driver.execute_script("return document.documentElement.outerHTML") #This is what the browser does to execute the javascript on the site, it is a piece of code from js

    sel_soup = BeautifulSoup(html, 'html.parser')

    sizes = []
    bids = []
    for size in sel_soup.find_all("div",class_="tile-value"):
        sizes.append(size.get_text())

    for bid in sel_soup.find_all("div",class_="tile-subvalue"):
        bids.append(bid.get_text())
    
    print(url)
    for x  in range(0,len(sizes)):
        print(sizes[x] + " " + bids[x])


getPrices('biohack gs')