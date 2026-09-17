# Quiz 2 — Solution & Grading Rubric

**ASM 532 — Module 2 — Lecture 2.3**

**Total: 20 points**

## R1 — Filtering logic in English (4 pts)

**Model answer:** Keep only the rows where `state` equals `"Indiana"` **and** `year` is
greater than or equal to 1970 — that is, 1970 through 2021, all 12 months of each year.
From those rows I will plot `average_temp` on the y-axis against time on the x-axis,
where time comes from combining the `year` and `month` columns.

| Criterion                                                     | Pts |
| ------------------------------------------------------------- | --: |
| States the state condition (`state == "Indiana"`)             |   1 |
| States the year condition (`year >= 1970`, inclusive of 1970) |   1 |
| Identifies `average_temp` as the value to plot (y-axis)       |   1 |
| Identifies `year` + `month` as the time/x-axis                |   1 |

## R2 — Pandas code (4 pts)

**Model answer:**

```python
indiana = df[(df["state"] == "Indiana") & (df["year"] >= 1970)]
```

**Equally correct alternatives:**

```python
indiana = df.query("state == 'Indiana' and year >= 1970")
indiana = df.loc[(df.state == "Indiana") & (df.year >= 1970)]

# chained, also fully correct
indiana = df[df["state"] == "Indiana"]
indiana = indiana[indiana["year"] >= 1970]
```

| Criterion                                                                                                     | Pts |
| ------------------------------------------------------------------------------------------------------------- | --: |
| Correct state condition                                                                                       |   1 |
| Correct year condition (`>= 1970`)                                                                            |   1 |
| Conditions combined correctly — `&` with parentheses, or `and` inside `.query()`, or chained across two lines |   1 |
| Result assigned to `indiana` and is a DataFrame, not a Series                                                 |   1 |

## R3 — Chart mock-up (6 pts)

Grade on the presence of components, **not** on the shape of the drawn line.

| Criterion                                                                   | Pts |
| --------------------------------------------------------------------------- | --: |
| Line chart form — a continuous line, not bars/scatter/pie                   |   1 |
| Descriptive title (e.g. "Indiana Average Monthly Temperature, 1970–2021")   |   1 |
| X-axis has a label naming time (Year / Date / Month)                        |   1 |
| X-axis shows plausible tick values (e.g. 1970, 1980, … 2020)                |   1 |
| Y-axis has a label naming temperature                                       |   1 |
| Y-axis label or ticks show units (°F) and a plausible range (roughly 15–80) |   1 |

## R4 — Matplotlib code (6 pts)

**Model answer (OO style):**

```python
fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(indiana["year"] + (indiana["month"] - 1) / 12, indiana["average_temp"])
ax.set_title("Indiana Average Monthly Temperature, 1970-2021")
ax.set_xlabel("Year")
ax.set_ylabel("Average temperature (°F)")
plt.show()
```

**Model answer (pyplot style):**

```python
plt.figure(figsize=(12, 4))
plt.plot(indiana["average_temp"])
plt.title("Indiana Average Monthly Temperature, 1970-2021")
plt.xlabel("Month index (Jan 1970 = 0)")
plt.ylabel("Average temperature (°F)")
plt.show()
```

**Also accepted:** the Pandas wrapper `indiana.plot(y="average_temp", kind="line")`,
provided the title and both axis labels are set.

| Criterion                                                                                                                                         | Pts |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | --: |
| Calls a line-plotting function (`plt.plot` / `ax.plot` / `.plot(kind="line")`)                                                                    |   1 |
| Plots `average_temp` from `indiana` as the y-values                                                                                               | 1.5 |
| X-values are a sensible time axis (combined year+month, a date column, or the default index) **and** the x-label honestly describes what was used |   1 |
| Title set                                                                                                                                         |   1 |
| Both axis labels set, with units on the y-label                                                                                                   |   1 |
| `plt.show()` — or the figure is otherwise displayed/returned                                                                                      | 0.5 |
