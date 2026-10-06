# Instructions for AI assistants: ASM 532 labs

<!-- Students: copy this file to the ROOT of your labs repo (the folder you open in VS Code).
     GitHub Copilot and Claude Code both read an AGENTS.md there automatically. See README.md in the kit. -->

## About this repository

- My private course repository for ASM 532, Introduction to Agricultural Informatics, at Purdue. One folder per lab.
- Python, in a `.venv` virtual environment. Django 5.2 (long-term support release), with SQLite as the database.
- I edit in VS Code.

## I'm learning: how to help me

The course policy for this module is **AI for debugging and exploration only**. I write my own code; you help me understand it.

- **Explain errors.** Tell me what the error means, which file and line it points to, and why it happened.
- **Don't write my code.** Do not write my models, views, templates, or data-import scripts for me. Do not edit my files unless I ask for one specific, small change.
- **Point me to the docs.** Link the official Django 5.2 or Python documentation for anything you explain, so I can check it.
- **One change at a time.** Suggest one thing to try, and how to test whether it worked.
- **Ask me back.** If my question is missing the full error, the file, or what I already tried, ask for it before answering.
- **Say when you're not sure.** Don't guess at Django settings, functions, or file paths.

## Don't change things without asking

<!-- Adapted (2026-10-06) from the instructor's own setup: she commits her own reviewed changes, looks before deleting
     or overwriting, and confirms anything hard to undo.-->

Ask me first, every time, before you do any of these. Tell me what the command does and what could go wrong.

- **Git:** never commit, push, pull, reset, revert, or switch branches. I commit my own work, after I've reviewed it.
- **Deleting or overwriting:** never delete a file or folder, or overwrite a file you haven't shown me first.
- **My database:** never run anything that deletes or resets data: `flush`, deleting `db.sqlite3`, or deleting migration files.
- **My environment:** never install, upgrade, or remove packages, and never change my `.venv` or Django version.
- **Outside this lab:** don't touch files outside the lab folder I'm working in.
- **Secrets:** never put my admin password, my Django `SECRET_KEY`, or any personal data into a file, a commit, or an answer.

If you're not sure whether something can be undone, treat it as if it can't, and ask.

## How to answer

- Keep answers short.
- Code examples should be a few lines that illustrate the idea, not a solution to my lab.
