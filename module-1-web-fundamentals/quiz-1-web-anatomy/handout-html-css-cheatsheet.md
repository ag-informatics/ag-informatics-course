# HTML Reference Cheatsheet

ASM 532 · Module 1
---

## Anatomy of an element

```
<p class="editor-note">My cat is very grumpy</p>
 └┬┘ └──────┬───────┘ └──────────┬─────────┘└┬─┘
opening   attribute            content    closing
  tag                                        tag
```

An element is opening tag + content + closing tag. Elements nest inside each other.
A few elements have no content and no closing tag: `<img>`, `<br>`, `<link>`, `<meta>`.

---

## HTML: page skeleton

| Tag | What it's for |
| --- | --- |
| `<!DOCTYPE html>` | First line of every page. Says "this is HTML." |
| `<html lang="en">` | Wraps the whole document. |
| `<head>` | Information *about* the page. Not shown on it. |
| `<title>` | Text in the browser tab. Goes in `<head>`. |
| `<link rel="stylesheet" href="style.css">` | Attaches a CSS file. Goes in `<head>`. |
| `<body>` | Everything the reader actually sees. |

## HTML: page regions

| Tag | What it's for |
| --- | --- |
| `<header>` | Banner at the top — site title, logo. |
| `<nav>` | The set of links to other pages. |
| `<main>` | Content unique to *this* page. Only one per page. |
| `<aside>` | Related, but not the main point — a sidebar. |
| `<footer>` | Bottom strip — copyright, contact. |
| `<section>` / `<div>` | Generic grouping when nothing above fits. |

## HTML: content

| Tag | What it's for |
| --- | --- |
| `<h1>` … `<h6>` | Headings. `<h1>` is the most important; don't skip levels. |
| `<p>` | A paragraph. |
| `<ul>` / `<ol>` | Unordered (bulleted) / ordered (numbered) list. |
| `<li>` | One item. Goes inside `<ul>` or `<ol>`. |
| `<a href="page.html">text</a>` | A link. `href` is where it goes. |
| `<img src="cat.png" alt="a description">` | An image. `alt` is required. |
| `<strong>` / `<em>` | Important / emphasised text. |
| `<span>` | Wraps a few words so you can style just them. Adds no meaning of its own. |

## HTML: tables

For **data** with rows and columns — not for arranging a page.

| Tag | What it's for |
| --- | --- |
| `<table>` | Wraps the whole table. |
| `<tr>` | One row. Everything else goes inside a row. |
| `<th>` | A **heading** cell — the label for a column or a row. |
| `<td>` | A **data** cell. |

Rows run across; cells sit inside rows:

```
<table>
  <tr>
    <th>Ingredient</th>
    <th>Amount</th>
  </tr>
  <tr>
    <td>Bread</td>
    <td>2 slices</td>
  </tr>
</table>
```

An empty cell is still a cell — write `<td></td>` to leave one blank.

## HTML: attributes you'll need

| Attribute | What it does |
| --- | --- |
| `class="name"` | A label you can reuse on many elements. CSS grabs it with `.name` |
| `id="name"` | A label used **once** on the page. CSS grabs it with `#name` |
| `href="..."` | On `<a>`: the destination. On `<link>`: the file being attached. |
| `src="..."` | On `<img>`: which image file to show. |
| `alt="..."` | On `<img>`: what the image shows, for anyone who can't see it. |

---

## CSS: the shape of a rule

```
selector {
  property: value;
}
```

## CSS: selectors

| Selector | Selects |
| --- | --- |
| `p` | every `<p>` element |
| `.note` | every element with `class="note"` |
| `#banner` | the one element with `id="banner"` |
| `nav a` | every `<a>` **inside** a `<nav>` |
| `h1, h2` | every `<h1>` **and** every `<h2>` |

## CSS: the box model

Every element is a box, in this order from the inside out:

```
        ┌─────────── margin ───────────┐   space OUTSIDE the border
        │  ┌───────── border ────────┐ │
        │  │  ┌─── padding ───┐      │ │   space INSIDE the border
        │  │  │   content     │      │ │
        │  │  └───────────────┘      │ │
        │  └─────────────────────────┘ │
        └──────────────────────────────┘
```

| Property | Sets |
| --- | --- |
| `width` / `height` | size of the content area |
| `padding` | space between the content and the border |
| `border` | e.g. `1px solid #333` |
| `margin` | space between this box and its neighbours |

## CSS: common properties

| Property | Example values |
| --- | --- |
| `color` | `red`, `#333`, `rgb(0,0,0)` — the **text** colour |
| `background-color` | same kinds of values — the **box** colour |
| `font-family` | `Arial, sans-serif` |
| `font-size` | `16px`, `1.2em` |
| `font-weight` | `bold`, `normal` — how heavy the text is |
| `text-align` | `left`, `center`, `right` |
| `list-style-type` | `none`, `disc`, `decimal` |
| `display` | `block`, `inline`, `flex`, `grid`, `none` |
| `gap` | `20px` — space between the children of a flex or grid container |

## CSS: sizing

| Property | Sets |
| --- | --- |
| `width` / `height` | A fixed size. |
| `max-width` | A size it must never exceed. `max-width: 100%` on an image is the usual way to stop it overflowing its column on a narrow screen — it shrinks to fit, but never stretches past its natural size. |
| `min-width` / `min-height` | A size it must never go below. Useful for giving an empty box visible height. |

## CSS: styling a table

| Property | Sets |
| --- | --- |
| `border-collapse` | `collapse` merges the border between two neighbouring cells into a single line. Without it each cell draws its own, so you get a doubled line everywhere they touch. Goes on the `<table>`. |
| `border` | On `th` / `td` — e.g. `1px solid #333`. Applied to the cells, not the table, or only the outside gets a line. |
| `padding` | On `th` / `td` — space inside each cell. Cells with none are very hard to read. |
| `text-align` | On `th` / `td` — heading cells are centred and bold by default; `left` overrides that. |

```
table {
  border-collapse: collapse;
}

th, td {
  border: 1px solid #333;
  padding: 8px;
  text-align: left;
}
```

Listing `th, td` together applies the same rules to both.

## CSS: putting boxes side by side

**Flexbox** — put this on the *container*, and its children line up in a row:

```
.container {
  display: flex;
  gap: 20px;          /* space between the children */
}
```

Then control how much room each child takes:

```
main  { flex: 3; }    /* takes 3 shares  */
aside { flex: 1; }    /* takes 1 share   */
```

**Grid** — the other way, when you want named rows and columns:

```
.container {
  display: grid;
  grid-template-columns: 3fr 1fr;
  gap: 20px;
}
```

---

*Comments:* `<!-- like this -->` in HTML, `/* like this */` in CSS.
