
# Twitter Scraping 

This is Streamlit web app for Scraping Twitter.It scrapes the twitter data for the given hashtag/keyword in a specific date range using snscrape library.The retrieved tweets are uploaded in MongoDB and can be dowloaded as CSV or JSON file.

## Tech Stack

**Language:** Python\
**Libraries:** Snscrape, pandas, pymongo\
**NoSQL Database:**: MongoDB\
**GUI Framework:** Streamlit

## Scraping the tweet

The TweetSearchScrape() method in Snscrape python library is used to retrieve the Twitter data. The method is passed with a query string containing the hashtag/keyword and the search dates (From start date to end date).

## Uploading data in MongoDB

Tweets that are retrieved using the Snscrape library is inserted into the MongoDB database by establishing the client connection.

## Creating the UI

 Streamlit framework is used for creating the GUI for Twitter Scraping.It is used to create search textbox,submit button and dispalying the tweets.

## How app works ?

**Step-1**  
Enter hashtag/keyword to be searched in search textbox.

**Step-2**  
Specify the date range between which tweets need to retrieved from Twitter.

**Step-3**  
Enter the number of tweets to be retrieved from Twitter and click 'SUBMIT' button.

**Step-4**  
The retrieved data are displayed in results section.

**Step-5** <br>
If the retrieved data needs to be uploaded to database, click 'UPLOAD TO DATABASE'.

**Step-6** <br>
Retrieved data can be downloaded in CSV/JSON format using 'DOWNLOAD' button.

## Database Configuration
Please replace with  your own **Username**,**Password** and **Mongodb Connection** string in **twitterscrap.py** file while running the code.
![image](https://user-images.githubusercontent.com/116367662/224507490-f7762817-aaeb-450c-8df9-d11eefb8f84a.png)


## Command to run the code

cmd --> streamlt run main.py


## Reference docs
 - [Streamlit docs](https://docs.streamlit.io/)
