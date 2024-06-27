"""Models of PUBLICAÇÕES"""

from django.db import models

class Publication(models.Model):
    """Create publication on the web site"""

    title = models.CharField("*Titulo", max_length=200)
    sub_title = models.CharField("Sub Titulo", max_length=255, blank=True, null=True)
    created_at = models.DateTimeField("Data de criação", blank=True, null=True)
    published_at = models.DateTimeField("*Data de Publicação", auto_now_add=True)
    posted_by = models.CharField("*Autor", max_length=100)

    class Meta:
        verbose_name = "Publicação"
        verbose_name_plural = "Publicações"

    def __str__(self):
        return f"{self.title}"


class Text(models.Model):
    """Texts that will be displayed in the post"""

    name = models.CharField("Titulo ou Sub Titulo", max_length=150, null=True, blank=True)
    content_text = models.TextField("*Texto da Publicação")
    order = models.PositiveIntegerField("*Ordem do texto")
    publication = models.ForeignKey(
        Publication,
        verbose_name="*Publicação",
        on_delete=models.CASCADE
    ) # Each post can contain one or more texts

    class Meta:
        verbose_name = "Texto"
        verbose_name_plural = "Textos"

    def __str__(self):
        return f"{self.name}"


class Sources(models.Model):
    """Souces of a post"""

    title = models.CharField("Titulo ou Sub Titulo", max_length=150, null=True, blank=True)
    order = models.PositiveIntegerField(
        "*Ordem do texto" # The order field defines the display order on the website
    )
    url = models.URLField("*URL", max_length=200)
    publication = models.ForeignKey(
        Publication,
        verbose_name="*Publicação",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Fonte"
        verbose_name_plural = "Fontes"

    def __str__(self):
        return f"{self.title}"
