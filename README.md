# CS 105 Final Project

- [Dependencies](#dependencies)
- [Main Objectives](#main-objectives)
- [Phase 1 Data Scraping](#phase-1-data-scraping)
- [Phase 2 Data Cleaning & EDA](#phase-2-data-cleaning--and-eda)
- [Phase 3 Data Analysis](#phase-3-data-analysis)

## Dependencies 
In order to use the web scraper, run the below command for Linux:
```
sudo pip3 install Scrapy
```
To run the modeling and prediction algorithms, run the following command for Linux:
```
sudo pip3 install -U scikit-learn
```
For macOS:
```
pip install -U scikit-learn
```
You will also need software that is able to read a Jupyter Notebook (.ipnyb file)


## Main Objectives
- Did the impeachment negatively affect Donald Trump's approval rating?
- Has COVID-19 impacted the Democratic Candidate Race?

## Phase 1 Data Scraping
###### (Due February 16, 2020) Simran and Ronan

For Phase 1 of the project, we scrape four different datasets from the website SurveyUSA using Scrapy. Links to the datasets are:

http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&d=1
http://www.surveyusa.com/client/PollReport_main.aspx?g=0f19d585-788e-4f86-81d0-d09a5e046780&d=1
http://www.surveyusa.com/client/PollReport_main.aspx?g=b4747822-277e-4d2c-b896-eb4e04672c09&d=1
http://www.surveyusa.com/client/PollReport_main.aspx?g=5128ee79-1b59-4146-bf80-54906bb24d4b&d=1

The website also shows all sample results in frequencies instead of counts. For example in one question, the sample size is 5000 but the result show 53% instead of 2650. We have to inspect the page element in depth to find how to scrape the counts instead of frequencies. After digging through the sources, we find that the landing site has two embedded sites that it loads up based on a dropdown menu that chooses between frequency and counts. We feed the embedded count url into the scraper.
The landing url for the first link above is as follows:

http://www.surveyusa.com/client/PollReport.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&

But the embedded url containing all the data in counts is as follows:

http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&d=1

We also obtain datasets from the website FourThirtyEight, which show live polling data. The data is directly downloaded from their GitHub repository [here](https://github.com/fivethirtyeight/data/tree/master/polls).

## Phase 2 Data Cleaning and EDA
###### (Due March 1, 2020) Simran and Wesley

SurveyUSA is not very organized and has multiple tables of unique questions. All of the tables have the same name so our robot can not scrape the data in a very meaningful way. Our scraper reads all the tables as one big table. We create a Python script in JupyterLab to clean the data and seperate it into the 34 different tables. Additionally, the tables are multi-indexed but the scraper sees it as data. We have to remove the indeces after running the split script. When reading the data sets for EDA, we must run a re-indexing script. In each survey folder there is one csv file named surveyusa1/2/3/4.csv with the raw data, and 34 other survey_#.csv files with the separated, reordered, and cleaned data.

We go through all of our data (from both FourThirtyEight and SurveyUSA), perform EDA on the most relavent data for our topic, and visualize our data using different graphing techniques such as scatterplots and bar graphs.

## Phase 3 Data Analysis
###### (Due March 20, 2020) Simran, Ronan, and Wesley

For Phase 2 of the project we fixed some issues with the data collection, then cleaned the data and started performing EDA on it.

The data was being collected in percentages when we should have been getting counts, so Ronan worked on modifying our collection to grab the correct data.

The data cleaning is done by Wesley in notebooks located in each surveyusa folder, the script cleans the data to look like the tables we got them from, using multi-indexing from the pandas library to sort the data with multiple headers so it is more convenient to work with and perform analysis on.

The EDA is done in the phase2 notebook, Simi and Wesley worked on performing EDA on the president_polls.csv file and the surveyusa files.
