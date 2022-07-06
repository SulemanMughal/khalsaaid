from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.


def index(request):
    template_name = 'master/index.html'
    context = {
        "section" : "home"
    }
    return render(request, template_name, context)

def donations(request):
    template_name = 'master/donate.html'
    context = {
        "section" : "donation"
    }
    return render(request, template_name, context)

def aboutUs(request):
    template_name = 'master/about-us.html'
    context = {
    }
    return render(request, template_name, context)


def recent_news(request):
    template_name = 'master/news.html'
    context = {
        "section" : "news"
    }
    return render(request, template_name, context)


def events(request):
    template_name = 'master/events.html'
    context = {
        "section" : "events"
    }
    return render(request, template_name, context)


def blogs(request):
    template_name = 'master/blogs.html'
    context = {
        "section" : "blogs"

    }
    return render(request, template_name, context)

def projects(request):
    template_name = 'master/projects.html'
    context = {
        "section" : "projects"
    }
    return render(request, template_name, context)


def employees(request):
    template_name = 'master/employess.html'
    context = {
    }
    return render(request, template_name, context)


from django.conf import settings
from django.core.mail import EmailMessage


def subscribe(request):
    subject, body, email = "sadasd", "test", "rahulriaan70@gmail.com"
    try:
        # email_msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], reply_to=[email])
        # email_msg.send()
        print("mail has been send")
        return redirect(reverse("index"))
    except Exception as e:
        print("**"*70 , e , "*" *70)
        return redirect(reverse("index"))
    

def subscribePage(request):
    template_name = 'master/subscribe.html'
    context = {
    }
    return render(request, template_name, context)


# def send_email():
    
