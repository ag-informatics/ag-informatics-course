from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


from .models import Crop


def index(request):
    crop_list = Crop.objects.all()
    context = {'crop_list': crop_list}
    return render(request, 'cropexplorer/index.html', context)