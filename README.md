# Project_1_Twitter_Scraper
Scrapping Data from Twitter based on user input.

# Requirements
I used snscrape, pymongo, pandas, streamlit, datetime modules for this project.
snscrape: snscrape is used to scrape the data from the social media. From Twitter it scrapes things like user, id, content, likescount, retweetCount, hashtags,etc.
  pip3 install snscrape --> used to install snscrape package in python.
pymongo is used to connect python with mongodb database.
  pip3 install pymongo  --> used to install pymongo package in python.
Pandas is used to create a dataframe. 
  pip3 install pandas  --> used to install pandas package in python.
Streamlit is used to create a web application.
  pip3 install streamlit  --> used to install streamli package in python.

# To get user inputs
sntwitter.TwitterSearchScraper(Text) used to scrape the data from twitter.
To get User input
     text=st.text_input('Enter the Search_keyword') 
     until_date=st.text_input('Until: YYYY-MM-DD')    
     since_date=st.text_input('Since: YYYY-MM-DD')
     scrapped_data = sntwitter.TwitterSearchScraper(text+' '+'until:'+until_date+' '+'since:'+since_date).get_items()
     
     for i in scrapped_data:
    # appending 'date','id','url','content','user','replyCount','retweetCount','lang','source','likeCount' attributes scrapped from twitter
          a.append(i.date)
          b.append(i.id)
          c.append(i.url)
          d.append(i.content)
          e.append(i.user)
          f.append(i.replyCount)
          g.append(i.retweetCount)
          h.append(i.lang)
          x.append(i.source)
          y.append(i.likeCount)
          count=count+1
          if count>=int(limit_range):
              break

    
  
  



