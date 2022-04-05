from django.shortcuts import render
from .models import Destination


def index(request):
    dest = Destination.objects.all()
    return render(request, "index.html", {"destination": dest})