from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium import webdriver
import time

def init_browser():
  # @NOTE: Replace the path with your actual path to the chromedriver
  executable_path = {"executable_path": "chromedriver.exe"}
  return Browser("chrome", **executable_path, headless=False)


def scrape_info():

  ### LATEST NEWS
  browserss = init_browser()

  url = "https://mars.nasa.gov/news/"
  browserss.visit(url)
  # Scrape page into Soup
  html = browserss.html
  soup = bs(html, "html.parser")

  #news title
  news_title = soup.find_all('div', class_ = 'content_title')[0].text.strip()
  print(news_title)

  #news paragraph
  news_info = soup.find_all('div', class_ = "rollover_description_inner")[0].text.strip()
  print(news_info)
  
   
  
  ### IMAGE MARS
  browsers = init_browser()

  url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
  browsers.visit(url)
  # Scrape page into Soup
  html = browsers.html
  soups = bs(html, "html.parser")

  #image url
  featured_image_urls = soups.find('footer')
  featured_image_urlss = featured_image_urls.find('a')
  featured_image_urlsss = featured_image_urlss['data-fancybox-href']
  featured_image_url = 'https://www.jpl.nasa.gov' + featured_image_urlsss
 
  ### Mars TWEET
  browser = init_browser()
  url = 'https://twitter.com/marswxreport?lang=en'
  browser.visit(url)
  html = browser.html
  souper = bs(html, 'html.parser')
  test = souper.find_all('div', class_ = 'js-tweet-text-container')[0]
  mars_weather = test.find_all('p')[0].text




  returns = {
    "url_image":featured_image_url,
    "news_title":news_title,
    "news_info":news_info,
    "mars_weather":mars_weather
    
  }
  #quit browser
  browser.quit()
  browsers.quit()
  browserss.quit()
 

  #results
  return (returns)

def scrape_infos():
 
  ## Mars Facts
  
  url = 'https://space-facts.com/mars/'
  tables = pd.read_html(url)
  df = tables[1]
  dfsss = df.rename(columns ={0:"",1:"Value"})
  dfssss = dfsss.set_index("")
  marsz = dfssss.to_dict('index')

 
  return marsz


def scrape_hem():
  #Mars Hemispheres
  hemisphere_image_urls = [] 
  hemisphere_titles = []
  for i in range(4):
      browsersss = webdriver.Chrome()
      browsersss.get("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
      time.sleep(5)
      img = browsersss.find_elements_by_xpath('//div[@class="container"]/div[@class="full-content"]/section/*[@id ="product-section"]/div[@class="collapsible results"]/div[@class="item"]/div[@class="description"]/a')
      ranger = img[i]
      blank = ranger.click()
      blank
      time.sleep(5)
      #getting full image urls
      soupers = bs(browsersss.page_source, 'html.parser')
      title = soupers.find('h2', class_ = 'title').text
      query = soupers.find('div', class_='downloads')
      #title = count.find('h3').text
      imgs = query.find('ul')
      img_1 = imgs.find('li')
      img_2 = img_1.find('a')
      img_url = img_2['href']
      hemisphere_image_urls.append(f"{img_url}")
      hemisphere_titles.append(title)
      browsersss.quit()
  
  one = hemisphere_image_urls[0]
  two =  hemisphere_image_urls[1]
  three =  hemisphere_image_urls[2]
  four =  hemisphere_image_urls[3]
  t_1 = hemisphere_titles[0]
  t_2 = hemisphere_titles[1]
  t_3 = hemisphere_titles[2]
  t_4 = hemisphere_titles[3]

  hi = {
      "one":one,
      "two": two,
      "three": three,
      "four":four,
      "t1":t_1,
      "t2":t_2,
      "t3":t_3,
      "t4":t_4
  }


  # quit browser


  return hi