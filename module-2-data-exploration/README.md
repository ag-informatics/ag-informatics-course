# Module 2: Data Exploration

## About This Module

In this module, we'll use the "data lifecycle" as a means to navigate the domain data landscape. The emphasis will be on learning how to formulate domain-specific data science questions and to conduct exploratory data analysis.

**1. Domain fluency: the agricultural data landscape**
What kinds of public data exist, who produces them, how to access them, and how to judge whether a dataset can answer a question you actually care about.

* What is data, and what makes agricultural data its own problem?
* Where does public ag data come from, and how do you get it?
* How do you tell whether a dataset is fit for your question?
* Goal: Be able to find, assess, and acquire data for a domain problem.

**2. Technical fluency: exploring data in a notebook**
A Python refresher, and the data notebook as a way of *exploring* data before committing to working with it.

* What does the Python data stack do for you?
* Why explore in a notebook rather than a script?
* How do you go from a question to pseudocode to working analysis?
* Goal: Be able to conduct an exploratory data analysis and visualise what you find.

## Course Materials

Lecture materials including handouts, demos, and quizzes.

- [Lecture 2.1](lecture-2.1.html)
- [Lecture 2.2](lecture-2.2.html) - Graded in-class activity ([handout](handouts/handout-data-problem.html))
- [Lecture 2.3 demo](demos/demo-plotting-notebook.ipynb) and [Quiz 2](quiz-2-python/README.md)
- [Lecture 2.4](lecture-2.4.html) - Quiz 2 answers, and the [choosing charts and Datasaurus Dozen demo](demos/demo-choosing-charts-notebook.ipynb)

Cheatsheets:
- [Custom Python cheatsheet for this module](handouts/cheatsheet-python.md)

### Lab 2

**[Lab 2: Data Notebook](lab-2-data-notebook/README.md)** - find a dataset for a problem you care about, assess whether it fits, and explore it in a Jupyter notebook. Instructions, prework and submission details are in the lab subfolder, along with:

- [`lab-2-skeleton.ipynb`](lab-2-data-notebook/lab-2-skeleton.ipynb) - the notebook template you work in, one section per step.
- [`aglandvalues-clean.csv`](lab-2-data-notebook/aglandvalues-clean.csv) - US agricultural land values by state, 1997-2023.
  The default dataset, for anyone not bringing their own.

Each lab has a specific AI use policy, specified in the lab itself. 
As a reminder, the overarching AI policy is available in the main repository [README](../README.md).

If you are a Purdue ASM 532 student: Check Brightspace for current instructions, due dates, and other submission details.

## Rubrics

Total: 30 (5 in-class activity + 5 quiz + 20 lab).

### In-class activity 2 — 5 pts

Activity 2, run during Lecture 2.2: framing your own data science question and identifying a dataset for it.

| Points | Criteria |
| --- | --- |
| 0 | Missed |
| 2 | Incomplete — doesn't have to be "right" |
| 5 | Complete - doesn't have to be "right"! |

### Quiz 2 — 5 pts

Pseudocode + python to produce a data visualization, cheat sheet on-hand.

### Lab 2 — 20 pts

Find and assess the suitability of public data for a specific problem, then create and use a data
notebook to analyse it. Bring your own dataset, or use one of the provided alternatives.

* Git Commits — 4 pts
    * 1 pt for each of 4 commits.
* Revised plan — 2 pts (STEP 7)
    * Picks up from what was done in lecture — dataset selected and question formulated.
* Final notebook — up to 14 pts
    * Acquire (STEP 8) — 2 pts. Provenance recorded, plus a fitness judgement: three data quality dimensions that matter for the question, and at least one the dataset fails.
    * Process (STEP 9) — 3 pts. Size, types, missingness, duplicates, and a cleaned file with the decisions written down. Students on the provided dataset verify it is clean and show how they know.
    * Analyze (STEP 10) — 5 pts. The bad first plot and what's wrong with it, then 2-3 visualizations, one grouped/compared and one bringing in a second variable.
    * Prove you could get it again (STEP 11) — 2 pts. The data re-requested with code, and one number matching between the download and the API pull.
    * Share and use (STEP 12) — 2 pts. What the data supports, what it doesn't, and which assumptions a reader needs.

## References

See `CREDITS.md` for image sourcing/attribution and non-image reference citations used in this module's slides and lab.

## License
This work by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

<!-- ## Revision History -->
