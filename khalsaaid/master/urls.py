from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("donations", views.donations, name="donations"),
    path("about-us", views.aboutUs, name="about_us"),
    path("news", views.recent_news, name="news"),
    path("events", views.events, name="events"),
    path("blogs", views.blogs, name="blogs"),
    path("projects", views.projects, name="projects"),
    path("team", views.team, name="team"),
    path("subscribe-email", views.subscribe, name="subscribe"),
    path("subscribe", views.subscribePage, name="subscribe_page"),
]