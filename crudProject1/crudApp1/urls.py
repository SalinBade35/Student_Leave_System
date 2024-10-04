# yo app lai chahiney jati sabai urls yetai rakhne

from django.urls import path
# from .views import home, form, contact, about
from .views import * # * means all 



urlpatterns = [
    path("", home, name="home"),
    path("form/", form, name="form"),
    path("contact/", contact, name="contact"),
    path("about/", about, name="about"),
    
]

