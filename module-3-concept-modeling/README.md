# Module 3: Concept Modeling

## About This Module

In this module, we'll use "conceptual modeling" as the overarching approach to creating data models that represent real world systems across agricultural domains. We will move through three levels of abstraction: from concepts, to objects, then data. 

**1. Domain fluency: conceptual models in agricultural landscapes**
Abstract real world systems by examining: work practices, activities, tasks, and the scope of possibilities.

* How can you map agricultural tasks to scope data models and tool functionality?
* How do people examine a system and identify which domain-appropriate concepts to model?
* What makes a concept, object, or data model "domain-specific"?
* What are some examples of models in agriculture and related domains?
* Goal: Be able to create a domain-driven concept model that represents the flow of data, while scaffolding user tasks.

**2. Technical fluency: design and implement data models**
Learn the process of abstraction and decomposition, including how to: model objects, attributes and operations; create relationships among them; and finally translate models to Python and SQL code.

* What are objects, attributes, operations, and relationships?
* What are object-oriented models, relational models, and other types of data models?
* How do people implement data models in databases?
* Goal: decompose a domain into concepts, design a data model, and implement it using clean code.

## Course Materials

Lecture materials including handouts, demos, and quizzes.

- [Lecture 3.1](lecture-3.1.html)
<!-- - [Lecture 3.2]() - Graded in-class activity ([handout]())
- [Lecture 3.3 demo]() and [Quiz 3]()
- [Lecture 3.4]() -->

### Lab 3

Instructions for the lab, including submission instructions, are in the [lab 3 subfolder](lab-3-data-model/README.md).

Each lab has a specific AI use policy, specified in the lab itself.
As a reminder, the overarching AI policy is available in the main repository [README](../README.md).

If you are a Purdue ASM 532 student: Check Brightspace for current instructions, due dates, and other submission details.

## Rubrics

Total: 30 (5 in-class activity + 5 quiz + 20 lab).

### In-class activity — 5 pts

Activity during Lecture 3.2: conceptual to data modeling.

| Points | Criteria |
| --- | --- |
| 0 | Missed |
| 2 | Incomplete — doesn't have to be "right" |
| 5 | Complete - doesn't have to be "right"! |

### Quiz — 5pts

Box-and-arrow diagram, entity-relationship diagram, and code with cheatsheet on-hand.

### Lab 3 — 20 pts

Create and implement a data model for a specific task-domain. BYO problem + data, or ask us to help you find one.

* Git Commits — 4 pts
    * 1 pt for each of 4 commits.
* Object model — 5 pts (STEP 4)
    * Hand-drawn box-and-arrow model, up to 4 objects, with attributes, operations and labelled relationships. Picks up from what was done in lecture.
* Data model diagram — 5 pts (STEP 5)
    * Formalised in Crow's Foot notation, with primary keys, a foreign key on the "many" side, and any lookup lists specified. Revised from STEP 4, with the changes noted.
* Implementation and queries — 6 pts (STEPs 7-9)
    * Two of your own objects built as tables with a working foreign key, completed model classes, and two queries — one on a single object, one following the relationship.

## References

See `CREDITS.md` for image sourcing/attribution and non-image reference citations used in this module's slides and lab.

## License
This work by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

<!-- ## Revision History -->
