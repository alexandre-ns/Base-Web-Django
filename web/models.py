from django.db import models

# Model that defines the appearance of the home(index.html) web page
class Home(models.Model):
    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    sub_title = models.CharField("Sub Titulo na página", max_length=250, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    home_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    def __str__(self):
        return self.title if self.title != None else str(self.active)
    
    class Meta:
        verbose_name = "Página inicial"
        verbose_name_plural = "Página inicial"

# Model that defines the appearance of the About.html web page
class About(models.Model):
    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    content_text = models.TextField("Texto da página")
    about_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Página Sobre"

# Model that defines the appearance of the contact.html page
class Contact(models.Model):
    title = models.CharField("Titulo na página", max_length=150, blank=True, null=True)
    tab_title = models.CharField("Titulo na aba", max_length=50, blank=True, null=True)
    content_text = models.TextField("Texto da página")
    contact_image = models.ImageField("Imagem cabeçalho", upload_to='images', blank=True, null=True)
    active = models.BooleanField("Página ativa", default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Página Contatos"

    
