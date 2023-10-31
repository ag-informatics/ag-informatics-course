# Module 6, Lab 6

## Before the Lab
We need to install new packages for this lab. Install packages could take time. It is highly suggest that you do before the lab. 

```bash
conda activate asm591
conda install pyarrow
conda install -c conda-forge geopandas
```

### Leaflet

In this lab, we will use Leaflet as a map tool. Leaflet is an open-source interactive map library. It is written in JavaScript. Therefore, it can be used in web platform including Django. More information about Leaflet and documents is here: https://leafletjs.com/index.html.

### Lab Submission Folder Structure
You will be submitting a few different things. Create a folder called **'lab5'**. Create a subfolder called **'paper-protoype'** and copy over your previous lab 5.

```
lab6/
  ACRE/         # Copy over your previous project, you'll be building on it.
  README.md
```
## Embed Leaflet map in Django
As Leaflef is a JavaScript library, we will need to create a javascript file for it. In Django, Javascript files (and also stylesheets like .css files) will be kept in `static` folder in your application. Let's create a `map.js` file in `static` folder and copy the following script.

```javascript
const copy =
  "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });
```

Next, we will import Leaflet script to our html page by adding the script below into the head section of your templete file (.html). 

```html
<head>
...
  <link rel="stylesheet" type="text/css" href="https://unpkg.com/leaflet/dist/leaflet.css" crossorigin=""/>
  <script src="https://unpkg.com/leaflet/dist/leaflet.js" crossorigin=""></script>
...
</head>
```

The last step is to include our `map.js` into the template file. First we will need to tell Django to load `static` folder by adding the following line to the first line of your templete file.
```html
{% load static %}   <-- add this line
<!DOCTYPE html>
<html lang="en">
```

Then add the folling script in the body part where you want to display the map.

```html
<body>
  ...
  <div id="map"></div>
  <script src="{% static 'map.js' %}" defer></script>
  ...
</body>
```

## Display ACRE map
You will see `acre_geometry.parquet` file in the data folder. Parquet file (.parquet) is a compress file (like zip file). In side, you will see the geometry of fields in ACRE. You can use `geopandas` to read this file by `read_parquet("filename.parquet")`. 

Your task is 
- Process ACRE geometry into .geojson file 
- create a new page call `map` in your navigation bar. 
- The map page will show a map of ACRE with field's boundaries. 
- When click on the field, the map will show a marker that show brief summary of the latest operation on that field and a link to view the full detail of that view. 

## Submitting your work
Make sure to save your notebook code after completing all the steps. Remember to use the git commands "add", "commit", and finally "push" to add your files, commit the changes with a comment, and push the changes to the Github website. Also remember, you should have a commit history with at least 5 commits to demostrate ongoing effort (don't just commit it all 5 mins before it's due!).

GO TO BRIGHTSPACE, submit the link to your repository. You are done!

## Future Learning Pathways 
Check the lecture from previous iterations of this course

- Lecture 6.1: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.1.html
- Lecture 6.2: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.2.html
- Lecture 6.3: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.3.html

You can work on `exercise.ipynp`. This is optional but recommend. 

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
