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
You will be submitting a few different things. Create a folder called **'lab6'** and copy over acrelog (including the acre folder) from lab 5.

```
lab6/
  acre/         # Copy over your previous project, you'll be building on it.
  README.md
```
## Embed Leaflet Map in Django
First, we will import Leaflet script to our html page by adding the script below into the head section of your template file (.html). 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
  ...
    <link
      rel="stylesheet"
      type="text/css"
      href="https://unpkg.com/leaflet/dist/leaflet.css"
      crossorigin=""
    />
    <script
      src="https://unpkg.com/leaflet/dist/leaflet.js"
      crossorigin=""
    ></script>
    <link rel="stylesheet" type="text/css" href="{% static 'leaflet-map.css' %}" />
    <script src="{% static 'leaflet-map.js' %}" defer></script>
  ...
  </head>
  <body>
    ...
  </body>
</html>
```

There are 4 scripts that we import here. The fisrt two are Leaflet's stylesheet and JavaScript modules. There two keep all functionalities for runing Leaflet. 

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      type="text/css"
      href="https://unpkg.com/leaflet/dist/leaflet.css"
      crossorigin=""
    />
    <script
      src="https://unpkg.com/leaflet/dist/leaflet.js"
      crossorigin=""
    ></script>
```

Another two scripts are `leaflet-map.css` and `leaflet-map.js` which are our custom style sheet and JavaScript that we will create later. 

```html
<link rel="stylesheet" type="text/css" href="{% static 'leaflet-map.css' %}" />
<script src="{% static 'leaflet-map.js' %}" defer></script>
```

Note that we import with `static` in front of the custom script. In Django, Javascript and stylesheets files will be kept in `static` folder in your application. We also need to tell Django that we will use `static` folder by adding one line at the top of html file as below.

```html
{% load static %}   <-- add this line
<!DOCTYPE html>
<html lang="en">
...
</html>
```

Let's create a static folder in your application folder. Then create `leaflet-map.js` and `leaflet-map.css`. Copy the following code in `leaflet-map.js`

```javascript
const copy =
  "&copy; <a href='https://www.openstreetmap.org/copyright'>OpenStreetMap</a>";
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });

map.fitBounds([
  [40.470060621973026, -86.99269856365936], // Somewhere in ACRE
  // You can add more coordinates
]);
```

We will be using OpenStreetMap layer. So, ther first line is to declear the source of our data. The second line is the URL of the default OpenStreetMap. There are many more options that you can use from [here](https://leaflet-extras.github.io/leaflet-providers/preview/). The third line will load the layer from providing URL. Then the forth line will put that layer into our map.

One last thing for the JavaScript file is to choose the default view. That is when `map.fitBounds()` comes to play. You can pass coordinate or a list of coordinates that the map will show when you reload it.

Next is the stylesheet. Open `leaflet-map.css` and copy the following code. For now, we will display `body` tag with 100% screen height. Then the tag with id=`map` will also be 100% of height and width. You can change this configuration later.
```css
html,
body {
  height: 100%;
  margin: 0;
}
#map {
  height: 100%;
  width: 80vh;
}
```

Now, we are ready to show the map. Choose one of your existing html files (besides the template) or create a new one to place the map in. Add the following line into the body part.

```html
<body>
  ...
  <div id="map"></div> <-- add this line
  ...
</body>
```

Lastly, you will need to config `url.py` and `views.py` to point to the template file we just created. The following snippet assumes you have placed it in the index.html file, so swap out the references to the index with your page if you chose elsewhere.

```python
# views.py
from django.shortcuts import render

def render_map(request):
    return render(request, "index.html")
```

```python
# url.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_map, name="index"),
]
```
## Putting Features on the Map
Leaflet allows us to modify the map freely. One of the common things to put into the map is a marker. Techically speaking, a marker is a point (geometric object) on the map. To add a marker, first add the following line into `leaflet-map.js`.

```javascript
let marker = L.marker([40.470060621973026, -86.99269856365936]).addTo(map);
```

The code above creates a marker object on the coordinate that we provide. Then we add that marker to the map that we created earlier. You should see a marker after you refresh the map. 

Next, let's add a popup box when we click on that marker. We can do that by adding more functionality at the end of the marker object we created previously. Refresh the page and try to click on the marker. 

```javascript
let marker = L.marker([40.470060621973026, -86.99269856365936])
  .addTo(map)
  .bindPopup("This is a popup");
```

We can also create a marker using Python. Open `view.py` then modify `render_map` function as below.

```python
import geojson
import shapely.geometry as geo

def render_map(request):
    point = geo.Point(([-86.99269856365936, 40.470060621973026]))
    marker = geojson.Feature(geometry=point, properties={"message": "Hello World"})
    data = geojson.FeatureCollection(marker)
    return render(request, "index.html", {"data": data})
```

First, we import `geojson` and `shapely.geometry`. We will use `shapely.geometry` to create geometry objects. In this case, we want to create a marker that is a point. Then we create a geoJSON feature object by passing the geometry and properties. The properties parameter accepts a dictionary. Therefore, you can have multiple key-value properties. Next, we wrap the marker into a geoJSON feature collection. A GeoJSON feature collection is a list of geoJSON feature. You can pass a list of geoJSON features. However, in this example, we only pass one marker. Lastly, we return the render page with additional information going back to the HTML side. 

Open `index.html` file and modify as below. We interpolate date from Django by wrapping it with double curly brackets. Then we give HTML a clue that this is a JSON data. Lastly, we name this data "data_geojson" for HTML and JavaScript side. 
```html
<body>
  {{ data|json_script:"data_geojson" }}
  <div id="map"></div>
</body>
```
Next we need to process the geoJSON data in JavaScript file. Open `leaflet-map.js` then add the code below. First, we parse the data from HTML. As the data is in geoJSON format, we can use Leaflet built-in function to display all features in the geoJSON feature collection. We can also bind a popup box with message that we want to show. In this case, it is a `message` property that we embed from Python side (`view.py`). Finally, we add the feature to the map. 

```javascript
const data = JSON.parse(document.getElementById("data_geojson").textContent);

let feature = L.geoJSON(data.features)
  .bindPopup(function (layer) {
    return layer.feature.properties.message;
  })
  .addTo(map);
```

You can add multiple geometry objects into one geoJSON feature collection. The objects could be points, lines, or polygons. The most of the data processing will be done in `view.py`. Whatever data you embed into rendering process will be passed to HTML and JavaScript side for display into the map. 

## Display ACRE map
You will see `acre_geometry.parquet` file in the data folder. Parquet file (.parquet) is a compressed file (like a zip file). Inside, you will see the geometry of fields in ACRE. You can use `geopandas` to read this file by `read_parquet("filename.parquet")`. 

Your task is:
- Create a map of ACRE with field's boundaries. 
- When you click on the field, the map will show a popup with a brief summary of the latest operation on that field and a link to view the full detail of that field. 

## Submitting your work
Make sure to save your notebook code after completing all the steps. Remember to use the git commands "add", "commit", and finally "push" to add your files, commit the changes with a comment, and push the changes to the Github website. Also remember, you should have a commit history with at least 5 commits to demostrate ongoing effort (don't just commit it all 5 mins before it's due!).

GO TO BRIGHTSPACE, submit the link to your repository. You are done!

## Future Learning Pathways 
Check the lecture from previous iterations of this course

- Lecture 6.1: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.1.html
- Lecture 6.2: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.2.html
- Lecture 6.3: www.aginformaticslab.org/ag-informatics-course/module6/lecture6.3.html

You can work on `exercise.ipynp`. This is optional but highly recommended if you want to learn how to work with geospatial data.

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
