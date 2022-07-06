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


def team(request):
    template_name = 'master/employess.html'
    context = {
        "section" : "team"
    }
    return render(request, template_name, context)


from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail

def subscribe(request):
    subject = "sadasd"
    from_email = settings.DEFAULT_FROM_EMAIL 
    message = 'This is my test message'
    recipient_list = ['rahulriaan70@gmail.com'] 
    html_message = '<h1>This is my HTML test</h1>'
    try:

        # email_msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER], reply_to=[email])
        # send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message)
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
    
