# Module 2, Lab 2: Data Notebook

## Orientation

### Exploring data!

**Data** are observations that someone, or something, recorded. Data are properties of objects or events. 

**Datasets** are collections of observations, made by particular people, for particular reasons, under particular conditions. Before you decide to use a dataset, you should figure out what those particularities are, and assess if and how they might influence your overarching data science question.

The act of poking-around-the-data is called **Exploratory Data Analysis (EDA)**. EDA is a process through which a data worker, including data scientists, inspect, clean, structure, and otherwise prepare their data as ingredients to cook with. 

> In this lab, you will find a dataset of interest, explore it in a Jupyter notebook, and explain what you found. 

### Maintaining a data "lab" notebook

A **Jupyter notebook** belongs to the data exploration genre of software. It runs code in small snippets, shows the code output next to the source code, and allows you to go back and forth between steps. It's built for the job of exploration! It is not just a "script".

> Your Jupyter notebooks can serve as a lab notebook. That is, a place for you to track what you did, why you did it and what you learned. In your notebook, you can think through the problem, write down what you're learning, try out things and note interesting preliminary findings worth pursuing. By committing your notebook to your code repository regularly, you can maintain a "log" of your data exploration. It's a great idea to keep a lab notebook, even for data work!

Your Jupyter notebook - documentation + code - is the deliverable of this lab. Documentation is NOT decoration. Documentation is rationale for your decisions, whether for you 6 months from now, or a collaborator next week. Explaining your reasoning as you work through the problem allows you to keep track of decisions when they are fresh. This is the "meta" stage of the lifecycle.

### Working in Python
Python is a general-purpose programming language that is commonly used in data science. There are MANY possible libraries that one can import into a Python project. In this lab, we'll only work with general purpose data libraries for data processing and analysis.

**pandas** will hold your data as a table that you can filter, group, and summarize. It has one observation per row, and one variable per column. **numpy** does the numerical work inside pandas. **matplotlib** makes plots and graphs and other data visualizations. **requests** will let you programmatically acquire data using an API. 

That's it, that's the stack!

## AI Use Policy for this Lab

Across these learning modules, we will move through three levels of AI-assisted programming (see [course readme](../../README.md) for details).

This lab involves:

> **No AI-generated code.** (Modules 1-3 default.) Do not use AI tools to generate code for this lab — hand-crafting code is the point. Discussion/ideation with AI is fine per the general Academic Integrity policy; writing your code is not.

## BEFORE THE LAB

Do this **before** the lab session. If your environment is not working, you lose the lab session to setup rather than to data, and the in-class code-along in Lecture 2.3 will not run for you either.

### STEP 0: Identify and fill your knowledge gaps

#### Start thinking about your data

You are choosing your own dataset for this lab. The **public data sources** slide in Lecture 2.2 is the place to start looking. You don't need to have decided before the lab — we'll work on framing your question in class — but arriving with a topic you actually care about will make the whole lab better.

#### Python intro / refresh

