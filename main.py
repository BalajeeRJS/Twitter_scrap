import streamlit as st
import datetime
import twitterscrap
import pandas as pd


#Initializing Variables
diplay_error = False
info_display = False
message = ""

#Setting session state to store results
if 'tweets_list2' not in st.session_state:
    st.session_state['tweets_list2'] = []


#Converting list to dataframe



def scrap():
   final_query=(query_text
   +" "
   +"since:"
   +str(from_date)
   +" "
   +"until:"+str(to_date))
   tweets_list2=twitterscrap.scrap(final_query,limit)
   return tweets_list2

#Uploading to Database
def upload(tweets_list2):
   
        message=twitterscrap.insert_data(query_text,tweets_list2)
        return message
   
       
@st.cache_data
def convert_to_csv(df):
    return df.to_csv().encode('utf-8')
@st.cache_data
def convert_to_json(df):
    
    return df.to_json( orient = 'records').encode('utf-8')

#Comfiguring Streamlit GUI
st.set_page_config(page_title='Twitter Scrapper',page_icon=':hash:',layout='wide')


with st.container():
    
    st.markdown("<h1 style='text-align: center;'>Welcome to Twitter Scrap</h1>", unsafe_allow_html=True)
    buff, col, buff2 = st.columns([1,1,1])
    with buff:
      st.image('Title.jpg',output_format="JPEG")
    with col:
      st.subheader("Please Enter below details")
      query_text = st.text_input(label='Enter Keyword or Hashtag',
                                 placeholder="Enter Keyword or Hashtag")
      
      from_date=st.date_input("From Date",datetime.date(2023, 1, 1))

      to_date=st.date_input("To Date",datetime.date(2023, 1,2))

      limit=st.text_input(label='Enter number of tweets',
                          placeholder="Enter number of tweets")
      
      col1, col2,col3 = st.columns([1,2,1])
      with col1:
       if st.button('SUBMIT'):
          if query_text !="" and limit!="":
           st.session_state['tweets_list2']=scrap()
          else:
             diplay_error=True
      
      with col2:   
       if len(st.session_state['tweets_list2'])!=0 and diplay_error!=True:
         if st.button('UPLOAD TO DATABASE'):
          
          message=upload(st.session_state['tweets_list2'])
          info_display=True
      with st.container():
       if len(st.session_state['tweets_list2'])!=0 and diplay_error!=True:
         file_type = st.radio("Choose File type for download",
                               ('CSV', 'JSON'))
         df = twitterscrap.convert_to_df(st.session_state['tweets_list2'])
         if file_type=='CSV':
            data=convert_to_csv(df)
            st.download_button( label="Download data as CSV",
                               data=data,file_name='Twitter_scrap.csv',
                               mime='text/csv')
         else:
            data=convert_to_json(df)
            st.download_button( label="Download data as JSON",
                               data=data,file_name='Twitter_scrap.json',
                               mime='text/json')
         
          
      with st.container():
        if diplay_error:
                     
          if query_text =="" and limit=="":
              st.error('Please enter Keyword/Hashtag and number of tweets')
          elif query_text=="":
              st.error('Please enter Keyword/Hashtag')
          elif limit=="":
              st.error('Please enter number of tweets')
          else:
              pass
        elif info_display:
          if message=='Successfully uploaded':
              st.success(message)
          else:
             st.error(message)
                                  
with st.container():
    st.subheader("Displaying the results")
    if len(st.session_state['tweets_list2'])!=0 and diplay_error!=True:
        tweets_df2=twitterscrap.convert_to_df(st.session_state['tweets_list2'])
        st.dataframe(tweets_df2)
    else:
        st.markdown("<b>NO RESULTS FOUND</b>",unsafe_allow_html=True)
        
    
      
      
