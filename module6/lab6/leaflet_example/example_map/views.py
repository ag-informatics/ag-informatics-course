import geojson
import shapely.geometry as geo
from django.shortcuts import render

# Create your views here.

def render_map(request):
    point = geo.Point(([-86.99269856365936, 40.470060621973026]))
    marker = geojson.Feature(geometry=point, properties={"message": "Hello World"})
    data = geojson.FeatureCollection(marker)
    return render(request, "index.html", {"data": data})