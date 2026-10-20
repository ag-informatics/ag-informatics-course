# Module 5, Lab 5: User Interface Prototype

## Orientation

You will design and implement an interactive **user interface** as views and templates in a Django web application, using the Bootstrap toolkit for a more consistent design.

You will build on your Lab 4 web application (or reset using my sample code), with the same two-part workflow we have practiced to date: plan on paper, then build.
* **Part 1 - Ideate:** map how someone uses your app (the full flow), circle one use case in it, then paper-prototype 4 web-pages.
* **Part 2 - Design:** create a light design system for a consistent user interface, and turn one of your views into a digital mockup.
* **Part 3 - Build:** implement your 4 web pages in Django, using Bootstrap components, styled to your design system. 

> In this lab, you will design and implement user interface upgrades to an existing web application to support dynamic user interactions.

### Component-based design

In Module 1 (Lecture 1.2) you broke a web page down with **atomic design**. Component-based design builds on the same idea: design and build each fundamental component for reuse everywhere. In this lab, we'll take this component-based or atomic design approach as follows:
* **Atoms:** single elements, e.g., a button, a text input, a badge.
* **Molecules:** atoms combined, e.g., a search box (an input + a button), a card.
* **Organisms:** sections of a page, e.g., a navbar, a form, a table.
* **Templates:** your parent template, `base.html`, laid out on Bootstrap's grid.
* **Pages:** your 4 views, filled with your app's data.

