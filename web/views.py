"""web page rendering (WEB SITE)"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from contact.forms import MessageForm
from contact.models import SocialMedia, Message
from publications.models import Publication, Text, Sources

from .models import  Home, About, Contact


class IndexTemplateView(TemplateView):
    """Rendering of the index.html page"""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # models needed for rendering
        home_obj = get_object_or_404(Home, active=True)
        publications = Publication.objects.filter()

        # pagination
        paginator = Paginator(publications, 1)
        page_number = self.request.GET.get('page')

        # check the image field
        if home_obj.home_image and hasattr(home_obj.home_image, 'url'):
            url_img = home_obj.home_image.url
        else:
            url_img = None

        context['page_obj'] = paginator.get_page(page_number)
        context['home'] = home_obj
        context['image'] = url_img
        context['media'] = SocialMedia.objects.filter(active=True)

        return context


class AboutTemplateView(TemplateView):
    """Rendering of the About.html page"""

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # models needed for rendering
        about_obj = get_object_or_404(About, active=True)

        # check the image field
        if about_obj.about_image and hasattr(about_obj.about_image, 'url'):
            url = about_obj.about_image.url
        else:
            url = None

        context['about'] = about_obj
        context['image'] = url
        context['media'] = SocialMedia.objects.filter()

        return context

class ContactTemplateView(TemplateView):
    """Rendering of the contact.html page and include form for messages"""

    template_name = 'contact.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # models needed for rendering
        contact_obj = Contact.objects.get(active=True)

        # check the image field
        if contact_obj.contact_image and hasattr(contact_obj.contact_image, 'url'):
            url = contact_obj.contact_image.url
        else:
            url = None

        context['form'] = MessageForm()
        context['contact'] = contact_obj
        context['image'] = url
        context['media'] = SocialMedia.objects.filter()
        return context

        # form message
    def post(self, request, *args, **kwargs):
        """form submission"""
        form = MessageForm(request.POST)

        if form.is_valid():
            new_message = Message(
                name=form.cleaned_data['name'],
                email_adress=form.cleaned_data['email_adress'],
                phone_number=form.cleaned_data['phone_number'],
                message_text = form.cleaned_data['message_text']
            )
            new_message.save()
            return redirect(IndexTemplateView)  # redirects to home page on success
        return self.render_to_response(self.get_context_data(form=form))



class PostTemplateView(TemplateView):
    """Rendering of the post.html page"""

    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        """post page rendering"""
        context = super().get_context_data(**kwargs)

        social_media_obj = SocialMedia.objects.filter(active=True)
        publication = get_object_or_404(Publication, id=self.kwargs.get('id'))
        sources = Sources.objects.filter(publication = publication).order_by('order')
        text_publicantion = Text.objects.filter(publication = publication).order_by('order')

        context['publication'] = publication
        context['texts'] = text_publicantion
        context['media'] = social_media_obj
        context['sources'] = sources
        return context