# AI debugging starter kit

<!-- Built 2026-10-06 (Ankita's request): a minimal, tool-agnostic version of her own AI-assisted workflow in the course
     repo (CLAUDE.md -> AGENTS.md, prompts.md -> prompts.md, the changelog's Request/Findings/Response/Next ->
     debug-log.md). Claude-drafted; tool facts checked against the VS Code, GitHub and Claude Code docs on 2026-10-06. -->

> Warning: While I use a more specific version of this setup in my own work, I've never tried giving someone else this version! 
> Consider this an experimental setup - try, but be careful! Let's discuss if you run into issues.

Three small files to help you use AI tools the way this course allows in Modules 3-5: **for debugging and exploring, not for writing your code.** They work with whichever AI tool you choose.

| File | Put it | What it does |
| --- | --- | --- |
| [`AGENTS.md`](AGENTS.md) | the **root** of your labs repo: the folder you open in VS Code | Tells your AI tool who you are, what you're building, and how to help: explain, point to the docs, don't write your code, and don't commit, delete, or reset anything without asking. Your tool reads it automatically. |
| [`prompts.md`](prompts.md) | your `lab4/` folder | A log of what you asked, what came back, and what you did with it. |
| [`debug-log.md`](debug-log.md) | your `lab4/` folder | One entry per bug: the error, what you tried, what you found, what fixed it. |

Each log has a **sample entry** for the same bug, a real Django error, so you can see how the two work together.

## Set up your AI tool in VS Code

### GitHub Copilot in VS Code (free for students)

- **Get it:** verified students get Copilot free through [GitHub Education](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students). Anyone can also use the limited Copilot Free plan.
- **Set it up:** [Set up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/setup/copilot), then [use chat](https://code.visualstudio.com/docs/chat/chat-overview).
- **Your instructions file:** Copilot reads `AGENTS.md` (or `.github/copilot-instructions.md`) at the root of your workspace: [Use custom instructions in VS Code](https://code.visualstudio.com/docs/agent-customization/custom-instructions).

### Claude Code in VS Code

- **Get it:** [Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code). Claude Code needs a Claude subscription.
- **Your instructions file:** Claude Code reads `AGENTS.md` too, as long as you don't also have a `CLAUDE.md`: [How Claude remembers your project](https://code.claude.com/docs/en/memory).

### Any other chat tool (ChatGPT, Gemini, ...)

Paste the contents of `AGENTS.md` as your first message in each new chat.

## How to use the logs

1. **Before you ask:** read the error, search it, and write your question in `prompts.md`. See Lecture 4.2's AI-assisted debugging slides.
2. **While you debug:** keep `debug-log.md` open, and add to the "Tried" list as you go.
3. **When you're done:** check the answer against the docs, and note how you checked it.

## Disclose it

Add a line to your lab README, for example: *"I used Copilot Chat to help debug; see `prompts.md` and `debug-log.md`."* The course AI policy asks you to disclose how you used AI tools, and to keep your prompts and the answers.

## How this kit was made

<!-- AI & Technology Use Disclosure for the kit, modelled on the course README's "AI & Technology Use Disclosure (from
     the Instructor)" written my Ankita. Claude-drafted (2026-10-06) from what actually happened; Ankita edited. -->

Per this course's own AI Use Policy, here's how this kit was made:

* **The workflow is from my (Ankita) Fall 2026 practices.** It's a simplified version of my AI use approach for analagous tasks in course prep: an instructions file that sets the rules (`AGENTS.md` here), a log of the prompts I write before I ask, and a change log of what I asked for, what we found, and what changed.
* **I used Anthropic's Claude Code to draft it**, at my direction: generalizing my files so they work with any AI tool, writing the templates and sample entries, and checking the tool instructions against the current GitHub, VS Code, and Claude Code documentation.
* **The sample bug is real.** The error in `debug-log.md` and `prompts.md` was produced by actually breaking the course's `farmnotes` demo app, so the error text is exactly what Django prints. The sample bug and code is a product of my code, building on education materials and publicly available references, with multiple years of TA contributions (just like the entire course)! The conversation in the sample is made up.
* **I outlined, reviewed, and edited everything** before publishing. 

**In short: The choices are mine! The power is now yours! Use tools responsibly; enjoy the support.**

