"""Models of WEB SITE"""
from django.db import models


class Home(models.Model):
    """Model that defines the appearance of the home(index.html) web page"""

    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    sub_title = models.CharField("Sub Titulo na página", max_length=250, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    home_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    class Meta:
        verbose_name = "Página inicial"
        verbose_name_plural = "Página inicial"

    def __str__(self):
        return self.title if self.title is not None else "PÁGINA INICIAL"


class About(models.Model):
    """Model that defines the appearance of the About.html web page"""

    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    content_text = models.TextField("Texto da página")
    about_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Página Sobre"

    def __str__(self):
        return f"{self.title}"



class Contact(models.Model):
    """Model that defines the appearance of the contact.html page"""

    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    content_text = models.TextField("Texto da página")
    contact_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Página Contatos"

    def __str__(self):
        return f"{self.title}"
