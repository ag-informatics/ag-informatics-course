# Debugging log

One entry per bug, newest at the bottom. Fill it in **while** you debug, not after: the "Tried" list is the part you'll want later. Think of this as a different type of "lab notebook" - recording what you'eve tried, what's worked, and what hasn't.

Copy this template for each entry:

```
## YYYY-MM-DD: short title
- **Error:** the last line of the error message (paste it exactly), and the file and line it points to
- **Tried:** what you tried, in order, and what happened each time
- **Found:** what was actually wrong
- **Fixed:** the change that fixed it
- **Next:** anything still broken, or what you'd check first next time
```

---

## Sample entry

*A made-up example, to show the shape. The error is real: it is what Django 5.2 prints for this mistake. It pairs with the sample in `prompts.md`.*

## 2026-10-15: index page shows a server error
- **Error:** `django.template.exceptions.TemplateDoesNotExist: farmnotes/index.html`, raised from `farmnotes/views.py`, line 10: `return render(request, 'farmnotes/index.html', context)`
- **Tried:**
  1. Restarted the server: same error.
  2. Checked the spelling of `index.html`: correct.
  3. Asked Copilot Chat (see `prompts.md`, 2026-10-15).
- **Found:** my template was at `farmnotes/templates/index.html`, but `'farmnotes/index.html'` tells Django to look in `farmnotes/templates/farmnotes/`.
- **Fixed:** moved the template to `farmnotes/templates/farmnotes/index.html`.
- **Next:** put my other templates in the same folder from the start.
