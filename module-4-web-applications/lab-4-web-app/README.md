# Module 4, Lab 4: Web Application

## Orientation

You will design and build a small **data management web application** in Django, with the same two-part workflow we have practiced to date: plan on paper, then build. 
* **Part 1 - Design** turns a real workflow into a plan for an app: follow a real-world THING managed by a user through a task domain. Then, you will scope a web application (a specification), define which web pages are required (a site map), and determine what data is stored and used (a class diagram).
* **Part 2 - Build** turns the web application specification (your plan) into a working Django app: models to represent the system components. Then you will populate your database using a sample dataset and develop your first web page to display this data.

You will stack the languages and skills learned to date. Thus, this lab assumes you can:
* Map user and data workflows to specify a software implementation (Modules 1-3)
* Design and implement a basic website in HTML and CSS, that enables users to navigate and view a web of hyperlinked content (Module 1).
* Design and implement a simple data model in Python and SQL, that reflects your concept model of a user's task domain (Modules 2 and 3).

The web application developed in this lab (Module 4), will be the basis for the next two labs, where you will:
* Develop a series of web pages to facilitate user-data interactions (Module 5)
* Rapidly prototype new ideas, using your web application as a space to tinker with more advanced functionality (Module 6).

> In this lab, you will specify, model, and build a dynamic web application that stores and displays real data.

### The structure of Django

* **Django** is a Python web framework: a skeleton and a toolbox for building web applications (Lecture 4.2). In this section, I'll share a lot of links, but consider these as **references** - not required reading, for this lab. The "BEFORE THE LAB" section links to two specific videos that cover the basics needed for the lab (and reflect what I've got in my lecture materials).

