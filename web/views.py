from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import  Home, About, Contact
from publications.models import Publication, Text, Sources
from contact.models import SocialMedia, Message
from django.shortcuts import render, get_object_or_404
from contact.forms import MessageForm

# Rendering of the index.html page
def index(request):
    # models needed for rendering
    home_obj = Home.objects.get(active=True)
    social_media_obj = SocialMedia.objects.filter(active=True)
    publication_list = Publication.objects.all()

    # pagination
    paginator = Paginator(publication_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # check the image field
    url_img = home_obj.home_image.url if home_obj.home_image and hasattr(home_obj.home_image, 'url') else None

    return render(
        request,
        'index.html',
        {
            'page_obj': page_obj,
            'home': home_obj,
            'image': url_img,
            'media': social_media_obj
        }
    )

# Rendering of the About.html page
def about(request):
    # models needed for rendering
    about_obj = About.objects.get(active=True)
    social_media_obj = SocialMedia.objects.filter()

    # check the image field
    url = about_obj.about_image.url if about_obj.about_image and hasattr(about_obj.about_image, 'url') else None

    return render(
        request, 
        'about.html', 
        {
            'about': about_obj, 
            'image': url, 
            'media': social_media_obj
        }
    )

# Rendering of the contact.html page and include form for messages
def contact(request):
    # models needed for rendering
    social_media_obj = SocialMedia.objects.filter()
    contact_obj = Contact.objects.get(active=True)

    # check the image field
    url = contact_obj.contact_image.url if contact_obj.contact_image and hasattr(contact_obj.contact_image, 'url') else None

    # form message
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = Message(
                name=form.cleaned_data['name'],
                email_adress=form.cleaned_data['email_adress'],
                phone_number=form.cleaned_data['phone_number'],
                message_text = form.cleaned_data['message_text']
            )
            new_message.save()
            return redirect(index)  # redirects to home page on success
    else:
        form = MessageForm()

    return render(
        request, 
        'contact.html', 
        {
            'form': form, 
            'contact': contact_obj, 
            'image': url, 
            'media': social_media_obj
            }
    )

# Rendering of the post.html page
def post(request, id):
    social_media_obj = SocialMedia.objects.filter(active=True)
    publication = get_object_or_404(Publication, id=id)
    sources = Sources.objects.filter(publication = publication).order_by('order')
    text_publicantion = Text.objects.filter(publication = publication).order_by('order')

    return render(
        request, 
        'post.html', 
        {
            'publication': publication, 
            'texts': text_publicantion, 
            'media': social_media_obj,
            'sources': sources
        }
    )