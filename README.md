# Predicting Homelessness in the US 
__Description:__ <br>
In the United States, homelessness is a significant problem, most importantly, for the people who experience it. In this study, we examine the factors that contribute to making individuals and families more likely to experience homelessness. <br> <br>
__Central Question:__ <br>
What are the most important factors that contribute to people experiencing homelessness?
## Data 
Source: HUD.gov <br>
PIT and HIC Data Since 2007 <br>
Date Published: March 2021
### Description
These raw data sets contain Point-in-Time (PIT) estimates and national PIT estimates of homelessness as well as national estimates of homelessness by state and estimates of chronic homelessness from 2007 - 2020. Estimates of homeless veterans are also included beginning in 2011. The accompanying Housing Inventory Count (HIC) data is included as well from 2007 - 2020.
### Features
25,228 rows, 93 columns (x9 datasets for the years 2012 - 2020) <br>
Key demograohic features in the PIT include: <br>
* Age group
* Gender Identity
* Race/Ethnicity
* Location 
<br> <br>
Key Homeless Shelter information in the HIC include: <br>
* Location
* County 
* Number of beds
* Type of shelter
* Number of available beds
## Exploratory Data Analysis
![2020 counts](Users/nicolacave/dsi_galvanize/capstones/capstone2/predicting_us_homelessness/images/2020_counts.png)
## Modeling
Model used: Multiple Linear Regression <br>
__Process:__ <br>
Feature Engineering > Model Training > Model Testing > Hyperparameter Tuning > Kfold Cross Validation(5)
## Results
__What can we learn from the model?__
R^2 on training data: 0.575 <br>
R^2 on testing data:  0.399 <br> <br>
__This model is insufficient!__ <br> <br>
__Cross validation verifies this.__ <br>
mean fold score: -1.11e+17 <br>
![feature importances](Users/nicolacave/dsi_galvanize/capstones/capstone2/predicting_us_homelessness/images/key_feature_importances.png) <br>
__The most important predictors of homelessness are: Gender Identity, Race/Ethnicity, Age Group (significantly less)__
## Discussion
__How can this model be improved?__<br>
Further studies: <br>
* Collect more robust demographic data 
* Improve feature engineering 
* Expand targets 
* Add classifiers 
* __More data!__ <br> <br>
__Ideal Use Case:__ <br>
Provide insight to county-wise HUD sectors to inform funding for  homeless shelters



