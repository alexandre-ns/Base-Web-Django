from django.db import models

# Create publication on the web site
class Publication(models.Model):
    title = models.CharField("*Titulo", max_length=200)
    sub_title = models.CharField("Sub Titulo", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Data de criação", blank=True, null=True)
    published_at = models.DateTimeField("*Data de Publicação", auto_now_add=True)
    posted_by = models.CharField("*Autor", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

# Texts that will be displayed in the post
class Text(models.Model):
    name = models.CharField("Titulo ou Sub Titulo", max_length=150, null=True, blank=True)
    content_text = models.TextField("*Texto da Publicação")
    order = models.PositiveIntegerField("*Ordem do texto")
    publication = models.ForeignKey(Publication, verbose_name="*Publicação",  on_delete=models.CASCADE) # each post can contain one or more texts 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Texto"
        verbose_name_plural = "Textos"

# souces of a post
class Sources(models.Model):
    title = models.CharField("Titulo ou Sub Titulo", max_length=150, null=True, blank=True)
    order = models.PositiveIntegerField("*Ordem do texto") # The order field defines the display order on the website
    url = models.URLField("*URL", max_length=200)
    publication = models.ForeignKey(Publication, verbose_name="*Publicação",  on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Fonte"
        verbose_name_plural = "Fontes"