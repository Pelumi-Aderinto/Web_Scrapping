import requests
import pandas as pd
from bs4 import BeautifulSoup as BS

url = "https://www.theguardian.com/au"
extracting_data = requests.get(url).text
wiki_data = BS(extracting_data, 'html.parser')

Headlines = []      # I will be scrapping the news headline, story link and contents; 3 parameters
links = []
story =[]
storys = []
data = []       # Creating empty lists to hold our data
i=0             # I created this int to serve as an iterator to iterate through the 'links' list and get the article contents for each link by incrementing it in every for loop

for news in wiki_data.findAll('div' , {'class':'fc-item__container'}): # This is the tag where the headline and link is contained
    datum = {} # An empty dict to hold the the scapped data
    Headlines.append(news.text.replace('\n',''))
    links.append(news.a['href'])
    page = requests.get(links[i])
    Object = BS(page.content) 
    for storyss in Object.findAll('div', {'class':'article-body-commercial-selector'}):# This is the tag to get the story content for each of the links
        story.append(storyss.text.replace('\n',''))
    
    if len(story) != i+1:
        story.append('No Story Available')

    datum['Headlines'] = Headlines[i]
    datum['Links'] = links[i]
    datum ['Story'] = story[i]
    
    data.append(datum) #The final list holding all of our data
    i+=1
    
df = pd.DataFrame(data)
df.to_csv('./Scrapped_data.csv')
