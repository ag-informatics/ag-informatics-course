# Demo: One Page, Five Layouts

ASM 532 · Module 1 · Lecture 1.3

This is the demo from class. Poke around at your own pace. Nothing here is graded.

There are four types of examples:
1. See a basic HTML page skeleton
2. Learn formatting: Single Recipe page
3. Learn layouts: The crazy pink website example
4. Learn more complex CSS layouts: Recipe Book

To view each example:
1. Navigate to the folder.
2. Open, e.g.,`recipe-book/index.html`, in a browser (double-clicking usually works).
3. Open the same folder in VS Code so you can edit alongside it.

## Basic HTML page skeleton

Source file: [0-start.html](0-start.html)
Look at this in the editor - the browser edition will not show you the structure.

## Learn formatting: Single Recipe page

Source folder: [1-mdn-example-formatting](1-mdn-example-formatting)

This example comes from: <a href="https://github.com/mdn/learning-area/blob/main/html/introduction-to-html/html-text-formatting/text-start.html">The MDN Learning Area repository, Intro to HTML, HTML-Text-Formatting</a>

## Learn layouts: The crazy pink website example
Source folder: [2-mdn-example-structure](2-mdn-example-structure)

This example comes from: <a href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Structuring_documents">The MDN Structuring documents tutorial</a>

## Learn more complex CSS layouts: Recipe Book
Source folder: [3-recipe-book](3-recipe-book)

The demo includes a recipe page, and five stylesheets. **The HTML file never changes.** Swapping the stylesheets is what changes the visuals. 

The main point: *structure* and *style* are separate things, and you can change your mind about the layout without touching the content.


Near the top of `index.html`, in the `<head>`, there's one line marked
`STEP:`

```html
<link rel="stylesheet" href="style.css">
```

Change the filename, save, and refresh the browser. That's it!

Start with `style.css` to see the page with no layout applied, then work
your way up. (The file may already be pointing at one of the steps — just
set it back to `style.css` to start from the beginning.)

### The five versions

| Set the link to | What it does | What to look for |
| --- | --- | --- |
| `style.css` | Nothing. This is the starting point. | Everything is in one column, top to bottom, in the same order as the HTML. This is called **normal flow** — it's what the browser does for free. Everything below is us overriding it. |
| `step-1-box.css` | The **box model** | Borders are drawn around every region so you can see that each one really is a box. Look at how `padding` pushes the border away from the text, and `margin` pushes the boxes away from each other. |
| `step-2-table.css` | The **ingredients table** | Cells get borders that merge instead of doubling up, room to breathe, and alternating row colours so your eye doesn't slip onto the wrong row. |
| `step-3-flex.css` | **Flexbox** | Two things move: the nav links go from a stacked list into a row, and the recipe and sidebar end up beside each other instead of one below the other. |
| `step-4-grid.css` | **Grid** | The whole page gets arranged at once. Open the file and look at `grid-template-areas` — the CSS is literally a picture of the layout. |

Each stylesheet is self-contained, so you can jump straight to any one of
them without running the others first.

Some supplementatry resources to help you understand the underlying code:
- [MDN: CSS box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
- [MDN: Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
- [MDN: Grid](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids)
- [MDN: Styling tables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Tables)

### Two things worth knowing

**Use DevTools to see the box model.** In step 1, right-click the recipe and
choose **Inspect**. In the panel that opens, find the box-model diagram — it
shows content, padding, border, and margin as coloured bands with real
numbers. Hover over each band and the browser highlights that exact region on
the page. This is the same inspector from Lecture 1.2, and it's the fastest
way to answer "why is there a gap there?"

**`display: flex` goes on the *container*, not on the thing you want to
move.** This is the single most common mistake when people first use
flexbox. If you want `main` and `aside` side by side, the `display: flex`
goes on the `<div>` that *holds* them — not on `main` or `aside` themselves.
Same with grid.

### A playground: CSS Zen Garden

This demo does a small version of something a website called
[CSS Zen Garden](https://csszengarden.com/) has been doing since 2003. It's
**one HTML file** that anyone can restyle by submitting a stylesheet — and
there are hundreds of submissions, each one wildly different from the last.

Go click through a few designs. The page content never changes; only the CSS
does. It's the same point this demo makes, at a scale that's genuinely fun to
look at.

If you want to see how any of them work, the site links each design's
stylesheet directly — and you now know how to read one.

### Try these

Break it on purpose. You can always undo.

- In `step-1-box.css`, change the `padding` and `margin` numbers on `.recipe`
  and watch the box respond. Then delete `box-sizing: border-box` and see
  what happens to the width.
- In `step-3-flex.css`, change `main` from `flex: 3` to `flex: 1`. What
  happens to the proportions? Now try `flex-direction: column` on `.content`.
- In `step-4-grid.css`, move the sidebar to the left: change the
  `"main aside"` row to `"aside main"`, and the columns from `3fr 1fr` to
  `1fr 3fr`. Two edits, no HTML change. There's a comment in the file marking
  the spot.
- Add a new ingredient row to the table in `index.html`. Notice you don't
  have to touch any CSS for it to be styled correctly.