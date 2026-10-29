# Agricultural Informatics Project - The Big Picture

In Project Part 1, you will propose a concept regarding an informatics problem that people encounter in agriculture, food systems, ecology, and related areas of research and practice. 

In Project Part 2, you will ideate and describe 3 possible solutions, whether they are entirely separate alternatives, variations on a theme, or components of a larger solution. You will explore these solutions to consider both technical feasibility and user-centered design implications.

In Project Part 3, you will write a software engineering specification document that puts together your problem statement (building on project part 1), your proposed solution (synthesizing from project part 2). You will articulate your users' requirements, software design and architecture, and your intended implementation strategy. 

By the end of this project, you will have described a proposed solution for a domain-specific problem. You can envision the final deliverable as a project description for a hackathon, as a product idea around which to build a business plan, or as first-draft of a graduate research proposal to discuss with your advisor! 

# Project Part 2: Solution Pitch

**Goal**: Pitch your project, three ideas, and your next steps to address the problem you've identified.

**Required**: A short **pitch deck**, presented in class as a **show and tell**. Think of it as an interim pitch to an investor or a grantmaker: what is the problem, what do your users need, what might you build, and what do you still need to figure out? This assignment focuses on **mapping the solution space**. It is critical to understand the approach that you will use to solve the problem and the possible solutions before you jump into creating that solution.

- **Show and tell:** a 4 minute in-class pitch: what is your current thinking? What do you need to figure out re: next steps? Followed by 1 minute of questions.
- **No writing:** no paper to submit. Put on the slides only what you'd show a funder: short phrases, visuals, and your voice in the room.

## Your show and tell "pitch" deck

**Slide 1: Problem.** Your problem (from Part 1) in one slide.
- What is the problem, and why is it an informatics problem?
- Who is affected?

**Slide 2: Design requirements.**
- Who are your users and what do your users need? Build on the actors and needs from Part 1. What task domain are the users working in?
- What is your high-level design goal? What might constrain or enable you in meeting this goal? 
- What data do you need, or do users need to provide?
- If there are any dependencies on external data, hardware, or other components, describe them as requirements for the design.

**Slide 3: Steps to identify a solution.** How will you pick the "best" idea from the ones that you came up with? This is a **plan** only - you don't have to have run any analysis or collected any data.
- What steps will enable you to identify and select the best solution?
- One way to do this, from Lecture 5.4 and Quiz 5:
  - Pick your **criteria**: what makes a solution "good" for your users? Borrow from Nielsen's heuristics or the technology assessments if they fit.
  - Rate each idea against each criterion: **works**, **partly**, or **breaks**.
  - You may also need to collect data to make the decision on the best approach. If so, say what data, and how.

**1-2 slides per idea, 3 ideas in total.** Come up with **3** different solutions to solve the problem. These can be different solutions entirely, or different variations on a theme (However, trivial iterations on a basic idea will not score well for originality).
- Your 3 ideas can also be **different parts of the same solution**. For example:
  - 3 different solutions to the problem
  - 3 variations on one theme
  - 1 data model and 2 user interfaces for it
  - 2 data models and 1 user interface
- Whatever the mix, each idea should be different enough that choosing between them is a real decision.
- For each idea:
  - A short 1-2 sentence general description.
  - How it would potentially work, including the data: where it comes from, how it's processed, and how it's used or shared.
  - 1-3 issues/threats that could prevent implementation of this approach.
  - A visual: a mockup or sketch of how this idea will work.

**Last slide: Next steps and open questions.**
- Which idea are you leaning toward, and what would it take at a broad level to implement it?
- What do you still need to find out?

**Using your lab work:**
- If you used your project domain in your labs, you may reuse that work here, and say which lab it came from. For example:
  - Lab 3: your task analysis, concept model, or data model
  - Lab 4: your problem statement, site map, or data model
  - Lab 5: your journey map, use case, paper prototypes, design system, or mockup
- If your labs used a different domain, apply the same methods to your project problem.
- Part 2 is a proposal. You don't need to build anything.

Check the rubric to see what you should provide!

**What this assignment is not:** In this assignment, you should not elaborate on the problem itself beyond one slide (that was part 1). You do not need to be too specific on the details or steps you need to carry out to produce any single solution. It is important to acknowledge implementation challenges for the various solution options, but this is not an assignment where you list every single step you need to carry out when you do the final programming. In part 3 (end of semester), you will describe a specific solution that you would like to propose for this problem. You can envision the final deliverable as a prompt for hack-a-thon or as a product idea around which to build a business plan.

