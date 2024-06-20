from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="about"),
    path('contato/', views.contato, name="contact"),
    #path('login/', views.login, name="login"),
    path('post/<int:id>/', views.post, name="post"),
    #path('password-reset/', views.reset, name="password_reset"),
]