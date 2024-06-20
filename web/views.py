from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Publication, Text, Home, About, Contact, Social_Media, Message
from django.shortcuts import render, get_object_or_404
from .forms import MessageForm

def index(request):

    home_obj = Home.objects.get(active=True)
    publication_list = Publication.objects.all()
    paginator = Paginator(publication_list, 10)
    social_media_obj = Social_Media.objects.filter()

    page_number = request.GET.get('page')
    print(home_obj.home_image.url)
    page_obj = paginator.get_page(page_number)
    #publi = Publication.objects.get(id=1)
    return render(request, 'index.html', {'page_obj': page_obj, 'home': home_obj, 'image': home_obj.home_image.url, 'media': social_media_obj})


def sobre(request):
    about_obj = About.objects.get(active=True)
    print(about_obj.about_image.url)
    social_media_obj = Social_Media.objects.filter()

    return render(request, 'about.html', {'about': about_obj, 'image': about_obj.about_image.url, 'media': social_media_obj})


def contato(request):
    social_media_obj = Social_Media.objects.filter()
    contact_obj = Contact.objects.get(active=True)
    if request.method == 'POST':
        print('contato entrou POST')
        form = MessageForm(request.POST)
        if form.is_valid():
            print('formulário válido')
            new_message = Message(
                name=form.cleaned_data['name'],
                email_adress=form.cleaned_data['email_adress'],
                phone_number=form.cleaned_data['phone_number'],
                message_text = form.cleaned_data['message_text']
            )
            new_message.save()
            return redirect(index)  # Redirect to a success page
    else:
        print('contato NÃO entrou POST')
        form = MessageForm()
        print('contato NÃO entrou POST 2')

    #return render(request, 'contact.html', {'form': form})

    return render(request, 'contact.html', {'form': form, 'contact': contact_obj, 'image': contact_obj.about_image.url, 'media': social_media_obj})


def post(request, id):
    social_media_obj = Social_Media.objects.filter()
    publication = get_object_or_404(Publication, id=id)
    text_publicantion = Text.objects.filter(publication = publication).order_by('order')
    return render(request, 'post.html', {'publication': publication, 'texts': text_publicantion, 'media': social_media_obj})


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = MessageForm()

    return render(request, 'contact.html', {'form': form})