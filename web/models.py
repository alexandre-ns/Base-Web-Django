from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)  # Título da 
    sub_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Data e hora de criação

    def __str__(self):
        return self.title



class Image(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='publications/images/', blank=True, null=True)  # Imagem opcional
    models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name
    

class Text(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name