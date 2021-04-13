# GUI-Twitter-Scraper
This is a simple GUI that allows users to scrape twitter data easily. This uses SnScrape as the base scraper and Tkinter as the GUI.


# Requirements
You must have SnScrape, Tkinter, and Pandas installed


# Usage
This program will allow you to download any historical tweets from Twitter, and you can set several parameters. In the example below, I want to download 500 tweets with the keyword "Lava" that were posted in January 2020, and were posted in Houston, TX. I want the CSV file that the tweets get written too to be named "LavaTweets." I did not specify who I wanted tweets from. If you want to specify who to get tweets from, please enter their @ tag (for instance, if you wanted to download the tweets of Nate Silver, you should enter "NateSilver538" no apostrophe). You also have the option to download retweets or not. You have the option of not filling in parameters if they do not matter to you by just leaving the space blank. If there are not as many tweets with specific parameters that you requested, you will simply get all the tweets that fit that parameter. For instance, if you request one billion tweets with the keyword "table" from user elonmusk, you will not get one billion tweets. When you have filled in all your parameters, you should press "Get Tweets" and the program will start. Updates of the scraping progress will be printed every 100 tweets. For each tweet, you will get the full text of the tweet, the time the tweet was posted, the username of the tweeter, the language the tweet is in, the self-reported location of the user, and the tweet ID, which can be used for futher hydrating.

![Screenshot_56](https://user-images.githubusercontent.com/68095150/114622169-9e8ec800-9c7b-11eb-8f34-a655cccce08f.png)


# Issues
This was created to help people very new to python scrape Twitter data in an easy and accessable way. Feel free to contact me about any issues or changes you think I should make, or with more general questions about Twitter datamining.
