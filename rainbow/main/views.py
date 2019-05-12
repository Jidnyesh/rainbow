from django.shortcuts import render
# from django.core.mail import send_mail
from django.template.loader import get_template
from .models import Project,Event
import sendgrid
from sendgrid.helpers.mail import *
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
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

def mail(request):
    SENDGRID_API_KEY="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"

    message = Mail(
        from_email='tatti@example.com',
        to_emails='jidnyeshaj@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

            
    return render(request,"test.html",{'a':a,'a1':a1,'a2':a2})