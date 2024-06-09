from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'about.html')
def contato(request):
    return render(request, 'contact.html')
def post(request):
    return render(request, 'post.html')