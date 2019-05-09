from django.shortcuts import render
from .models import Project,Event
# Create your views here.


def index(request):
    projects = Project.objects.all().order_by('-created_at')
    context = {'projects':projects}
    return render(request,"index.html",context)

def events(request):
    events = Event.objects.all().order_by('-created_at')
    context = {'events':events}
    return render(request,"events.html",context)

def about(request):
    return render(request,"about.html",context)

def contact(request):
    return render(request,"contact.html",context)