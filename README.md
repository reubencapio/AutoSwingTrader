# AutoSwingTrader
Code structure explanations:

TestCppClient Folder - Contains the code to connect to InteractiveBroker API to send the BUY/SELL signal.
nlp_stocks Folder - Contains the code to crawl news websites for any news regarding the preselected tech stocks
sentiment_analysis.py - Code that uses nltk to get a sentiment analysis of the news that was crawled by the spiders inside nlp_stocks folder
mergeTextFiles - Code that merges the crawled data for easier sentiment analysis processing.
