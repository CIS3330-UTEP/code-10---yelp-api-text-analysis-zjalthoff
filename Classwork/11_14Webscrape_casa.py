from bs4 import BeautifulSoup
import requests
import pandas as pd

# Collecting Name, Title, address, Phone, and Email

web_url = 'https://www.utep.edu/business/people/faculty-profiles.html'

page_to_scrape = requests.get(web_url) #get HTML from site

soup = BeautifulSoup(page_to_scrape.text,'html.parser') #putting HTML into text and parse w/ HTML

info_tags = soup.findAll('div',attrs={'class':'infoCol'}) #find all w/ tag 'div' and class 'infoCol'
professor_list = []

for tag in info_tags:
    professor = {}
    professor['name'] = tag.find('h3',attrs={'class':'name'}).text
    professor['Title'] = tag.find('span',attrs={'class':'Title'}).text

    if tag.find('span',attrs={'class':'address'}) is not None:
        professor['address'] = tag.find('span',attrs={'class':'address'}).text
    else:
        professor['address'] = 'N/A'
    
    if tag.find('span',attrs={'class':'phone'}) is not None:
        professor['phone'] = tag.find('span',attrs={'class':'phone'}).text
    else:
        professor['phone'] = 'N/A'

    if tag.find('span',attrs={'class':'email'}) is not None:
        professor['email'] = tag.find('span',attrs={'class':'email'}).text
    else:
        professor['email'] = 'N/A'
    
    professor_list.append(professor)

prof_df = pd.DataFrame.from_dict(professor_list)
prof_df.to_csv("COBA_Professor_info.csv",index=False) #do not want index in the file itself

# # For CASA scrape some other element/s and save into csv file (Due Midnight)