from django.urls import path
from .views import IndexTemplateView, AboutTemplateView, ContactTemplateView, PostTemplateView

urlpatterns = [
    path('', IndexTemplateView.as_view(), name="index"),
    path('sobre/', AboutTemplateView.as_view(), name="about"),
    path('contato/', ContactTemplateView.as_view(), name="contact"),
    path('post/<int:id>/', PostTemplateView.as_view(), name="post"),

]