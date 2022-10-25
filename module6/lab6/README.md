# Module 6, Lab 6

## Before the Lab
In this lab, we will be using the python libraries *shapely* and *pyproj*. You will need to install them in your python environment in order to complete this lab.

If you are using Anaconda, you can do this with the Environment page in Anaconda. However, you made need to make sure you are using at least Python 3.8. If not create a new Environment and install your applications and libraries into it.

### Copy the Lab Skeleton File into your Repository

This lab is similar to Lab 2 - We will be using a Jupyter notebook to complete this lab. So, the first step is to copy the notebook into your repository. Just like in lab 2, follow these steps:

Navigate to the "ag-informatics-course" repository folder on your computer. Use the command "git pull" to download all the new changes. You should now have a folder titled "module6", with a "lab6" folder inside it. It will contain this README.md file and a "Lab6-Skeleton.ipynb" file This file contains the instructions for your lab. You will use it like a "worksheet", filling in the blanks wherever it prompts you with "Enter code here".

Let's move this file into your repository for you to use:

1. Copy the "lab6" into your existing github repository titled "YOURNAME-ASM591-Labs".
2. Rename "Lab6-Skeleton.ipynb" to "Lab6-YOURNAME.ipnyb". THIS IS THE FILE YOU WILL BE WORKING IN
3. Replace the README.md file with your own.
4. Git add, commit, and push so that your repository now contains these items.
5. View your new Jupyter Notebook in your github repository to confirm everything is in the right place.

## Open your Jupyter Notebook

1. Run Jupyterlabs or Jupyter Notebook from Anaconda.
2. Open the file Lab6-YOURNAME.ipnyb
3. Follow the directions in the lab.

**NOTE**: Part 1 is just a script to make sure you have correctly setup your libraries to work with geometric data. If it does not run correctly, talk to your lab instructor for troubleshooting. *Hint: The programming in the test script provides a useful example of many of the commands to use in the rest of the lab. Use it as a starting place for your own code as necessary.*

## Submitting your work
Make sure to save your notebook code after completing all the steps. Remember to use the git commands "add", "commit", and finally "push" to add your files, commit the changes with a comment, and push the changes to the Github website. Also remember, you should have a commit history with at least 5 commits to demostrate ongoing effort (don't just commit it all 5 mins before it's due!).

GO TO BRIGHTSPACE, submit the link to your repository. You are done!

## Future Learning Pathways 
The [Shapely documentation](https://shapely.readthedocs.io/en/stable/manual.html) is actually an excellent place to explore geometric operations. You can learn more than you ever thought possible about boundaries, geometric objects and how to work with them. **Really!** It has been well written! It is less code documentation and more of an introduction to the basics of geometry. If you are in Precision Agriculture, or another field in which geometry is important, you really should understand the issues it discusses. For example, a line may "contain" a point, but it doesn't "cross" the point. Also, lines that "touch" do not "overlap" and lines that "overlap" do not "touch." We are not very precise when we discuss these ideas, but programming requires a degree of precision that can be very useful to understand. The documentation makes sure to mention these gotchas between how we think and talk about geometry.

## License
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

<!-- This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa] -->

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

  "Introduction to Agricultural Informatics Course" by [Ankita Raturi, Purdue University](https://github.com/ag-informatics/ag-informatics-course) with edits by [Joseph Dvorak, University of Kentucky](https://www.engr.uky.edu/directory/dvorak-joseph) is licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.](http://creativecommons.org/licenses/by-nc-sa/4.0/).