**Comments on Originality**: Your proposal cannot just be a rewrite of an article you found online. You cannot just rehash a discussion point that people have been writing about in the exact same way for years. **Example**: There are a million discussions on "smart" irrigation systems and why using IoT sensors in the field is the way to attack the problem and deliver many economic, social and environmental benefits. Picking this as your problem and a simple Arduino-based capacitive moisture sensor as a potential solution will result in a low originality grade as it has already been done. That said, many problems in agriculture and strategies to solve them are actually centuries old. You do not need to come up with an entirely new set of solutions, but the approach should be yours and not immediately identifiable as already widely discussed.

## AI Use Policy
ALL parts of this project involve:

> **No AI-generated content.** Do not use AI tools to draft, rewrite, or summarize your concept: no genAI images, no genAI slide layouts. **Writing is thinking**, and the act of writing out your thoughts from scratch will help you refine your ideas, as well as support our ability to evaluate your concept. **Design signals intention**, and the act of sketching, diagramming, mapping out your thoughts will help you see how your ideas can be realized. Discussion and ideation with AI is fine per the general Academic Integrity policy, as is using it to find and understand literature. But remember: YOU are responsible for the content, you must verify what you learn using ALL digital tools, whether search engines or LLMs. YOU are responsible for your concept, and if you can't verbally explain what you've written, then we will have to discuss how you produced your content.

As a reminder, the overarching AI policy is available in the main repository [README](../README.md).

## Submission

If you are a Purdue ASM 532 student: check Brightspace for current instructions, due dates, and to submit.

## Grading Rubric (40 total points)

| Criteria | Exemplary | Good | Weak | Unacceptable |
| --- | --- | --- | --- | --- |
| Addresses: Design requirements | 5 points Users' goals and needs, and the data they have, are described concretely enough that an idea could be evaluated against them. | 4 points Users and data are identified, with needs described in general terms. | 2 points Users are named, but their needs or data are implicit, not explicitly described. | 0 points No discussion of what users need or what data they have. |
| Ideate: Format | 5 points 3 ideas are provided. General description, operation, issues and threats, and a mockup or sketch are provided. | 4 points 3 ideas are provided but either the description, operation, issues/threats, or sketch is missing, or these sections are incomplete. | 2 points Fewer than 3 ideas are provided, or two of the idea sections are missing information. | 0 points Fewer than 2 ideas are provided, or ideas are described with only a few words. |
| Ideate: Reasonableness of Solutions | 5 points All solutions are reasonable solutions to the problem. They may be off-the-wall, expensive, or impractical, but they do not violate physical laws. | 4 points Solutions are mostly feasible, or at least one is completely infeasible. | 2 points Some solutions are completely infeasible, or most solutions have issues. | 0 points Solutions do not make sense as solutions to the problem. |
| Ideate: Unique, Varied Solutions | 5 points Different mechanisms are used in the solutions. Solutions are unique and thought-provoking. | 4 points At least one idea is only a minor deviation from another. | 2 points Most ideas are just minor iterations of the same basic solution. | 0 points All ideas are iterations of the same basic solution. |
| Addresses: What steps will enable you to identify and select the best solution? | 5 points A clear set of step-by-step procedures are provided that can be expected to identify the best solution to pursue. | 4 points Procedures for identifying the best solution are provided but some details are missing. | 2 point The procedures for identifying the best solution are vague and general. | 0 points There is no description of procedures to determine the best solution. |
| Addresses: Next steps and open questions | 5 points The idea being pursued, what it would take at a broad level to implement it, and the specific open questions are clear. | 4 points Next steps are given, but what it would take or the open questions are vague. | 2 points Next steps are only briefly mentioned. | 0 points No next steps or open questions. |
| Presentation | 5 points Language is clear and concise. Ideas and selection are well-described and understandable to the listener. | 4 points Presenter described the ideas adequately, though may be unclear. | 2 points Presenter was not very clear, listeners were not able to follow the complete narrative, though major points were understandable. | 0 points Presenter was not clear, coherent, and it was not possible to follow the narrative. |
| Originality | 5 points The approach is completely novel and/or the discussion is completely different than prior arguments about the approach (but still correct) | 4 points The approach is either only briefly discussed in media or the discussion of the problem is novel and insightful beyond that discussion. | 2 points The approach has been discussed in the press, but this pitch adds a slightly original component. | 0 points The approach has shown up in many news articles and discussed in the exact same manner. |
