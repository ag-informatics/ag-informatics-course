# Quiz 1: Decomposing a Website

ASM 532 &middot; Module 1 &middot; Lecture 1.3

Translate a layout diagram to HTML + CSS.

This quiz was written on paper, in pairs, with the cheatsheet available. It is
reproduced here so you can revisit it, and so you can check your answer against
the worked solution. We walked through the answers in Lecture 1.4.

## The drawing

![The hand-drawn quiz layout: RECIPES as a large heading, a ruled navigation row reading home, all-recipes, and a boxed random, then the recipe title Sunbutter Jelly Sandwich, a framed drawing of bread and jars, the sentence I LOVE this sandwich with LOVE in red, a four-row ingredients table, a blue Instructions heading, the line Spread jam and sunbutter, Combine, and a ruled strip across the bottom.](img/layout.jpeg)

## The task

Work from the layout drawing. In the `index.html` page, address requirements
R1-R10 (structure and content). In the `style.css` page, address R11-R17
(appearance).

## index.html: structure and content

**R1** A banner containing the site name "RECIPES" in the LARGEST heading font.
The id "banner" will be used in the CSS file (selector practice c).

**R2** The navigation row of links to the site's other pages: home, all-recipes,
random. Use an UNORDERED LIST to contain the links within the `<nav>` tags.
The "random" is boxed in the drawing, so give it the class-name "random-box"
to use in CSS.

**R3** A main content area holding the whole recipe, R4 through R9. `<main>` is
for the content unique to THIS page. One per page.

**R4** The recipe title "Sunbutter Jelly Sandwich". A heading, less prominent
than the banner: which heading should you use next?

**R5** A photograph with "alt" text that describes it. Assume there is another
file in the folder "img" called "sandwich.jpg", so the file path is:
`img/sandwich.jpg`

**R6** The sentence: I LOVE this sandwich. In the drawing, LOVE is red and
bolder than the words around it. Wrap just that one word in a tag carrying the
class "highlight", so R15 can style it.

**R7** A table of ingredients, two columns wide and four rows deep. Note: the
top row's right-hand cell is empty. An empty cell is still a cell, so it gets
written out.

**R8** A heading: "Instructions".

**R9** The sentence: Spread jam & sunbutter. Combine. Note the `&amp;`, as a
bare `&` is reserved in HTML.

**R10** A solid red strip across the very bottom with no text, but at a fixed
height.

## style.css: appearance

### Selector practice

Write the selector that would target each of the following. Just the selector,
no rules needed.

- a. every paragraph on the page
- b. every element with class "highlight"
- c. the element with id "banner"
- d. every link inside the nav
- e. every cell in the table

### Rules

**R11** WHOLE PAGE. Set the font for the whole document, and remove the
browser's default margin so your header can sit flush against the edge.

**R12** THE HEADER. Give it some breathing room INSIDE the box, so "RECIPES" is
not jammed against the edge. Which property is that: padding or margin?

**R13** THE NAV. In the drawing the links run left to right, but `<li>` items
stack vertically by default. Two things to fix: the bullets, and the direction.

**R14** THE BOXED NAV ITEM. "random" is drawn inside its own rectangle. Use the
class you gave it in index.html.

**R15** The word LOVE is red and bolder than the words either side. Both come
from CSS here, so this rule needs two declarations. Target the class you added
in R6.

**R16** The "Instructions" heading is blue.

**R17** THE FOOTER. A solid red strip, tall enough to be visible even though it
holds no text. An empty element collapses to zero height, so it needs one of
min-height or padding to occupy space at all.

## What is in this folder

| File | What it is |
| --- | --- |
| [handout-index.html](handout-index.html) | The HTML skeleton handed out in class, with blanks to fill in. |
| [handout-style.css](handout-style.css) | The CSS skeleton handed out in class. |
| [handout-html-css-cheatsheet.md](handout-html-css-cheatsheet.md) | The reference sheet you could use during the quiz. |
| [img/layout.jpeg](img/layout.jpeg) | The layout drawing you were working from. |
| [quiz-1-solution/](quiz-1-solution/) | The worked solution. |

The solution folder is a complete, working page. Open
[quiz-1-solution/index.html](quiz-1-solution/index.html) in a browser to see it
render, and read it alongside
[quiz-1-solution/style.css](quiz-1-solution/style.css) in your editor. Every
section is labelled with the requirement it satisfies, so it doubles as the
marking key.
