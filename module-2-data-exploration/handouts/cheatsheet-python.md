# Python Reference

ASM 532 - Module 2 - Custom Cheatsheat

---

Everything here is `pandas`, `numpy`, `matplotlib` or `requests` - the four libraries in Lab 2.

## Anatomy of a call

```
landuse.Item.unique()
└──┬───┘ └┬─┘ └──┬───┘
 the     the   the method. The () are required,
dataframe column even when nothing goes inside.
```

Read it left to right: start with a thing, narrow it down, then do something to it.
Anything with `()` on the end **does** something. Anything without, like `.shape`, just
**reports** something.

---

## Getting started

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
```

`as pd` is a nickname, so you write `pd.read_csv()` instead of `pandas.read_csv()`.
These four nicknames are near-universal - use them and any example you find online will match.

## Reading data in

| Call | Reads |
| --- | --- |
| `pd.read_csv('data/file.csv')` | A CSV file. The usual one. |
| `pd.read_csv('file.csv', skiprows=3)` | Same, ignoring 3 junk lines above the header. |
| `pd.read_excel('file.xlsx')` | An Excel spreadsheet. |
| `pd.read_json('file.json')` | A JSON file. |

```python
agland = pd.read_csv('data/faostat-aglanduse-world.csv')
```

The result is a **dataframe**: one observation per row, one variable per column.

## Looking at what you've got

Do these *before* you plot anything. Every one of them answers a question you will
otherwise guess at.

| Call | Tells you |
| --- | --- |
| `df` | The whole thing (Jupyter shows the top and bottom). |
| `df.head()` / `df.tail()` | First / last 5 rows. `df.head(20)` for more. |
| `df.shape` | `(rows, columns)`. No `()`. |
| `df.info()` | Every column, its type, and how many values are non-empty. |
| `df.describe()` | Count, mean, min, max, quartiles - numeric columns only. |
| `df.columns` | The column names. |
| `df.dtypes` | The type of each column. `object` usually means text. |
| `df.Item.unique()` | Every distinct value in that column. |
| `df.Item.value_counts()` | Every distinct value, and how often each appears. |
| `df.isna().sum()` | How many values are missing, per column. |

```python
agland.Value.describe()      # stats for one column
agland.describe()            # stats for every numeric column
```

## Picking out rows and columns

**One column** - two ways, same result:

```python
agland['Value']              # always works
agland.Value                 # shorter, but breaks if the name has a space
```

**Several columns** - note the double brackets:

```python
agland[['Year', 'Value']]
```

**Rows that match a condition.** The bit inside the brackets is a true/false test,
one answer per row; you get back the rows that answered true.

```python
forest = landuse[landuse.Item == 'Forest land']
europe = forest[forest.Area == 'Europe']
```

| Test | Means |
| --- | --- |
| `df.Area == 'Europe'` | equal to. **Two** equals signs. |
| `df.Value > 1000` | greater than. Also `<`, `>=`, `<=` |
| `df.Area != 'World'` | not equal to |
| `df.Area.isin(['Asia', 'Africa'])` | is one of these |
| `df.Value.isna()` | is missing |

Stack conditions with `&` (and) / `|` (or). **Each condition needs its own brackets:**

```python
subset = landuse[(landuse.Area == 'Europe') & (landuse.Year > 2010)]
```

## Summarising

```python
agland.Value.mean()          # one number
agland.groupby('Area').Value.mean()          # one number per Area
agland.groupby('Area').Value.describe()      # full stats per Area
```

`groupby` is *split, then measure*: split the rows into groups by a column, then run the
measurement on each group separately.

| Call | Gives |
| --- | --- |
| `.mean()` `.sum()` `.count()` | average, total, how many |
| `.min()` `.max()` | smallest, largest |
| `.sort_values('Value')` | sorted rows. Add `ascending=False` for biggest first. |
| `.reset_index()` | turns a groupby result back into a normal dataframe |

## Cleaning

| Call | Does |
| --- | --- |
| `df.dropna()` | Drops rows with missing values. `axis=1` drops columns instead. |
| `df.drop(columns=['Domain', 'Flag'])` | Drops columns you name. |
| `df.drop_duplicates()` | Drops repeated rows. |
| `df.Value.astype(float)` | Converts a column's type - text to number, usually. |
| `df.Value.str.replace(',', '')` | Text surgery. Strips the commas out of `"3,500"`. |
| `df.to_csv('clean.csv', index=False)` | Saves your work. `index=False` skips the row numbers. |

Assign the result, or it does not stick:

```python
agland = agland.dropna()                 # yes
agland.dropna()                          # no - throws the result away
```

Numbers that arrived as text will not plot. `df.dtypes` tells you; `.astype(float)` fixes it -
but strip the junk out first, or the conversion fails.

---

## The shape of a plot

```
fig, ax = plt.subplots(figsize=(10, 6))
└┬┘  └┬┘                       └──┬───┘
 │    │                    width, height in inches
 │    │
 │    └─ the AXES - one set of x/y axes. The data is drawn here.
 └────── the FIGURE - the whole picture. Can hold several axes.
