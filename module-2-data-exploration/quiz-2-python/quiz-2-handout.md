# Quiz 2: Visualizing Data

**ASM 532 — Module 2 — Lecture 2.3**

Name:

**Total: 20 points**

Closed book. No computers or internet. The Pandas and Matplotlib cheat sheets are the only materials allowed.

## The data

A DataFrame `df` holding **Average Monthly Temperature by US State** is already loaded.
Assume `pandas as pd` and `matplotlib.pyplot as plt` are already imported.
Temperatures are in degrees Fahrenheit (°F). Each row is one state in one month of one
year; the data covers 1950–2021.

`df.head(5)`

| index | month | year | state      | average_temp | monthly_mean_from_1901_to_2000 | centroid_lon | centroid_lat |
| ----: | ----: | ---: | ---------- | -----------: | -----------------------------: | -----------: | -----------: |
|     0 |     1 | 1950 | Alabama    |         53.8 |                           45.9 |   -86.828372 |    32.789832 |
|     1 |     1 | 1950 | Arizona    |         39.6 |                           41.1 |  -111.664418 |    34.293110 |
|     2 |     1 | 1950 | Arkansas   |         45.6 |                           40.4 |   -92.439268 |    34.899745 |
|     3 |     1 | 1950 | California |         39.4 |                           42.7 |  -119.610699 |    37.246071 |
|     4 |     1 | 1950 | Colorado   |         25.2 |                           24.5 |  -105.547825 |    38.998552 |

_Table 1: first 5 rows_

`df.tail(5)`

| index | month | year | state         | average_temp | monthly_mean_from_1901_to_2000 | centroid_lon | centroid_lat |
| ----: | ----: | ---: | ------------- | -----------: | -----------------------------: | -----------: | -----------: |
| 41467 |    12 | 2021 | Virginia      |         45.2 |                           41.1 |   -78.812254 |    37.515024 |
| 41468 |    12 | 2021 | Washington    |         34.7 |                           33.6 |  -120.446866 |    47.380969 |
| 41469 |    12 | 2021 | West Virginia |         41.8 |                           37.6 |   -80.613712 |    38.642599 |
| 41470 |    12 | 2021 | Wisconsin     |         29.3 |                           24.9 |   -90.011694 |    44.638030 |
| 41471 |    12 | 2021 | Wyoming       |         31.3 |                           24.8 |  -107.551454 |    42.999642 |

_Table 2: last 5 rows_

<!-- Add space for printing -->

<br><br><br><br><br><br><br><br><br><br><br><br><br>

## The task

Produce a **line chart of Indiana's average monthly temperature from January 1970
through December 2021** — one data point per month, time running along the x-axis.

---

## Step 1 — Filter the raw data

**R1 (4 pts)** In plain English, describe the filtering logic you need: which
rows do you keep, and which column(s) will you actually plot?

```














```

**R2 (4 pts)** Translate R1 into Pandas code. Store the result in a variable
named `indiana`.

```python












```

<!-- Add space for printing -->

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>

## Step 2 — Create the chart with Matplotlib

**R3 (6 pts)** Sketch a mock-up of your chart with necessary components in the frame below. You are
graded on the **chart components you include** (title, axis labels etc), _not_ on the accuracy of the line you draw.

```























```

**R4 (6 pts)** Write the Matplotlib code that turns `indiana` (from R2) into
the chart you sketched in R3. Include everything needed to display it.

```python





















```
