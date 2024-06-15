from django.db import models
from polymorphic.models import PolymorphicModel


class Publication(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class GenericContent(models.Model):
    TEXT = "TXT"
    IMAGE = "IMG"
    YEAR_IN_SCHOOL_CHOICES = {
        TEXT: "Texto",
        IMAGE: "Imagem",
    }
    type_content = models.CharField(max_length=3, choices=YEAR_IN_SCHOOL_CHOICES, default=TEXT)
    order = models.PositiveIntegerField(null=True, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)

class Image(GenericContent):
    name = models.CharField(max_length=150)
    content_image = models.ImageField(upload_to='web/images/', blank=True, null=True) 
    #publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)
    #order = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Text(GenericContent):
    name = models.CharField(max_length=150)
    content_text = models.TextField()
    #publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return self.name
    
    class MyModel(PolymorphicModel):
        pass