The architecture a Django web app includes: 
* **URLs**: maps the URL (user HTTP request) to the Django app's `views`. These are Python statements in the `urls.py` file.
  * Learn more about the [URL dispatcher](https://docs.djangoproject.com/en/5.2/topics/http/urls/).
* **views**: coordinates user requests to decide which data and templates are required to create a user response. Django Views control the HTML response: they ask `models` to pull the requested data, and render that data using HTML `templates`. These are Python functions in `views.py` file.
  * Learn more about [how to write views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
* **models**: structures data in the database based on your specification. Each `model` is a Python class in the `models.py` file, where methods support interaction with the data itself. CRUD methods are built-in (see also: [Django model queries](https://docs.djangoproject.com/en/5.2/topics/db/queries/)).
  * Learn more about models: [Django models documentation page](https://docs.djangoproject.com/en/5.2/topics/db/models/)
* **templates**: provide a generic web page layout in HTML, and CSS can be used in conjunction with these layouts. Think of these as fill-in-the-blank pages that get filled out by the `view` using answers from the `model`. These HTML pages are stored in the app's `templates/` folder.
  * Learn more about [Django's template language that connects HTML and Django](https://docs.djangoproject.com/en/5.2/topics/templates/).

Two additional files are important to understand the Django structure:
* **settings**: configures the whole project, including which apps it runs. Your app must be listed in `INSTALLED_APPS`, or Django can't find its `models`, `templates`, or static files. These are Python settings in the project's `settings.py` file.
* **admin**: Django's built-in web dashboard to manage your data, without writing any `views`. You register each `model` you want to manage. These are Python statements in the app's `admin.py` file.
  * Learn more about [Django's default database and admin dashboard](https://docs.djangoproject.com/en/5.2/intro/tutorial02/)
  * And here's [how you can configure the admin site](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/)

Django calls this architecture **MTV**: Model-Template-View. The diagram below illustrates one request path.

![Diagram of a Django application. An HTTP request arrives at URLS (urls.py), which forwards it to the appropriate view. The View (views.py) reads and writes data through the Model (models.py), uses a Template (filename.html), and returns an HTTP response as HTML.](img/django-structure.png)

Image source + Learn more: [MDN, Django introduction](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Introduction).

**How do the pieces connect?**
Let's follow one request through the `farmnotes` demo, when someone visits `http://127.0.0.1:8000/farmnotes/1/`:

1. **The request arrives at the project's `urls.py`** (`myapp/myapp/urls.py`). Its line `path('farmnotes/', include('farmnotes.urls'))` passes anything starting with `farmnotes/` to the app.
2. **The app's `urls.py` picks the view** (`myapp/farmnotes/urls.py`). The pattern `<int:field_id>/` matches `1/`, so it calls the `notes` view with `field_id=1`.
3. **The view asks the model for data** (`views.py`). `get_object_or_404(Field, pk=field_id)` fetches field 1, or answers "404 page not found" if there isn't one.
4. **The model talks to the database** (`models.py`). You don't have to write SQL: Django turns `Field` into the table `farmnotes_field` in `db.sqlite3` (via `makemigrations` and `migrate`), and turns each row back into a Python object.
5. **The view hands the data to a template** (`templates/farmnotes/notes.html`). `render()` fills in the template's `{{ field.name }}` variables and `{% for %}` loops.
6. **The response goes back to the browser** as plain HTML, styled by any static files (`static/farmnotes/style.css`).

### Some terms for this module

| Term | Means | Example |
| --- | --- | --- |
| **Function** | Defined with `def`, and called on its own. | `greet("Bessy")` |
| **Method** | A function defined inside a class, and called on an object. Its first argument is `self`. `__init__()` is the constructor method. | `sunny.details()` |
| **Operation** | The design word, from your Lab 3 object model. In code, an operation becomes a method. | "record planting" |
| **View function** | Django's name for a function in `views.py` that answers a web request. | `index(request)` |

## AI Use Policy for this Lab

Across these learning modules, we will move through three levels of AI-assisted programming (see [course readme](../../README.md) for details).

This lab involves:

> **AI for debugging/exploration only.** (Modules 3-5 default.) Write your pseudocode and function outlines by hand first; use AI only to debug, explore alternatives, or ask thoughtful questions once you're stuck — not to generate the initial code.

**What does responsible AI use look like?**

&#129488; **Part 1 - Design** is about a system YOU have followed. Do NOT hand it to an AI: the point is to convey *your* understanding of *your* domain. AI will give you a generic answer for a generic problem.

&#128591; **Part 2 - Build:** write each model, view, and template yourself first. Django errors can be cryptic, so this is where AI can help you *debug*, as in Lecture 4.2:

  1. **Read the error.** The last line of the traceback says *what* went wrong. The preceding lines provide context, i.e., *where* the issue happened.
  2. **Search it.** [The Django docs](https://docs.djangoproject.com/en/5.2/), [Stack Overflow, a popular coder-to-coder forum](https://stackoverflow.com/questions).
  3. **Write the question first.** What you expected, what happened (the full error), the smallest code that still breaks and its file, and what you already tried. Best practices for asking a good question are similar for asking people and when interacting with AI systems. Some specific guidance is available via the StackOverflow community:
     * [How to ask a good (programming) question](https://stackoverflow.com/help/how-to-ask).
     * [How to create a minimal, reproducible example](https://stackoverflow.com/help/minimal-reproducible-example) - key to debugging!

  4. **Ask to understand, then verify.** Ask "why is this failing?", not "fix this". Ask for a reference you can check. Change one thing at a time.

### &#129302; AI-coding resources

**What can you use?**
1. You can access Github Copilot in VS Code via the free [Student Developer Pack](https://education.github.com/pack). 
2. Purdue Students: check this [Purdue AI webpage](https://www.purdue.edu/ai/enterprise-ai-toolkit/) to find out what you have access to. As of October 6, 2026, this includes Purdue's GenAI studio that contains many open source models, and Google's Gemini Enterprise.
3. Other providers (Anthropic, Google, Microsoft) etc., have assorted offerings that can work in VS Code, but many require a subscription. 

I'll curate and add resources here to support your AI-assisted coding journey:
 * **Try the [AI debugging starter kit](ai-debugging-kit/README.md)** to manage and track your responsible AI use while debugging and exploring. It works with GitHub Copilot or Claude Code in VS Code, or any AI-chat tool.
     * `AGENTS.md` tells your AI tool how to help you: explain, point to the docs, don't write your code, and don't commit, delete, or reset anything without asking.
     * `prompts.md` and `debug-log.md` are your **prompt log** and **debugging log**, each with a sample entry.
 * At minimum, **keep a debugging log:** one entry per bug (the error, what you tried, what fixed it), and the prompts you used. Asking AI to write your models or views for you is cheating yourself out of learning.

## BEFORE THE LAB

### STEP 0: Identify and fill your knowledge gaps

#### Tutorial videos

Watch the following tutorials:

- Introduction to Django: https://cs50.harvard.edu/web/weeks/3/
- SQL, Models, and Migrations: https://cs50.harvard.edu/web/weeks/4/

Then visit the [demos folder](../demos/README.md) for this module. It has the `farmnotes` example project from Lectures 4.2 and 4.4, all of whose code runs. It is highly recommended to install Django and run the demo before starting this lab.

#### Install Django

With your Lab 2 `.venv` active, add Django, pinned to the current long-term support release:

```bash
pip install "django>=5.2,<5.3"
```

#### Set up the AI debugging starter kit

Copy [`AGENTS.md`](ai-debugging-kit/AGENTS.md) to the root of your labs repo, and [`prompts.md`](ai-debugging-kit/prompts.md) and [`debug-log.md`](ai-debugging-kit/debug-log.md) into your `lab4` folder. If you want to use an AI tool in VS Code (GitHub Copilot or Claude Code), set it up now, before you need it: see the [kit's README](ai-debugging-kit/README.md).

#### Diagramming tool

You will draw a class diagram again. 
* You may use the tool you picked for Lab 3 (see Lab 3, STEP 0).
* Alternatively, you may want to explore diagramming in `mermaid` like I show in my lecture slides. It can be a little finicky, so your mileage may vary.
  * You can either read the docs directly, or try out the live editor: [for class diagrams in mermaid, start here](https://mermaid.js.org/syntax/classDiagram.html).

#### Choose your track

Some of you may want to continue working with the data you explored in Module 3. Some of you may want a pre-defined project to focus on skills building. Some of you may want to use this lab and the next two to do some rapid prototype on a completely different project idea. 

**Make this decision by the time you come to LAB.** Stick with it for the rest of this module. You can change your mind next lab. I'll have web app "skeleton code" to help you "reset" and pick up the default-farm track if you run into any issues - i.e., when you start Lab 5 you can begin with my "answer" to Lab 4, but know that my choices may have been different from yours.

##### &#127805; Default-farm track: support agronomy-farm data interactions

Real farm operations data from the [Purdue ACRE / Agronomy Farm](https://ag.purdue.edu/department/agry/acre/index.html), provided in [`data/`](data/). It is messy on purpose: you will import only the columns your classes need, and you may need to clean them first. It was created in partnership with Rachel Stevens, ACRE's farm manager.

##### &#128640; Choose-your-own track: support user-data interactions

Bring your own problem domain and data: the domain you modeled in Lab 3, your research, a job, a family farm or business, or anything else you scope with me first. Your data should be similar in size to the ACRE data (a few hundred rows): an existing dataset, a subsample of one, or a reasonable sample dataset you generate.

Either way, **you will import your data with a fixture file** (STEP 7). 

&#128587; Not sure? Talk to me. I'll help you scope it quickly.

#### Lab submission folder structure

You will be submitting a few different things. Create a folder called **'lab4'**. Create a subfolder called **'images'**. You will be uploading screenshots and diagrams throughout this lab into this folder. You will need to give each image the appropriate filename so that we know what it is. You will also create a README.md file that describes your solution. Use this [Github Markdown Reference Guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to make sure your description is correctly formatted.

```
lab4/
  images/
  <project>/    # Don't create this folder yet, this shows where the Django project you create later will live.
  README.md
```

---

## Part 1 - DESIGN -- in the Lecture 4.3 activity, finish on your own.

### Follow ONE track: default-farm vs choose-your-own

From here on, wherever the two tracks differ, a step has two subsections marked as:

**&#127805; Default-farm track: support agronomy-farm data interactions** 

**&#128640; Choose-your-own track: support user-data interactions**


### STEP 1: Problem Statement

> README.MD: Under the heading "Problem Statement", copy or write your problem statement.

#### &#127805; Default-farm track: support agronomy-farm data interactions

[The Agronomy Farm](https://ag.purdue.edu/department/agry/acre/index.html) (AKA ACRE) is a 1600 acre research and education farm and facility about 7 miles northwest of the Purdue West Lafayette Campus. Over 50 researchers, from 8 departments are running approximately 180 research projects at ACRE, ranging from plant breeding and genetics, to serving as a testbed for digital agricultural technologies. When fields are not in research use, they are put into production, with the ACRE team growing commodity corn and soybean. Rachel Stevens, the farm manager, works with three full-time technicians and a team of seasonal and student labor as needed.

![Three maps of Purdue's Agronomy Center for Research and Education (ACRE) side by side: an aerial imagery map in a frame, a whiteboard field map with handwritten field numbers and colored magnets, and a printed logbook field map with numbered fields totalling 1408 acres.](img/acre-maps.jpg)

**Data Management Challenge:** The farm manager has decades of historical farm operations data per field in logbooks like the one shown below:

![An open ring binder from the ACRE office. The left page is a printed topdress conversion table; the right page is a handwritten field log for field 70, listing dated operations from 2016 to 2018, such as chiseling, planting soybeans, spraying, combining, and spreading fertilizer, each with the worker's name.](img/acre-logbook.jpeg)

The farm manager wants a web application in which all her historical field data resides in a logically structured database that allows for easy searching and exploration of the data. She also wants a password-protected dashboard that her workers can use to input new data into the application. **In this lab, you will create a data management Django web application for the ACRE farm management team.**

#### &#128640; Choose-your-own track: support user-data interactions

Write a short problem statement in the same shape as the ACRE one: whose data, what it is, and what the app should let them do.


### STEP 2: Follow the object (update if needed)

In the Lecture 4.3 activity, you followed one thing through a system, filling in a color-coded card at each station, and then drew a rough **activity diagram** and wrote **use cases**.

#### &#128640; Choose-your-own track: support user-data interactions

If you followed something from another domain in class, repeat the walk for your own domain.

#### Both tracks

> IMAGE UPLOAD: Save a photo of your worksheet with the filename **'worksheet'** inside your **'lab4/images'** folder.

### STEP 3: Write a specification

The specification is the plan for your **minimum viable product (MVP)**: the smallest app that is still useful.

> README.MD: Under the heading "Specification", write:
> 1. **Use cases**: 2-3, each naming who (a role) does what.
> 2. **Functional requirements**: what the app must do, e.g. "a technician can record an operation for a field".
> 3. **Non-functional requirements**: qualities the app must have, e.g. "a worker can find a field's history in under a minute".
> 4. **MVP cut**: which of the above your app will do in this lab, and which wait for later.

### STEP 4: Site map and data model

**The site map.** Draw the pages your app will have, and how they link. Label each page with its **view**, its **template**, and the **model(s)** it shows. For a worked example, see the [farmnotes site map](../demos/README.md#farmnotes-site-map) in this module's demos (also in Lecture 4.4).

**The data model.** Design a data model that considers logical groupings of data entities into Django `classes` and attributes.

#### &#127805; Default-farm track: support agronomy-farm data interactions

Start by looking at the [data](./data/) folder. Consider the first row: on April 24, 2022, Evan used the Hagie STS12 to spray 2-4D round up on field 200. Thus, we can glean the following data from the entry:

- Field number: 200
- Date of operation: 4-24-2022
- Worker: Evan
- What was done: Spraying 2-4D

#### &#128640; Choose-your-own track: support user-data interactions

If you already have a data model for your domain (from Lab 3, for example), start from it. If not, start from your data, as the default-farm track does. Either way, shape the model to what your app now needs to do (your STEP 3 specification).

#### Both tracks

Draw a simplified UML class diagram of the **data model** for your app. Your data model should have the following:

1. Consist of **at least 4 classes**. Use more if your app needs them.
    - For any attribute that is a "look up" list (e.g., a choice from a fixed set of options like operations), you must specify the lookup list.
    - Each class must have a primary key.
2. There must be a relationship between your classes.
    - Relationships will need to be represented through a foreign key attribute.

<!-- H11 resolved 2026-10-06: minimum 4 classes, so the 5-class ACRE reference build (Module 5's starting skeleton) fits. -->

> IMAGE UPLOAD: Save your site map and data model with the filenames **'site-map'** and **'data-model'** inside your **'lab4/images'** folder.

> README.MD: Under the heading "Data Model", do the following:
> 1. Insert the images of your site map and data model.
> 2. Describe what each of the classes represent and how they relate to each other.
> 3. Describe why you chose to model the data in this manner.

> README.MD: Under the heading "Data Dictionary", you will have a table that describes each of the terms in your data model (keep the headings the same). An example of a data dictionary is shown in the table below (yours might be different).

| Variable     | Scope            | Description          | Acceptable Values | Data Type |
| ------------ | ---------------- | -------------------- | ----------------- | --------- |
| field_number | Class            | ACRE field ID Number | >0                | int       |
| field_name   | Field, Attribute | Name of the field    | 50 characters     | String    |

---

## Part 2 - BUILD -- LAB INSTRUCTIONS

### STEP 5: Initialize the Project & Application

Initialize a project, and within it, an app.

#### &#127805; Default-farm track: support agronomy-farm data interactions

Name the project **'acre'** and the app **'acrelog'**.

#### &#128640; Choose-your-own track: support user-data interactions

Name the project and the app for your domain. Use your names wherever this lab says `acre` and `acrelog`.

#### Both tracks

Make sure you create a **'urls.py'** file inside your app, as well as required sub-folders (e.g., for templates).

Create a stub template file called **'index.html'**, and add the corresponding `index` function in **'views.py'**. You will also need to add a route to this file, just like we did in Lecture 4.2. Display a message like "hello world" via your `index` stub to test that you have connected all the pieces together.

Your app folder should look like this:

```
acre/
  manage.py
  acre/
  acrelog/
      migrations/
      templates/
        acrelog/
          index.html
      __init__.py
      admin.py
      apps.py
      models.py
      tests.py
      urls.py
      views.py
  db.sqlite3
```

<!-- Template path changed from templates/index.html to templates/acrelog/index.html, the convention Lecture 4.4 teaches. -->

Start the server and visit http://127.0.0.1:8000/acrelog to confirm that you have a working application.

> IMAGE UPLOAD: Take a screenshot of your working application with the filename **'hello-world'** inside your **'lab4/images'** folder.

### STEP 6: Implement the Data Model

First, implement your models in the **'models.py'**. Run `makemigrations` and `migrate`. Create a couple of test data entries through either the Django API or the admin dashboard as we previously did in class.

> IMAGE UPLOAD: Take a screenshot of your admin dashboard showing that you have successfully created a few data entries in your application. Upload with the filename **'sample-data'** inside your **'lab4/images'** folder.

### STEP 7: Import the data with fixtures

Next, you will need to bulk import your data into your application.

In Django, a ["fixture" file](https://docs.djangoproject.com/en/5.2/howto/initial-data/) can be used to provide initial data to a model. For example, let's say you have a spreadsheet and want to import that data into your Django app, doing it manually would take a long time. Ideally, you'd write a python script to convert the spreadsheet into a "fixture" file, that is a specially marked up data file, that Django then reads to know how and where to put the data.

In your Django app, create a folder called **'fixtures'** and place it in the app directory (so it should be in the same location as **'models.py'**).

In this JSON ["fixture" file](https://docs.djangoproject.com/en/5.2/howto/initial-data/), create the structure shown below. In the code block below, the first entry is a template and the second is an example. BE CAREFUL: the commas, colons, {} and [] brackets are all important! Missing one, can cause the whole thing to break. You can use [this JSON file validation tool](https://jsonlint.com/) to check to see if your JSON file is correctly structured.

```JSON
[
  {
    "model": "myapp.classname",
    "pk": 1,
    "fields": {
      "attribute_name1": "Value",
      "attribute_name2": "Value"
    }
  },
  {
    "model": "myapp.field",
    "pk": 2,
    "fields": {
      "field_id": "32",
      "field_name": "Corner"
    }
  }
]
```

Please see this [guide](./data/loaddata-guide.ipynb) for how to create fixture files from a CSV. **Import only the columns your classes need.**

#### &#127805; Default-farm track: support agronomy-farm data interactions

The guide is written for the ACRE data, so you can follow it step by step. The data is messy on purpose: expect to clean some columns before they fit your classes.

#### &#128640; Choose-your-own track: support user-data interactions

The guide's first cell says what to change for your own data: your CSV file name, your `"model"` values (`yourapp.yourclass`), and your column names.

#### Both tracks

Open your terminal and load each fixture file. With the guide's two files, that is:

```bash
python manage.py loaddata operator-data.json operation-data.json
```

Once you have run this command, open your Django app's admin dashboard. Your data should now appear in your database!

You might have multiple fixture files or have multiple versions of them. In some cases, you will build a couple of classes then add more later. You can always reset your database by deleting `db.sqlite3` and the numbered migration files in your app's `migrations` folder (keep its `__init__.py`). You can create a new database by running `makemigrations` and `migrate` again. As long as you create fixture files correctly, the import data process should cost only a few commands.

**Don't commit your database.** `db.sqlite3` holds your admin login, and your migrations plus fixtures can rebuild it. Add a `.gitignore` file to your `lab4` folder containing the line `db.sqlite3`.

### STEP 8: Create a View for Data Exploration

Create a view and its template that lets a user view the list of the main objects in your database (e.g., the fields in the ACRE database) in your **'index.html'** page.

> IMAGE UPLOAD: Take a screenshot of your index page showing several data entries. Save it with the filename **'sample-view'** inside your **'lab4/images'** folder.

## How to Submit your Lab - GitHub + Brightspace

- Push to your private `YOURNAME-ASM532-Labs` repo, in the `lab4` folder:
   - your README, with the Problem Statement, Specification, Data Model, and Data Dictionary, and a line disclosing any AI use
   - your `prompts.md` and `debug-log.md` (from the [AI debugging starter kit](ai-debugging-kit/README.md))
   - the images listed in each step
   - your Django project, with its fixtures, and a `.gitignore` that leaves out `db.sqlite3`
- **4+ commits**, each with a message saying what changed and why.
- Then submit the repo link on Brightspace. Check Brightspace for the deadline.

Your final lab submission should contain the following files (if your images are another file type that's OK!). The tree uses the &#127805; Default-farm track's names; on the &#128640; Choose-your-own track, use your own project and app names.

```
lab4/
  .gitignore                  <-- contains: db.sqlite3
  README.md                   <-- you should have all the pieces described in lab here
  prompts.md                  <-- your prompt log
  debug-log.md                <-- your debugging log
  images/                     <-- images you've uploaded
    worksheet.jpg
    site-map.png
    data-model.png
    hello-world.png
    sample-data.png
    sample-view.png
  acre/                       <-- your Django project
    manage.py
    acre/
    acrelog/                  <-- your Django APP
        fixtures/             <-- you created everything in here
          operator-data.json  <-- your fixture files: names depend on your classes
          operation-data.json
        migrations/
        templates/            <-- you created everything in here
          acrelog/
            index.html
        __init__.py
        admin.py
        apps.py
        models.py             <-- contains your models
        tests.py
        urls.py               <-- contains your URL routes
        views.py              <-- contains your views
```

### Academic Integrity Reminder

<!-- Submission Policy snippet — see documentation/SNIPPETS.md, edit there first -->

**I will trust that you are doing the right thing, unless I see evidence to the contrary.**

**Your private ASM532 assignment repositories will contain one folder per lab.** Make sure you keep this repo private for the duration of the course. This will also prevent others from copying your code, while still letting you share your code's history with us.

**For each lab, you should have 4+ "commits" to your repo.** For example, you'll push your code at the beginning and end of each lab — but since it's good practice to commit between major changes, I hope you'll end up with more than 4 commits! Don't commit your entire lab 5 minutes before the deadline — we'll check your commit history to assess your version control skills.

**Each commit should have a meaningful commit message that explains how/why you changed your code.** For example, if you'd just written the code to render a graph of your processed data, your commit message could read something like: "used matplotlib to plot corn commodity prices over time for 5 states. yay!"

## License

This work by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

<!-- Rubrics live in the module README, not here. Further reading goes on a closing "Learn More"
     slide in the lecture deck, not in any README. -->
