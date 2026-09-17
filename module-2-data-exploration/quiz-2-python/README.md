# Quiz 2: Visualizing Data

ASM 532 - Module 2 - Lecture 2.3

Create a graph using Matplotlib

This quiz is a mock up of a line chart

## The Data

Average Monthly Temperature by US State is loaded into a variable `df`.

Source: Justin Wong, [Average Monthly Temperature by US State](https://www.kaggle.com/datasets/justinrwong/average-monthly-temperature-by-us-state), Kaggle, compiled from NOAA NCEI [Climate at a Glance: Statewide Mapping, Average Temperature](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/mapping/110/tavg/202208/1/value). The file is in [`../demos/`](../demos/kaggle-average_monthly_temperature_by_state_1950-2021.csv), trimmed to 1950-2021 to match the quiz (the Kaggle download runs to August 2022).

| index | month | year | state       | average_temp | monthly_mean_from_1901_to_2000 |   centroid_lon |  centroid_lat |
| ----: | ----: | ---: | ----------- | -----------: | -----------------------------: | -------------: | ------------: |
|     0 |     1 | 1950 | Alabama     |         53.8 |                           45.9 | -86.8283719359 | 32.7898321918 |
|     1 |     1 | 1950 | Arizona     |         39.6 |                           41.1 | -111.664418336 | 34.2931098705 |
|     2 |     1 | 1950 | Arkansas    |         45.6 |                           40.4 | -92.4392676639 | 34.8997453322 |
|     3 |     1 | 1950 | California  |         39.4 |                           42.7 | -119.610698951 | 37.2460706736 |
|     4 |     1 | 1950 | Colorado    |         25.2 |                           24.5 | -105.547824721 | 38.9985518194 |
|     5 |     1 | 1950 | Connecticut |         32.5 |                           27.3 | -72.7257060428 | 41.6202863352 |
|     6 |     1 | 1950 | Delaware    |           42 |                           34.8 | -75.4004040929 | 38.8870164548 |
|     7 |     1 | 1950 | Florida     |         64.4 |                           58.3 | -81.7974638723 | 28.6284392647 |
|     8 |     1 | 1950 | Georgia     |         53.5 |                           46.6 | -83.4463418309 | 32.6492290722 |
|     9 |     1 | 1950 | Idaho       |         20.4 |                           22.9 | -114.659382348 | 44.0890895052 |

Table 1: A result from `df.head(10)` showing the first 10 rows of the data

| index | month | year | state         | average_temp | monthly_mean_from_1901_to_2000 |   centroid_lon |  centroid_lat |
| ----: | ----: | ---: | ------------- | -----------: | -----------------------------: | -------------: | ------------: |
| 41462 |    12 | 2021 | South Dakota  |         31.4 |                           25.7 | -100.230507516 | 44.4361607025 |
| 41463 |    12 | 2021 | Tennessee     |           48 |                           43.3 | -86.3433803654 | 35.8429870949 |
| 41464 |    12 | 2021 | Texas         |         58.2 |                           50.8 | -99.3506971451 | 31.4844643819 |
| 41465 |    12 | 2021 | Utah          |         36.8 |                           31.5 | -111.678216374 | 39.3237947509 |
| 41466 |    12 | 2021 | Vermont       |         31.2 |                           26.8 | -72.6626493581 | 44.0751958252 |
| 41467 |    12 | 2021 | Virginia      |         45.2 |                           41.1 | -78.8122544727 | 37.5150238913 |
| 41468 |    12 | 2021 | Washington    |         34.7 |                           33.6 | -120.446866425 | 47.3809688818 |
| 41469 |    12 | 2021 | West Virginia |         41.8 |                           37.6 | -80.6137119661 | 38.6425987436 |
| 41470 |    12 | 2021 | Wisconsin     |         29.3 |                           24.9 | -90.0116942643 | 44.6380301915 |
| 41471 |    12 | 2021 | Wyoming       |         31.3 |                           24.8 | -107.551454075 |  42.999642032 |

Table 2: A result from `df.tail(10)` showing the last 10 rows of the data

## The task

Create a line chart showing Indiana average monthly temperature starting from 1970.

## Step 1: Filter raw data

In this step, use Pandas commands to filter data that will be used to create a chart.

**R1** Provide your filtering logic in English.

**R2** Translate the logic in R1 into Python (Pandas) commands.
Noted: You can assume that the Pandas library and data is loaded

```python
import pandas as pd

df = pd.read_csv(....) # data ia loaded
```

## Step 2: Create a chart using Matplotlib

**R3** Draft a mock up chart on the blank canvas below. Add components that you think they are necessary (e.g., title and axis label). Do not worry about the chart's data. You won't be graded based on the correctness of the chart.

**R4** Use Matplotlib commands to create a chart from data from **R2** and chart's components from **R3**.

Noted: You can assume that the Matplotlib is loaded.

```python
import matplotlib.pyplot as plt

```

## What is in this folder

| File                           | What it is                                                |
| ------------------------------ | --------------------------------------------------------- |
| [handout](quiz-2-handout.md)   | The skeleton handed out in class, with blanks to fill in. |
| [solution](quiz-2-solution.md) | The worked solution.                                      |
