from django.shortcuts import render
from .models import Publication, Image, Text

def index(request):
    publi = Publication.objects.get(id=1)
    return render(request, 'index.html', {'publi': publi})
def sobre(request):
    return render(request, 'about.html')
def contato(request):
    return render(request, 'contact.html')
def post(request):
    return render(request, 'post.html')