```

Almost everything you want is a method on `ax`. Start every plot this way.

```python
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(agland['Year'], agland['Value'])
plt.show()
```

`plt.show()` goes last. In Jupyter it draws the figure; without it you may get a line of
machine output above your plot.

## Plot types

| Call | Draws | Use it for |
| --- | --- | --- |
| `ax.plot(x, y)` | Line | Something changing over time |
| `ax.scatter(x, y)` | Dots | Two variables against each other |
| `ax.bar(labels, values)` | Vertical bars | Comparing categories |
| `ax.barh(labels, values)` | Horizontal bars | Same, with long category names |
| `ax.hist(values, bins=20)` | Histogram | The spread of one variable |
| `ax.pie(values, labels=labels)` | Pie | Parts of one whole. Few slices only. |

**Line, with the options you will actually want:**

```python
ax.plot(europe['Year'], europe['Value'], marker='x', label='Europe')
ax.plot(asia['Year'], asia['Value'], marker='o', label='Asia')
ax.legend()
```

Call `ax.plot()` once per series, give each a `label`, then call `ax.legend()` once at the end.

**Pie, as run in class:**

```python
explode = (0.1, 0.1, 0.1, 0.1, 0.1)      # nudge each slice out. One number per slice.
ax.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
ax.axis('equal')                          # keeps it a circle, not an oval
```

`autopct='%1.1f%%'` prints the percentage on each slice to one decimal place.

## Labelling a plot

An unlabelled plot does not count as an answer.

| Call | Sets |
| --- | --- |
| `ax.set_title('...')` | The title above the plot |
| `ax.set_xlabel('...')` / `ax.set_ylabel('...')` | The axis labels. **Include the units.** |
| `ax.legend()` | The key. Needs `label=` on each series. |
| `ax.grid(axis='y')` | Gridlines. `'x'`, `'y'`, or leave empty for both. |
| `ax.set_ylim(4400, 5000)` | Zoom the y axis to a range. Also `set_xlim`. |
| `ax.ticklabel_format(style='plain')` | Stops big numbers turning into `4.4e6`. |
| `ax.tick_params(axis='x', rotation=45)` | Angles crowded x labels so they fit. |

## Saving a plot

```python
plt.savefig('forest-by-continent.png', dpi=140, bbox_inches='tight')
```

Before `plt.show()`, not after - showing it clears the figure. `bbox_inches='tight'` stops
labels being cut off at the edge.

---

## Getting data from an API

```python
r = requests.get('https://api.weather.gov/alerts/active')
r.status_code            # 200 means it worked
data = r.json()          # the response, as Python dictionaries and lists
```

A JSON response is nested dictionaries and lists. Walk down one level at a time:

| Call | Gives |
| --- | --- |
| `data.keys()` | The names available at this level |
| `data['features']` | The value stored under that name |
| `data['features'][0]` | The first item in a list. Counting starts at 0. |
| `len(data['features'])` | How many items |
| `pd.json_normalize(data['features'])` | Flattens the list into a dataframe |

Sending options along with the request:

```python
params = {'commodity_desc': 'CORN', 'year': '2025', 'format': 'JSON'}
r = requests.get(url, params=params)
```

## numpy, briefly

`pandas` is built on `numpy`, so most of the time you are using it without noticing.
Directly, you need it for:

```python
values = np.array([168.4, 172.1, 159.8])
values.mean()            # also .std(), .min(), .max(), .sum()
np.isnan(values).any()   # any missing values?
```

An array holds one variable. A dataframe holds a whole table.

---

## From plan to code

Write the plan first, in plain English, as comments. Then fill in the code under each line.
The plan is worth marks on its own, and it is how you work out that a step is missing before
you have written anything.

```python
# read the land use csv
# keep only the rows for forest land
# keep only Europe
# plot value against year, as a line
# label both axes and give it a title

landuse = pd.read_csv('data/faostat-landuse-continents.csv')
forest = landuse[landuse.Item == 'Forest land']
europe = forest[forest.Area == 'Europe']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(europe['Year'], europe['Value'], marker='x')
ax.set_xlabel('Year')
ax.set_ylabel('Forest land (1000 ha)')
ax.set_title('Forest land in Europe, 1961-2019')
plt.show()
```

---

## When it goes wrong

| Message | Usually means |
| --- | --- |
| `KeyError: 'Value'` | No column by that name. Check `df.columns` - spelling, capitals, stray spaces. |
| `FileNotFoundError` | The path is wrong. It is relative to where the notebook sits. |
| `NameError: name 'pd' is not defined` | The import cell has not been run this session. |
| `TypeError: unsupported operand` | You are doing maths on text. Check `df.dtypes`. |
| `ValueError: could not convert string to float` | Junk in the column - `(NA)`, `(D)`, commas. Clean, then convert. |
| Empty plot, no error | Your filter matched no rows. Check `.shape` on the subset. |

*Comments:* `# like this` in Python.
