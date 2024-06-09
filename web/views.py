from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def sobre(request):
    return render(request, 'about.html')
def contato(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')
def post(request):
    return render(request, 'post.html')
def reset(request):
    return render(request, 'reset_password.html')