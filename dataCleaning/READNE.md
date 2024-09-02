# Codility Test for Data Cleaning using Pandas

You are given a data set called biopics.csv containing information on biographical movies. Your task is to perform some data manipulations on the biopics data.

## Data Overview

The original biopics data are made available by the analytics website FiveThirtyEight. You will be working with a preprocessed version, available for you at biopics.csv. It contains the following columns:

- title￼- the movie's title
- country￼- country of production ￼
- year_release - the year the movie was released
- box_office￼- movie's earning at the box office, in US$ ￼
- type_of_subject - the occupation of the movie's subject or their reason for recognition
- lead_actor_actress￼- the name of the actor or actress who played the subject Instructions

Write a function named process_data() that takes no arguments. The function should load the biopics data (this has been implemented for you), perform data manipulations described below and return a pandas data frame with manipulated data.

Clean up the biopics data:

1. Filter out duplicated rows
2. Rename the variable called box_office￼to earnings￼
3. Filter out rows for which earnings￼are missing (i.e. they are NaN)
4. Keep only movies released in the year 1990 or later
5. Convert the type of type_of_subject￼and country￼to Categorical￼
6. Create a new variable called lead_actor_actress_known￼that is False￼if lead_actor_actress￼is NaN￼and True￼otherwise
7. Update earnings￼such they they are expressed in millions of dollars, instead of dollars
8. Reorder the columns in the data frame such that they are in the following order: title, year_release, earnings, country, type_of_subject, lead_actor_actress, lead_actor_actress_known￼
9. Sort the rows in descending order by earnings.

On top of the Python Standard Library, you can make use of any function from the pandas￼packages.
