# Module 4: Web Applications

## About This Module

In this module, we'll begin to write software specifications to guide the design and implementation of a web application. The emphasis will be on learning how to translate real world user context into data models and functioning code.

**1. Domain fluency: translating agricultural activities into digital workflows**
Translate real world user needs into a minimum viable product (MVP)
* How can you map agricultural activities as digital data-driven workflows?
* How do people translate activities into operations?
* What are some examples across the genres of ag-tech?
* Goal: Design and scope an MVP solution for real user needs (including your own), with focus on working with data. 


**2. Technical fluency: specifying practical software implementations**
Learn how to design 

* How does one scope a feasible software development project?
* How can software specifications guide implementation?
* How are dynamic web applications built - and what else can be made using this approach?
* How do people write clean object-oriented code?
* Goal: Implement a small Django web application, with focus on Python classes / Django models.


## Course Materials

Lecture materials including handouts, demos, and quizzes.

- [Lecture 4.1](lecture-4.1.html) - [Demo: from functions to Django models](demos/README.md) ([read-along handout](handouts/handout-functions-objects-readalong.html))
- [Lecture 4.2](lecture-4.2.html) - same demo: its `myapp` Django project
<!-- Add when they ship (Lecture 4.4 is built; it stays out of the push until reviewed):
- [Lecture 4.3](lecture-4.3.html) - follow-the-object activity (lab period), with its cards and worksheet handouts
- [Lecture 4.4](lecture-4.4.html) - same `myapp` project: views, templates, static files and a fixture
-->

### Lab 4

Instructions for the lab, including submission instructions, are in the [lab 4 subfolder](lab-4-web-app/README.md).

Each lab has a specific AI use policy, specified in the lab itself.
As a reminder, the overarching AI policy is available in the main repository [README](../README.md).

If you are a Purdue ASM 532 student: Check Brightspace for current instructions, due dates, and other submission details.

## Rubrics

Every graded item in this module, with its points. Keep rubrics here, not in the lab or quiz
README — one place to look, and the lab README stays about doing the lab.

<!-- Total, the in-class activity (Lecture 4.3) and the check-in: Ankita to add, with their points, when 4.3 ships.
     The template's sections were removed so the push scan passes. -->

### Lab 4 — 20 pts

Specify, model, and build a Django web application. Default-farm track: the ACRE farm data. Or the Choose-your-own track, scoped with us.

* Git Commits — 4 pts
    * 1 pt for each of 4 commits.
* Specification — 4 pts (STEPs 1-3)
    * Problem statement, worksheet photo, 2-3 use cases, functional and non-functional requirements, and an MVP cut.
* Site map, data model and data dictionary — 4 pts (STEP 4)
    * Pages labelled with their view, template and model(s); a class diagram of at least 4 classes, with primary keys, a foreign key relationship and any lookup lists; a data dictionary.
* Implementation — 8 pts (STEPs 5-8)
    * A working project and app, models with admin test data, data imported with a fixture file (and `db.sqlite3` left out of the repo), and an index page listing the main objects.

## References

See `CREDITS.md` for image sourcing/attribution and non-image reference citations used in this module's slides and lab.

## License
This work by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

<!-- ## Revision History -->