![Atomic design's five levels, using an Instagram post as the example: atoms (icons), molecules (a photo header bar), organisms (a full post header), templates (the post layout with a placeholder image), and pages (the same layout with a real photo of a bulldog and a real caption).](img/atomic-design-recap.png)

*Brad Frost, [Atomic Design, Chapter 2](https://atomicdesign.bradfrost.com/chapter-2/).*


### Some terms for this module
Design teams organize user interface decisions into a design system:

| Concept | What it contains | In this lab | Where is it implemented? |
| --- | --- | --- | --- |
| **Design system** | Everything together: principles, guidelines, components, tokens, documentation | Your *light* design system: your style guide (STEP 3) plus the Bootstrap patterns and components you build with | Whole web-app|
| **Style guide** | Visual rules: colors, typography, spacing, iconography, brand voice | STEP 3: your colors, fonts and assets | In CSS |
| **Pattern library** | Reusable UX patterns: layouts, page templates, interaction patterns | Bootstrap's [grid](https://getbootstrap.com/docs/5.3/layout/grid/) and [examples](https://getbootstrap.com/docs/5.3/examples/), and your parent template, `base.html` (STEP 5) | In Django's HTML templates, Bootstrap layouts|
| **Component library** | Coded UI components: buttons, inputs, modals, cards | [Bootstrap's components](https://getbootstrap.com/docs/5.3/components/accordion/): the pieces in your paper prototype kit and the view menu | In Bootstrap components |

Adapted from [Design Systems vs Pattern Libraries vs Style Guides](https://www.uxpin.com/studio/blog/design-systems-vs-pattern-libraries-vs-style-guides-whats-difference/), UXPin.

We'll use Django's template language, with Bootstrap, a front-end toolkit, to implement a consistent design.

### Bootstrap as a component and pattern library

[Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) is an open-source toolkit of CSS and JavaScript: a pattern library (layouts) and a component library in one. These are the parts you'll use:

| Bootstrap part | What it gives you | Used in |
| --- | --- | --- |
| [Get started](https://getbootstrap.com/docs/5.3/getting-started/introduction/) | The two CDN links (CSS and JavaScript) that add Bootstrap to a page | STEP 5 |
| [Containers](https://getbootstrap.com/docs/5.3/layout/containers/) and [grid](https://getbootstrap.com/docs/5.3/layout/grid/) | Page layout: rows of 12 columns, the same grid as your paper kit | STEPs 2, 4, 5 |
| [Examples](https://getbootstrap.com/docs/5.3/examples/) | Ready-made page layouts to start from | STEP 4 |
| [Components](https://getbootstrap.com/docs/5.3/components/accordion/) (listed down the left side) | Navbar, cards, list groups, accordion, carousel, nav pills, badges, buttons, modal, alerts | STEPs 2, 4, 6 |
| [Tables](https://getbootstrap.com/docs/5.3/content/tables/) | Styled tables | STEPs 2, 6 |
| [Forms](https://getbootstrap.com/docs/5.3/forms/overview/) | Text inputs, selects, checkboxes, input groups, range sliders | STEPs 2, 6 |
| [CSS variables](https://getbootstrap.com/docs/5.3/customize/css-variables/) | Colors and fonts set in one place (your design system's "tokens") | STEPs 3, 5 |
| [Icons](https://icons.getbootstrap.com/) | A free icon set | STEP 3 |
| [Accessibility](https://getbootstrap.com/docs/5.3/getting-started/accessibility/) | Components are built to be accessible, if used as documented | STEPs 4, 6 |

To see these working together in Django, run the [Bootstrap + Django demo](../demos/README.md) (STEP 0).

### Django templates and their design philosophy

Django's [template system](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/#template-system) has a few design principles. Three matter most for this lab:

* **[Separate logic from presentation](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/#separate-logic-from-presentation).** "A tool that controls presentation and presentation-related logic – and that's it." Query, filter and sort your data in `views.py`. Templates only loop, branch, and lay it out.
* **[Discourage redundancy](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/#discourage-redundancy).** A sitewide header, footer and navbar should live "in a single place." That's template inheritance in action: every page `extends` a parent template.
* **[Safety and security](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/#safety-and-security).** Templates can't run arbitrary Python, and Django escapes what users type when it's shown with `{{ }}`. Don't switch that off (e.g., with `|safe`).

Django + Bootstrap in practice:
* **One parent template, `base.html`**, holds everything shared: Bootstrap's CDN links, your `style.css` (loaded *after* Bootstrap, with `{% load static %}`), the navbar, the footer, and an empty `{% block content %}`.
* **Every view's template `{% extends %}` `base.html`** and fills in only its `{% block content %}`: its own Bootstrap layout and components.
* **Link with [`{% url %}`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#url)**, not typed-out paths, so your navbar doesn't break if a route changes.
* **Optional: a component you reuse** (e.g., the same card on two pages) can live in its own small template, pulled in with [`{% include %}`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#include). That's Django's version of a component.

```
base.html              Bootstrap + style.css, navbar, footer, {% block content %}
└── index.html         {% extends "acrelog/base.html" %}: fills content, loops over the records
    └── _card.html     optional: {% include "acrelog/_card.html" %}, once per record
```

The [Bootstrap + Django demo](../demos/README.md) follows this pattern. For a simple walk-through of template flow, see [Django Templates](https://www.geeksforgeeks.org/python/django-templates/) (GeeksforGeeks).

## AI Use Policy for this Lab

Across these learning modules, we will move through three levels of AI-assisted programming (see [course readme](../../README.md) for details).

This lab involves:

<!-- AI Use Policy menu. Canonical text: documentation/SNIPPETS.md, "AI Use Policy". This lab uses option 2.

     1. No AI-generated code. (Modules 1-3 default.) Do not use AI tools to generate code for
        this lab — hand-crafting code is the point. Discussion/ideation with AI is fine per the
        general Academic Integrity policy; writing your code is not.

     2. AI for debugging/exploration only. (Modules 3-5 default.) Write your pseudocode and
        function outlines by hand first; use AI only to debug, explore alternatives, or ask
        thoughtful questions once you're stuck — not to generate the initial code.

     3. AI-assisted "vibecoding." (Module 6 only.) AI-assisted code generation is expected and
        taught here, from a written specification.
-->

> **AI for debugging/exploration only.** (Modules 3-5 default.) Write your pseudocode and function outlines by hand first; use AI only to debug, explore alternatives, or ask thoughtful questions once you're stuck — not to generate the initial code.

Keep using the [AI debugging starter kit](../../module-4-web-applications/lab-4-web-app/ai-debugging-kit/README.md) from Lab 4 and follow the responsible AI use practices previously described. Copy your `prompts.md` and `debug-log.md` into your `lab5` folder and keep logging.

## BEFORE THE LAB

### STEP 0: Identify and fill your knowledge gaps

#### Choose your track

Stick with the track you chose for Lab 4, or switch to the default-farm track now by starting from my reset skeleton.

##### &#127805; Default-farm track: support agronomy-farm data interactions

Start from the reset skeleton in [`skeleton/`](skeleton/): my "answer" to Lab 4. It's the ACRE app with five classes (`Operator`, `Field`, `Machine`, `Seed`, `Operation`), every operation from the ACRE log as a fixture, an index page listing the fields, and a page for each field's operations. My choices may have been different from yours.

Copy the `skeleton/acre/` folder into your `lab5` folder, then, inside your `.venv`:

```bash
cd acre
python manage.py migrate
python manage.py loaddata acrelog/fixtures/acre-data.json
python manage.py runserver
```

Then go to http://127.0.0.1:8000/acrelog/. The two pages already in the skeleton **don't count** toward your 4 views.

##### &#128640; Choose-your-own track: support user-data interactions

Continue with your own Lab 4 project. Copy it into your `lab5` folder.

#### Your spec kit

Both tracks: copy the [`spec-kit/`](spec-kit/) folder into your `lab5` folder. `SPEC.md` is version 1 of your software specification: the user-interface half. **Fill in section 0 now:** an updated description of your system, from your Lab 4 Problem Statement. Then you fill in the rest as you go (STEPs 1-4); the handouts are paper editions of its parts. In Module 6 the same folder grows into a full specification, which your Project Part 3 builds on.
<!-- Claude-drafted 2026-10-18 from her answer to open item 5 ("seed the spec kit ... the handouts can be seen as handout-edition of spec kit components"). -->

#### Bootstrap + Django setup

You'll be able to start building before Lecture 5.3. Your TA will demo this setup in the first lab session.

- **Run the [Bootstrap + Django demo](../demos/README.md).** It's the Module 4 `farmnotes` app with a parent template, Bootstrap components, a form and a small design system. Its README explains each file.
- Skim the Bootstrap parts table above.
- Django template inheritance: [`{% extends %}`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#extends) and [`{% block %}`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#block).
- Named URLs: [`{% url %}`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#url).
- [Working with forms](https://docs.djangoproject.com/en/5.2/topics/forms/) (covered in Lecture 5.3).

#### Design tool

Select one of the following prototype tools for your design system and wireframe mockup (or let us know if you plan to use something else):

- [Miro for education](https://miro.com/education-whiteboard/) - you can use [the wireframe toolkit](https://miro.com/wireframe/) and other similar templates. **(free, recommended)**
- [Pencil project](https://pencil.evolus.vn/) - free and open source software **(free, recommended)**
- [Creately](https://creately.com/lp/ui-mockup-tool/)

If you want more advanced tools, you can try out [Figma - includes free student education access](https://www.figma.com/education/); [UXpin](https://www.uxpin.com/); and [Balsamiq](https://balsamiq.com/)


## Part 1 - IDEATE (in class)

### STEP 1: Journey map and use case

Map how someone would use your web application, from start to finish: the **full flow**. Think back to your task analysis in Lab 3. Look for the holes and broken spots in the flow: those are the places that need a view.

Then pick your **use case**: circle the columns of **one** task on your map. Write who the user is (a role, not a name) and their goal in the boxes at the top. Your 4 views are the pages this use case moves through, and the rest of Part 1 is for this use case only.

- Handout: [journey map](../handouts/handout-journey-map.html)
- A legible photo of the handout is enough. Redrawing it digitally (Miro, Creately, or `mermaid`) is optional.

> SPEC KIT: Save your journey map, with your use case circled, as **'journey-map'** in **'lab5/spec-kit/img'**, and fill in section 1 of `SPEC.md` (who, goal, steps).

### STEP 2: Design 4 webpages and paper-prototype them

Design 4 webpages that your use case needs from the menu below: **2 basic, 1 form, and 1 advanced.**

Use this handout to create a paper prototype that spans the full use case: [paper prototype kit](../handouts/handout-paper-prototype-kit.html).
- The front has two browser screens with Bootstrap's 12-column grid. The back has cut-outs of Bootstrap components, each sized in grid columns ("4 col") and labelled as an atom, molecule or organism. Place each piece on the columns it covers, and it will fit the screen the same way in code.
- Keep the labels: your paper prototype is the plan for your mockup and your code.

#### Pick ONE form webpage

A page where the user adds a record. See [Working with forms](https://docs.djangoproject.com/en/5.2/topics/forms/) and the `observe` page in the [demo](../demos/README.md). Default-track example: record a new operation.

#### Pick TWO basic webpage from this list
| View | Bootstrap component | Default-track example |
| --- | --- | --- |
| 1. A list of records as cards | [Card](https://getbootstrap.com/docs/5.3/components/card/) in a [grid](https://getbootstrap.com/docs/5.3/layout/grid/) | every machine and its status |
| 2. A list of records as a table | [Table](https://getbootstrap.com/docs/5.3/content/tables/) | the operations log for one season |
| 3. The detail page for one record | [Card](https://getbootstrap.com/docs/5.3/components/card/) + [list group](https://getbootstrap.com/docs/5.3/components/list-group/) | one operation: date, operator, field, machine, seed, notes |
| 4. A filtered list | [Nav pills](https://getbootstrap.com/docs/5.3/components/navs-tabs/) or [badges](https://getbootstrap.com/docs/5.3/components/badge/) as filter links | operations of one type, or by one operator |
| 5. Grouped records that expand | [Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) | each field, opening to show its operations |
| 6. A home page that summarizes | Cards with counts, and buttons into the app | how many fields, operations this year, the latest operation |
| 7. A home page with a slideshow | [Carousel](https://getbootstrap.com/docs/5.3/components/carousel/) | photos of the farm's fields or equipment, each linking into the app (you supply the photos) |

#### Pick ONE advanced webpage from this list
Ordered from least to most effort. If you'd like to implement something outside of this list, discuss with us first so that we can help you scope!

1. An admin dashboard customized for your users (set [`list_display`, `list_filter` and `search_fields`](https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#modeladmin-options) in `admin.py`, as in Module 3).
2. A search box that filters a list (a GET form with an [input group](https://getbootstrap.com/docs/5.3/forms/input-group/)).
3. A list filtered by a slider (a GET form with a [range](https://getbootstrap.com/docs/5.3/forms/range/) input), e.g., the operations above a seeding rate, or within a range of dates.
4. An edit page that updates an existing record, with a [modal](https://getbootstrap.com/docs/5.3/components/modal/) to confirm (it reuses your form view, filled in with an existing record).
5. A chart page that graphs data from your database. Pick one:
    - **Image:** a matplotlib plot saved as an image and shown in a Bootstrap [card](https://getbootstrap.com/docs/5.3/components/card/), as in Module 2.
    - **Interactive:** a [Chart.js](https://www.chartjs.org/docs/latest/getting-started/) chart, with your data passed to it using Django's [`json_script`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#json-script).
6. A map page that shows your records as pins. Pick one:
    - **Image:** a Python geoJSON plot saved as an image and shown in a Bootstrap [card](https://getbootstrap.com/docs/5.3/components/card/).
    - **Interactive:** a [Leaflet](https://leafletjs.com/examples/quick-start/) map, with your data passed to it using [`json_script`](https://docs.djangoproject.com/en/5.2/ref/templates/builtins/#json-script).
    - Your records need coordinates. &#127805; Default-farm track: the reset skeleton's `Field` has no coordinates, so you would add them.

> SPEC KIT: Photograph your paper prototype, one photo per view, as **'paper-prototype-1'** to **'paper-prototype-4'** in **'lab5/spec-kit/img'** (numbered in the order the user moves through them). In `SPEC.md`, fill in section 2 (your 4 views, numbered 1 to 4: which menu option each one is, and which step of your use case it serves) and section 3.

## Part 2 - DESIGN

### STEP 3: A light design system

A design system serves as a blueprint for implementation shared across every page in the web application: colors, fonts, assets. Here we'll specify a minimal, or light design system.

Pick a consistent look and feel before you mock anything up, so every view matches. Design it so everyone can use it: see [Visual design for accessibility](https://digital.gov/guides/accessibility-for-teams/visual-design) (digital.gov).

- **Colors:** Select your background color (white is ok!), an accent color, a normal font color, and a "highlight" color. 
    - Generate a palette: [Coolors](https://coolors.co/) or [Adobe Color](https://color.adobe.com/create/color-wheel).
    - Check that text is readable on its background with the [WebAIM contrast checker](https://webaim.org/resources/contrastchecker/): aim for at least 4.5:1 for normal text.
    - Don't use color as the only signal: pair it with a label or an icon.

- **Fonts:** 1-2 font families, at about 4 sizes (header, subheader, main text, small text).
    - Browse [Google Fonts](https://fonts.google.com/), or keep [Bootstrap's defaults](https://getbootstrap.com/docs/5.3/content/typography/).
    - Keep main text at least 16px, Bootstrap's default.

- **Assets:** pick or create your icons, images, videos, and other digital assets. Remember to credit the author if you're using third-party content.
    - Emojis: Check the [HTML UTF-8 codes](https://www.w3schools.com/charsets/ref_emoji_intro.asp) to use emojis on websites, like I've been doing &#128540;.
    - Icons: [Bootstrap Icons](https://icons.getbootstrap.com/) or the [Noun Project](https://thenounproject.com/). 
    - Photos and media: [Unsplash](https://unsplash.com/) or [Wikimedia Commons](https://commons.wikimedia.org/).
    - Give every image alt text that says what it shows or does ([how to decide](https://www.w3.org/WAI/tutorials/images/decision-tree/)).

### STEP 4: ONE digital mockup

Mock up **one** of your 4 views in your design tool, with your design system applied: choose your most complex view (usually the form or the advanced view). Your other views go straight from your paper prototype to code. The mockup is a quick gut-check on how feasible your paper prototype is.

- **Start from your paper prototype.** Lay the view out on Bootstrap's [grid](https://getbootstrap.com/docs/5.3/layout/grid/), or start from one of the [Bootstrap examples](https://getbootstrap.com/docs/5.3/examples/).
- **Build it from [Bootstrap components](https://getbootstrap.com/docs/5.3/components/accordion/)**, and label which component each part is, so your mockup doubles as your build plan.

> SPEC KIT: Export your design system and your mockup together (they're in the same file) as **'design-mockup'** in **'lab5/spec-kit/img'**. In `SPEC.md`, fill in section 4 (its Palette, Typography and Assets tables) and section 5, and mark which view you mocked up.

## Part 3 - BUILD

### STEP 5: Bootstrapify your app

Create a parent template that every page extends. Include:

1. The title of your app, and a "logo": a relevant icon (e.g., from the [Noun Project](https://thenounproject.com/))
2. A Bootstrap [navbar](https://getbootstrap.com/docs/5.3/components/navbar/) that links to each of your views, using `{% url %}`.
3. A [container](https://getbootstrap.com/docs/5.3/layout/containers/)-based layout. Your pages' content goes in its `{% block content %}`.
4. A footer with YOUR NAME and the date the page was last updated.
5. Your own `style.css`, loaded **after** Bootstrap, that applies your design system.

### STEP 6: Implement your 4 views

Build each view from your paper prototype (and your mockup, for the one you mocked up), using Bootstrap components, styled to your design system. Each view needs a URL route, a view function and a template.

> IMAGE UPLOAD: Take a screenshot of each view, with the filenames **'view-1'** to **'view-4'** (numbered to match your spec kit's Views table).

## How to Submit your Lab - GitHub + Brightspace

- Push to your private `YOURNAME-ASM532-Labs` repo, in the `lab5` folder:
   - your spec kit: `spec-kit/SPEC.md`, with its images in `spec-kit/img/`
   - your README, with a line disclosing any AI use
   - your `prompts.md` and `debug-log.md`
   - the images listed in each step
   - your Django project, with its fixtures, and a `.gitignore` that leaves out `db.sqlite3`
- **4+ commits**, each with a message saying what changed and why.
- Then submit the repo link on Brightspace. Check Brightspace for the deadline.

```
lab5/
  .gitignore                  <-- contains: db.sqlite3
  README.md                   <-- AI disclosure
  prompts.md
  debug-log.md
  spec-kit/                   <-- copied from this lab, then filled in
    SPEC.md
    img/
      journey-map.png
      paper-prototype-1.jpg ... paper-prototype-4.jpg
      design-mockup.png
  images/
    view-1.png ... view-4.png
  acre/                       <-- your Django project (default-farm names shown)
    manage.py
    acre/
    acrelog/
        fixtures/
        migrations/
        static/acrelog/
          style.css           <-- your design system
        templates/acrelog/
          base.html           <-- your parent template
          ...                 <-- one template per view
        forms.py              <-- your form
        urls.py
        views.py
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
