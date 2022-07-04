from django.shortcuts import render

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