If you are not familiar with Python, or need a quick refresher, do this 30 minute [Short Introduction to Programming in Python](https://datacarpentry.github.io/python-ecology-lesson/01-short-introduction-to-Python) by the Data Carpentry.

Here are basic tutorials for each of the packages this lab uses. The two in **bold** are the ones worth doing before you arrive; the rest are reference.

1. [Jupyter notebook](https://jupyter.org/): An interactive Python environment that lets you run and view code alongside your notes. This is where the whole lab happens.

   - We'll do a quick demo in class.
   - **Go through this quick tutorial: [Jupyter Notebooks](https://datacarpentry.github.io/python-ecology-lesson/jupyter_notebooks).**
   - Full documentation: <https://jupyter-notebook.readthedocs.io/en/stable/>.

2. [Numpy](https://numpy.org/): Python package for scientific computing. We're mostly going to use pandas and matplotlib, so the other materials cover what you need to know about numpy.

3. [Pandas](https://pandas.pydata.org/): Python package for data analytics. It's got an R/Matlab style feel to it.

   - **Go through this [10 minute introduction to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html).**
   - Full documentation: <https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html>.

4. [Matplotlib](https://matplotlib.org/): Python package for data visualization.

   - [Quick start guide for matplotlib](https://python-graph-gallery.com/matplotlib/).
   - You can consult the Data Carpentry [Introduction to Matplotlib](https://datacarpentry.github.io/python-ecology-lesson/08-putting-it-all-together).
   - Full documentation: <https://matplotlib.org/stable/>.

5. [Requests](https://requests.readthedocs.io/en/latest/): Python package to make HTTP requests. You'll need this only if your dataset comes from an API. Read "Make a Request" from [this tutorial](https://requests.readthedocs.io/en/latest/user/quickstart/).

### STEP 1: Install Python

We are using VS Code and a virtual environment only.

If you have not installed Python before, install Python 3.12 or newer:

- **Windows:** install via the Microsoft Store, or download from <https://www.python.org/downloads/windows/>
- **macOS:** download the installer from <https://www.python.org/downloads/macos/>
- **Linux:** Python is usually installed by default. If your distribution doesn't have it, install from source: <https://www.python.org/downloads/source/>

You should already have VS Code from Lab 1. If not, install it from <https://code.visualstudio.com>.

### STEP 2: Understand why we use a virtual environment

Software is evolving constantly. Python, for example, releases a new version annually. New versions come with new features, and at the same time, some existing features will be changed, deprecated, or removed. This applies to over 100,000 Python libraries. This can cause incompatibility issues between Python and the other libraries required to run the code. For example:

- You try to run code that you (or a colleague who graduated and left) wrote a few years ago.
- You try to run your code on another machine, like a high performance computer.

To prevent this, it is highly recommended to create a virtual environment and record a list of required libraries. That way you can be sure you have the correct set of libraries whenever you need to run the code again.

`venv` creates a local virtual environment specific to one project, which makes it fast and keeps each project's libraries separate. VS Code has built-in support that makes it straightforward.

> This is not busywork: it is the same reasoning as the **Documentation** and **Data Management** parts of the data lifecycle. An analysis nobody can re-run is an analysis nobody can check.

### STEP 3: Create your environment

1. Create a new file named `requirements.txt` in your lab folder, and paste in the following:

```text
numpy==2.5.*
pandas==3.0.*
matplotlib==3.11.*
requests==2.34.*
jupyter==1.1.*
```

2. Open the command palette in VS Code (**View → Command Palette**), then type `Python: Create environment`.
3. Choose `venv`.
4. Choose your Python version. If you have several, choose the latest.
5. Select the `requirements.txt` you created in step 1 as the dependency file.

VS Code will create a virtual environment in a `.venv` folder and install everything listed. If you would rather do this manually:

```bash
# macOS and Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```bash
# Windows
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

A `.venv` folder is machine-specific and easy to regenerate, so it is good practice **not** to commit it to GitHub. Create a file named `.gitignore` in your repository and add a line reading `.venv`.

### STEP 4: Install the VS Code extensions and select your kernel

You need the **Python** and **Jupyter** extensions from Microsoft. Open the Extensions panel (ctrl/cmd + shift + x), search for each, and install.

Then, with a notebook open, click **Select Kernel** in the top right and choose the `.venv` environment you just created. **This is the step that most often goes wrong** — if your notebook can't find pandas, this is almost always why.

![Screenshot of VS Code with a Jupyter notebook open. On the left, the Extensions panel shows the Microsoft Jupyter extension highlighted and labelled "Install extension". On the right, the "Select Kernel" button in the notebook toolbar is highlighted and labelled "Activate kernel".](img/vscode-0.png)

### STEP 5: Check that it works

Before you finish, make a new notebook, run this in a cell, and confirm you get version numbers rather than an error:

```python
import pandas as pd
import matplotlib
print(pd.__version__, matplotlib.__version__)
```

If that runs, you are ready for the lab. If it doesn't, bring it to office hours or the start of lab — don't spend the lab session on it.

---

## LAB INSTRUCTIONS

Work through these in your copy of [`lab-2-skeleton.ipynb`](lab-2-skeleton.ipynb).

- **Your dataset, your choices.** The steps say what to produce, not which function to call.
- **No dataset of your own?** Use `aglandvalues-clean.csv` in this folder — US agricultural land values by state, 1997-2023. Bring a *problem* to it as well as a file: pick something you would want to know from land values, and frame that.
- **Markdown is graded work.** Every step ends with you saying what you found.
- **Every code cell starts with your plan, written as comments.** What you intend to do, in order, in plain English — then the code under it. This is the "function designs" step in the course AI policy, and it is what makes a notebook yours.

Check Brightspace for the deadline. Steps 10-12 build on Lecture 2.3, so leave them until after it.

### STEP 6: Set up your lab repository and notebook

- Your private `YOURNAME-ASM532-Labs` repo from Lab 1, one folder per lab — make a `lab2` folder.
- Add `@tame0001` as a collaborator if you have not already.
- Copy `lab-2-skeleton.ipynb` into your `lab2` folder and rename it `lab2-YOURNAME.ipynb`.
- Copy `aglandvalues-clean.csv` across too if you plan to use it.
- Open it in VS Code, select your `.venv` kernel (see STEP 4), confirm a cell runs.
- Commit and push. **That is commit 1.**

### STEP 7: Understand and plan — what is your question?

- Markdown only, no code.
- The revised version of your Lecture 2.2 worksheet — start from the handout, not from scratch.
- The problem, who has it, and why it matters.
- The actors, and what they are trying to do.
- **Your question, in one sentence.**
- What would count as an answer.
- What changed since the handout — contact with a real dataset always changes something.

### STEP 8: Acquire — get your data, and record where it came from

- Get the file into your `lab2` folder, commit it, and load it into a dataframe.
- **Record the provenance in markdown** — source, URL, date retrieved, terms of use.
- Say what actually arrived: format, rows, columns, anything surprising.
- **Judge whether it fits.** Name the three data quality dimensions from Lecture 2.2 that matter most for your question, and say how your dataset does on each. **At least one should be a dimension it does badly on** — every dataset fails something, and saying which is the skill.
- Worth looking at: `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`.
- Will not load? It is usually the delimiter, the encoding, or preamble rows above the header.

### STEP 9: Process — what is in here, and what is broken?

Five questions. Answer each in code, then say what you found.

- **How big is it, and how big should it be?** — `.shape`, `.info()`, `.head()`, `.tail()`
- **Is every column the type it should be?** — `.dtypes`, `.describe()`, `type()`. Numbers stored as text sort wrong and will not plot.
- **What is missing, and how is "missing" spelled here?** — `.isna().sum()`, `.value_counts()`, `.unique()`, `.str.contains()`. `NaN` is one spelling; `(NA)`, `(D)`, `(S)`, `-999` and an empty string are others.
- **Anything duplicated, or out of order?** — `.duplicated()`, `.sort_values()`, `.reset_index()`
- **Clean it, and keep the raw file.** — `.dropna()`, `.drop()`, `.astype()`, `.str.strip()`, `.to_csv()`. Save under a new name; check the shape again afterwards.
- Then: one line per decision, saying what you changed and why.

**Using `aglandvalues-clean.csv`?** It has already been cleaned — the name says so. Your job for this step is to **verify that, and show how you know**: run the same five questions, and report what you checked and what came back clean. A dataset someone hands you as "clean" still has to be inspected before you trust it, and that inspection is exactly the same work.

### STEP 10: Analyze — what does it look like?

- **Plot it badly first.** Whole thing, no styling, no subsetting. Then say what is wrong with it — that sentence is the point of the step.
- Then **two or three visualizations chosen for your question**, using the chooser slides from Lecture 2.4.
- One must involve a **comparison or grouping**.
- One must bring in a **second variable**, with a sentence on what the pairing shows.
- Titles, axis labels, legends. Save each plot as a file and commit it.
- Worth looking at: `.groupby()`, `.mean()`, `plt.subplots()`, `ax.set_xlabel()`, `ax.legend()`, `plt.savefig()`.

### STEP 11: Prove you could get it again

- A download needs a human. An API does not — so it can be repeated, scheduled, and checked. The acquisition slide asked: *can I get this again next year, the same way, and prove it?* This is where you answer.
- **If your dataset has an API:** re-request the data you analysed in STEP 10, with code instead of clicking. **Show one number matching** between your downloaded file and the API pull. That match is the proof.
- **If it does not:** use the National Weather Service active alerts feed instead — <https://api.weather.gov/alerts/active>, no key, no account. Then add one line: what would you have to do to turn that response into a dataframe like the one you already have?
- Either way, show that you can: make the request and confirm it worked; turn the response into something Python can navigate; reach one specific value several levels down.
- Worth looking at: `requests.get()`, `.status_code`, `.json()`, `.keys()`, `pd.json_normalize()`.

### STEP 12: Share and use — what can you say, and what can you not?

- Markdown only, no code.
- What you can say from this data, with confidence.
- What you **cannot** say — what would a reader be wrong to conclude from your plots? Start from the thing you named in class that this dataset would not let you answer.
- Which cleaning assumptions a reader needs to know about.
- Who would use this, and what they would need next.

### Optional exercises

- Not graded. In the skeleton notebook, at the end.
- Install and use a package that is not in `requirements.txt` (`yfinance`, for commodity and stock prices).
- Clean the raw version of the ag land values file yourself — the one in this folder was cleaned for you.
- **Two y-axes:** put two sources on one plot with `ax.twinx()`, and work out what moves first. Genuinely fiddly, which is why it is here rather than in STEP 10.

## How to Submit your Lab - GitHub + Brightspace

- Push to your private `YOURNAME-ASM532-Labs` repo, in the `lab2` folder:
  - `lab2-YOURNAME.ipynb`, running top to bottom with no errors — restart the kernel and run all before you submit
  - your raw data file, and your cleaned data file under a different name
  - every plot you made, saved as an image file
- **4+ commits**, each with a message saying what changed and why.
- Then submit the repo link on Brightspace. Check Brightspace for the deadline.

### Academic Integrity Reminder

<!-- Submission Policy snippet — see documentation/SNIPPETS.md, edit there first -->

**I will trust that you are doing the right thing, unless I see evidence to the contrary.**

**Your private ASM532 assignment repositories will contain one folder per lab.** Make sure you keep this repo private for the duration of the course. This will also prevent others from copying your code, while still letting you share your code's history with us.

**For each lab, you should have 4+ "commits" to your repo.** For example, you'll push your code at the beginning and end of each lab — but since it's good practice to commit between major changes, I hope you'll end up with more than 4 commits! Don't commit your entire lab 5 minutes before the deadline — we'll check your commit history to assess your version control skills.

**Each commit should have a meaningful commit message that explains how/why you changed your code.** For example, if you'd just written the code to render a graph of your processed data, your commit message could read something like: "used matplotlib to plot corn commodity prices over time for 5 states. yay!"

## License

This work by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
