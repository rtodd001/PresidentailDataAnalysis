# CS 105 Final Project
#### Team Lollipop
- Simran Purewal, SID: 862086140
- Ronan Todd, SID: 861228848
- Wesley DeVore, SID: 862081656


### Table of Contents
- [Main Objectives](#main-objectives)
- [Product Specification](#product-specification)
- [Dependencies](#dependencies)
- [Sprint 1 Data Scraping](#sprint-1-data-scraping)
- [Sprint 2 Data Cleaning & EDA](#sprint-2-data-cleaning--eda)
- [Sprint 3 Data Analysis](#sprint-3-data-analysis)

## Main Objectives
We plan to use data in order to analyze President Donald Trump's approval rating and the ongoing Democratic Candidate Race. During our analysis, we answer the following questions:
1. Did the impeachment negatively affect President Trump's approval rating?
2. Has COVID-19 impacted the Democratic Candidate Race?

## Product specification
> For this sprint, you are asked to perform data analysis. This can include building a model to
perform prediction (like applying linear regression or kNN) or clustering. You can also use the
models for data analysis, not just ‘predictions’. For example, in linear regression we saw that the
resulting coefficients tell us how the features are correlated to the target variable. So, this analysis
might help you identify features of importance with respect to a target feature in the dataset.


## Dependencies 
### Scrapy
In order to perform web scraping, we use Scrapy. Linux and macOS users can run the below command to install: 
```
sudo pip3 install Scrapy
```
### scikit-learn
To run the modeling and prediction algorithms, we use scikit-learn. Linux users can run the below command to install: 
```
sudo pip3 install -U scikit-learn
```
macOS users can run this command instead:
```
pip install -U scikit-learn
```
### Pandas
To run Data Formatting, we use Pandas. Linux and macOS users can run the below command to install: 
```
pip install pandas
```
### Other Software
You will also need software that is able to read a Jupyter Notebook (.ipnyb file)

## Sprint 1 Data Scraping
###### (Due February 16, 2020) Simran and Ronan

For Sprint 1 of the project, we obtain relevant datasets from two different websites: SurveyUSA and FourThirtyEight. 

### SurveyUSA
From SurveyUSA, we scrape four different datasets using Scrapy. Links to the datasets are: (Simi)

- [Either Biden, Sanders, or Warren is in Front in Delegate-Rich California, 45 Days Till Ballots Are Counted](http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&d=1)
- [Interviews Conducted After Democratic Candidate Debate In Atlanta, During Televised Impeachment Hearings on Capitol Hill](http://www.surveyusa.com/client/PollReport_main.aspx?g=0f19d585-788e-4f86-81d0-d09a5e046780&d=1)
- [17 Days till Iowans Caucus, Where Does the Democratic Primary Stand Nationwide?](http://www.surveyusa.com/client/PollReport_main.aspx?g=b4747822-277e-4d2c-b896-eb4e04672c09&d=1)
- [6 High-Profile Democrats All Defeat Dented Donald Trump in General Election 'Today'](http://www.surveyusa.com/client/PollReport_main.aspx?g=5128ee79-1b59-4146-bf80-54906bb24d4b&d=1)

The website also shows all sample results in frequencies instead of counts. For example in one question, the sample size is 5000 but the result show 53% instead of 2650. We have to inspect the page element in depth to find how to scrape the counts instead of frequencies. After digging through the sources, we find that the landing site has two embedded sites that it loads up based on a dropdown menu that chooses between frequency and counts. We feed the embedded count url into the scraper. (Ronan)

The landing url for the first link above is as follows:

> http://www.surveyusa.com/client/PollReport.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&

But the embedded url containing all the data in counts is as follows:

> http://www.surveyusa.com/client/PollReport_main.aspx?g=9634c475-cb54-4a34-ab4b-c0d9a2b82759&d=1

### FourThirtyEight
We also obtain datasets from the website FourThirtyEight, which show live polling data. The data is directly downloaded from their GitHub repository [here](https://github.com/fivethirtyeight/data/tree/master/polls). (Simi) In particular, the datasets we obtain from FourThirtyEight are:
- Presidential Primary Polls
- Presidential General Election Polls
- Presidential Approval Polls

## Sprint 2 Data Cleaning & EDA
###### (Due March 1, 2020) Simran and Wesley

For Sprint 2 of the project, we were required to clean the datasets obtained in Sprint 1 and perform EDA on the relevant data.

### Data Cleaning
SurveyUSA is not very organized and has multiple tables of unique questions. All of the tables have the same name so our robot can not scrape the data in a very meaningful way. Our scraper reads all the tables as one big table. We create a Python script in JupyterLab to clean the data and seperate it into the 34 different tables. Additionally, the tables are multi-indexed but the scraper sees it as data. We have to remove the indeces after running the split script. When reading the data sets for EDA, we must run a re-indexing script. In each survey folder there is one csv file named surveyusa1/2/3/4.csv with the raw data, and 34 other survey_#.csv files with the separated, reordered, and cleaned data.(Wesley)

### EDA
We go through all of our data (from both FourThirtyEight and SurveyUSA), perform EDA on the most relevant data for our topic, and visualize our data using different graphing techniques such as scatterplots and bar graphs. (Simi)

## Sprint 3 Data Analysis
###### (Due March 20, 2020) Simran, Ronan, and Wesley

We are now using the clean data to answer our [Main Objectives](#main-objectives).
### 1. Did the impeachment negatively affect President Trump's approval rating?

We have data of Donald Trump's approval ratings since 2017. We filter the data to the specific timeline of the impeachment process. Let's review the timeline of everything before we start.
 
- December 18, 2020 : Impeached by US HoR
- January 16, 2020 : Passed the Senate
- February 5, 2020 : Acquitted

Simi creates a Linear Regression model to show detailed analysis of the approval rating trend. You can find the Notebook detailing the findings [here](https://github.com/CS-UCR/cs105-prj-phase1-lolli-lolli-lollipop/blob/master/phase_3_simi.ipynb). 

The results of the model shows that there is a trend in Trump's approval rating throughout the House and Senate events. The trend shows a slow but staggered delcine in his approval ratings. The ratings jump from 38% to 50% very quickly, making it difficult to see a definitive change. The model allows us to see the gradual overall decline. 

During the Acquitted process, the trend changes. It is still shaky low 30s to high 40s changes present in the House and Senate phase. However, the model shows that there is a slight increase in his approval ratings. The incline has a smaller slope compared to his impeachment ratings. 

Overall, the changes in his approval ratings were still minimal in the long run. There are moments where the ratings hit an overall low, but the trend still stayed consistent.

### 2. Has COVID-19 impacted the Democratic Candidate Race?

We have been tracking the candidacy throughout the project. However, the number of candidates running have drastically changed since the beginning of the project. We have are focusing on the top two Candidates: Biden vs Bernie. For the full list of candidates that have dropped out of the race, click [here](https://www.google.com/amp/s/people.com/politics/2020-presidential-candidates-who-have-dropped-out/amp/).

Wesley creates a Linear Regression model to show detailed analysis of the candidate polls. You can find the Notebook detailing the findings [here](https://github.com/CS-UCR/cs105-prj-phase1-lolli-lolli-lollipop/blob/master/phase3_wesley.ipynb). While observing the data, we discover that there is an inflection around the beginning of 2020. This coincides with the timeframe of COVID-19 appearing on worldwide media. We decide to investigate California, a strong democratic state. In California, Biden and Bernie show similar support in the beginning of the race. The data shows that Biden had higher numbers than Bernie. Then at the inflection point, around January, Biden starts to lose and Bernie starts to win. Bernie has a strong healthcare stance in his campaign. We believe that due to the pandemic, people are aligning themselves with the candidate with better healthcare support. 

Wesley decided to expand the model to the entire US if the decision is nation-wide. The last two graphs in the Notebook shows a scatterplot of the US polls for Biden vs Bernie. It is clear to see a trend. It is intestring to note that Bernie and Biden have traded approval number through the pandemic. 

We have decided to not do any prediction because it is highly dependent on external factors.
