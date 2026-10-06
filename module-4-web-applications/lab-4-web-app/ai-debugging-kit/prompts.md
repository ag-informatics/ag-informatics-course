# Prompt log

One entry per question you ask an AI tool, newest at the bottom. Write the question here **before** you ask it: writing it down is often enough to spot the answer. 

I write these like I'm explaining the problem to myself and writing out my thinking about how I might try to solve the problem. 

Copy this template for each entry:

```
## YYYY-MM-DD: short title
- **Tool:** e.g., Copilot Chat in VS Code, Claude Code, ChatGPT
- **Where:** lab, file, and line
- **What I asked** (paste it exactly):
- **What came back** (a short summary):
- **What I did with it, and how I checked it:**
```

---

## Sample entry

*A made-up example, to show the shape. It pairs with the sample in `debug-log.md`.*

## 2026-10-15: Django can't find my index template
- **Tool:** Copilot Chat in VS Code
- **Where:** lab4, `farmnotes/views.py`, line 10
- **What I asked:**
  > I'm getting `django.template.exceptions.TemplateDoesNotExist: farmnotes/index.html` when I open http://127.0.0.1:8000/farmnotes/. My view calls `render(request, 'farmnotes/index.html', context)`, and my template is at `farmnotes/templates/index.html`. Why can't Django find it? Please explain, and point me to the Django docs, rather than rewriting my code.
- **What came back:** Django looks inside each app's `templates/` folder for the path in `render()`. So `'farmnotes/index.html'` means `farmnotes/templates/farmnotes/index.html`: there's a missing `farmnotes/` folder. It linked the Django tutorial's "Template namespacing" note.
- **What I did with it, and how I checked it:** Read the "Template namespacing" note in the [Django 5.2 tutorial, part 3](https://docs.djangoproject.com/en/5.2/intro/tutorial03/#write-views-that-actually-do-something). Moved `index.html` into `templates/farmnotes/`, and reloaded the page: it worked.
