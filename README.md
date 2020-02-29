# CS 105 Final Project  

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

We also obtained datasets from the website FourThirtyEight, which shows live polling data. The data was directly downloaded from their GitHub repository [here](https://github.com/fivethirtyeight/data/tree/master/polls).

## Phase 2: Data Cleaning & EDA
###### (due March 1, 2020)

