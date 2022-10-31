import pandas as pd
import pymongo
import snscrape.modules.twitter as sntwitter
import streamlit as st
from datetime import datetime
# Empty list used to append the scrapped data
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
x=[]
y=[]
count=0

st.set_page_config(page_title='Twitter Scraper ')

st.markdown('# Twitter Scraper')

text=st.text_input('Enter the Search_keyword')                    #User input to scrape the data from twitter

col1,col2,col3=st.columns(3)

with col1:
    until_date=st.text_input('Until: YYYY-MM-DD')        # Getting date inputs 
    Until_date=str(until_date)
with col2:
    since_date=st.text_input('Since: YYYY-MM-DD')
    Since_date=str(since_date)
with col3:
    limit_range=st.text_input('Limit_range: number')

# Session _state to keep the values
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked=False

def callback():
    st.session_state.button_clicked = True

if (st.button('Submit', on_click=callback) or st.session_state.button_clicked):


    if len(text) == 0:
        st.error('Please Enter search_keyword', icon="🚨")

    else:
        if len(until_date) == 0 or len(since_date) == 0 or len(limit_range) == 0:
            st.error('Please Enter range', icon="🚨")
        else:
            st.write('Entered Search_keyword is :'+' '+ '\"'+ text + '\"'+ ' ' + 'Until:' + '\"'+ Until_date + ' ' + '\"'+ 'Since:' + '\"'+ Since_date +'\"')
            scrapped_data = sntwitter.TwitterSearchScraper(text+' '+'until:'+Until_date+' '+'since:'+Since_date).get_items()

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

            # Create a dataframe with date, id, url, tweet content, user,reply count, retweetCount,language, source, like count.
            data = {'date': a, 'id': b, 'url': c, 'content': d, 'user': e, 'replyCount': f, 'retweetCount': g, 'lang': h,
                    'source': x, 'likeCount': y}

            df = pd.DataFrame(data)  # converting the list into dataframe

            # Converting the dataframes Column object into string. In streamlit Conversion failed for column user with type object

            df[['url', 'content', 'user', 'lang', 'source']] = df[['url', 'content', 'user', 'lang', 'source']].astype('string')

    st.dataframe(df)

    st.download_button("Download CSV",df.to_csv(),file_name='Twitter_data.csv',mime='text/csv')      # To download the dataframe as a csv file

    cd = df.to_json()                              # converting the dataframe into json document

    st.download_button('Download json', cd, file_name='Twitter_data.json',mime='application/json')   # To download the dataframe as a json file

    # Uploading the scrapped data into database
    if st.button("Upload into Database"):
        now = datetime.now()                  # current time
        timestamp1 = datetime.timestamp(now)  # converting the datetime object into a timestamp
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Twitter_database"]  # Creating a database named 'Twitter_database'
        mycol = mydb["Twitter_datas"]  # Creating a collection named 'Twitter_datas'
        key = text + str(timestamp1)  # concatenating search_keyword with timestamp to make it as a keyword for the database document
        # eg:({“text+current Timestamp”: [{1000 Scraped data from past 100 days }]})
        x = mycol.insert_one({key: [cd]})  # Inserting the datas which is stored in a variable 'c' with help of created key
        st.write('Data uploaded successfully')


