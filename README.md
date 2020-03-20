# CS 105 Final Project  

## Dependencies


Main Objectives
- Did the impeachment negatively affect Donald Trump's approval rating?
- Has COVID-19 impacted the Democratic Candidate Race?


Our final project for CS 105 was split up into three phases:

- Phase 1: Data Scraping
- Phase 2: Data Cleaning & EDA
- Phase 3: Analysis & Conclusions


## Phase 1: Data Scraping
###### (due February 16, 2020)

For Phase 1 of the project, we scraped four different datasets from the website SurveyUSA using Scrapy and cleaned them. Links to the datasets are:

http://www.surveyusa.com/client/PollReport.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759
http://www.surveyusa.com/client/PollReport.aspx?g=0f19d585-788e-4f86-81d0-d09a5e046780
http://www.surveyusa.com/client/PollReport.aspx?g=b4747822-277e-4d2c-b896-eb4e04672c09
http://www.surveyusa.com/client/PollReport.aspx?g=5128ee79-1b59-4146-bf80-54906bb24d4b

The website is not very organized, and all of the tables were named the same thing so our robot could not scrape the data in a very meaningful way. After scraping the data, we created a Python script in JupyterLab to clean the data and seperate it into the 34 different tables that were originally found on the website. In each survey folder there is one csv file named surveyusa1/2/3/4.csv with the raw data gathered, and 34 other survey_#.csv files with the separated, reordered, and cleaned data.

The website also showed all sample results in frequencies instead of counts. For example, the sample size was 5000 but the result showed 53% instead of 2650. We had to inspect the page element in depth to find how to scrape the counts instead of frequencies because the url for both were the same. After digging through the sources, we found that the landing site has two embedded sites that it loads up. We found the url for the embedded count data and fed that to our scraper.

We also obtained datasets from the website FourThirtyEight, which shows live polling data. The data was directly downloaded from their GitHub repository [here](https://github.com/fivethirtyeight/data/tree/master/polls).

## Phase 2: Data Cleaning & EDA
###### (due March 1, 2020)

For Phase 2 of the project, we managed to get the SurveyUSA datasets in counts instead of percentages and performed further cleaning to the newly obtained datasets. We then went through all of our data (from both FourThirtyEight and SurveyUSA), performed EDA on the most relavent data for our topic, and visualized our data using different graphing techniques such as scatterplots and bar graphs.

## Phase 3: Data Analysis
##### (Due March 20, 2020)
=======
For Phase 2 of the project we fixed some issues with the data collection, then cleaned the data and started performing EDA on it.

The data was being collected in percentages when we should have been getting counts, so Ronan worked on modifying our collection to grab the correct data.

The data cleaning is done by Wesley in notebooks located in each surveyusa folder, the script cleans the data to look like the tables we got them from, using multi-indexing from the pandas library to sort the data with multiple headers so it is more convenient to work with and perform analysis on.

The EDA is done in the phase2 notebook, Simi and Wesley worked on performing EDA on the president_polls.csv file and the surveyusa files.
