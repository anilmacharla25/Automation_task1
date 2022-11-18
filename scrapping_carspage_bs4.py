#scrape the data from carspage.ca
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
url='https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7' #first page link
page=requests.get(url)
print(page)
soup=BeautifulSoup(page.text,'lxml')
print(soup)
posts=soup.find_all('div',class_='media soft push-none rule')
print(len(posts))
df=pd.DataFrame({'web_link':[''],'car_name':[''],'desc':[''],'price':[''],'color':[''],'km_travelled':[''],'dealer_info':['']})
c=0
while True:
    for post in posts:
        car_html=post.find('h4',class_='hN')
        car_name=car_html.text.strip()
        web_link=car_html.find('a').get("href")
        try:
            desc=post.find('h5',class_='hN grey')
            desc=desc.text
        except:
            desc='Not Mentioned'
        price=post.find('strong',class_='delta').text.strip()
        colour=post.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        km_travelled=post.find_all('div',class_='grey l-column l-column--small-6 l-column--medium-4')[0].text.strip()
        dealer_info=post.find('hgroup',class_='vehicle__card--dealerInfo').text.replace('Buy From Home Options','').strip()
        df=df.append({'web_link':web_link,'car_name':car_name,'desc':desc,'price':price,'color':colour,'km_travelled':km_travelled,'dealer_info':dealer_info},ignore_index = True)
        print(df)
    next_page=soup.find('a',{'title':'Next Page'}).get('href')
    next_page_full='https://www.carpages.ca'+next_page
    page=requests.get(next_page_full)
    print(page)
    print('-------------------------')
    soup=BeautifulSoup(page.text,'lxml')
    c+=1
    if c==10:        
        df.to_excel(saving_path)
        break
    

