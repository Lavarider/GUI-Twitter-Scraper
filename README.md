# GUI-Twitter-Scraper
This is a simple GUI that allows users to scrape twitter data easily. This uses SnScrape as the base scraper and Tkinter as the GUI.


# Requirements
You must have SnScrape, Tkinter, and Pandas installed


# Usage
This program will allow you to download any historical tweets from Twitter, and you can set several parameters. In the example below, I want to download 500 tweets with the keyword "Lava" that were posted in January 2020, and I want the CSV file that the tweets get written too to be named "LavaTweets." You also have the option to download retweets or not. You have the option of not filling in parameters if they do not matter to you by just leaving the space blank. When you have filled in all your parameters, you should press "Get Tweets" and the program will start. Updates of the scraping progress will be printed every 100 tweets. For each tweet, you will get the full text of the tweet, the time the tweet was posted, the username of the tweeter, the language the tweet is in, the self-reported location of the user, and the tweet ID, which can be used for futher hydrating.
![Screenshot_51](https://user-images.githubusercontent.com/68095150/113883738-6d4e5d80-978c-11eb-97ae-06f9b0245ecf.png)

# Issues
This was created to help people very new to python scrape Twitter data in an easy and accessable way. Feel free to contact me about any issues or changes you think I should make, or with more general questions about twitter datamining.

# Future Updates
I plan to add specific user-based scraping, as well as location-based scraping.
