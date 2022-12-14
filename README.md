# Web_Scrapping
A coding challenge

## DETAILS AND EXPLANATION OF THE PROBLEM AND MY APPROACH TO THE SOLUTION

### PROBLEM STATEMENT
1. Write an application to crawl an online news website, e.g. www.theguardian.com/au or www.bbc.com using a crawler framework such as [Scrapy] (http://scrapy.org/). You can use a crawl framework of your choice and build the application in Python.
2. The appliction should cleanse the articles to obtain only information relevant to the news story, e.g. article text, author, headline, article url, etc. Use a framework such as Readability to cleanse the page of superfluous content such as advertising and html
3. Store the data in a hosted mongo database, e.g. compose.io/mongo, for subsequent search and retrieval. Ensure the URL of the article is included to enable comparison to the original.
4. Write an API that provides access to the content in the mongo database. The user should be able to search for articles by keyword

### APPROACH TO SOLUTION
1. Addressing the first problem and using the beautifulsoup framework in python, I crawled an online news website(www.theguardian.com/au)
2. After crawling the website and getting raw html tags, I then cleansed and processed it to be able to obtain the news headline, links to story and the content of the story.
3. I hosted a mongo database on Atlas (cloud mongodb) and connected to it with my python sdk and insert the cleansed data in step 2 to it.
4. I then wrote wrote an API to provide access to the content in the mongo database and also deployed it on heroku for public access. 
So I created two endpoints(or routes) and then made them publicly accessible on heroku. The first one which is the default("https://evening-badlands-93116.herokuapp.com/") route gives access to all the content of the database while  (https://evening-badlands-93116.herokuapp.com/find?keyword=<>) returns the details about the Headline relating to the keyword searched.
Let's see for example

  i.   [link here](https://evening-badlands-93116.herokuapp.com/) gives access to the entire content of the database.

  ii.  [link here](https://evening-badlands-93116.herokuapp.com/find?keyword=Ministers) gives access to a specific information for a certain searched keyword('Ministers') in the headlines story. You can replace this search term with anything of your choice you wish to know about.
  
  Users can then search for their article of choice and get the necessary details by including the keyword they are interested in after the heroku link as a search tag as seen in the hyperlinks above.
  
  The Procfile and the requirement.txt files are required files to use HEROKU to be able to make my API written in "api_mong.py" publicly accessible.



### MAJOR CHALLENGE(S) FACED
1. I was unable to scrap all data story effectively as not all hyperlinks led to a page with contents to scrap. Some links led to videos which kept on breaking my 'for' loop code midway and I was only able to scrap as many as my code could output before the breakage with youtube links.



