from django.urls import path
from .views import index, about, contact, post

urlpatterns = [
    path('', index, name="index"),
    path('sobre/', about, name="about"),
    path('contato/', contact, name="contact"),
    path('post/<int:id>/', post, name="post"),

]