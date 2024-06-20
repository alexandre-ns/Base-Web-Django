from django.db import models
from django.core.validators import RegexValidator

class Publication(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True)
    posted_by = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Text(models.Model):
    name = models.CharField(max_length=150)
    content_text = models.TextField()
    order = models.PositiveIntegerField(null=True, blank=True)
    publication = models.ForeignKey(Publication, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Home(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=250)
    home_image = models.ImageField(upload_to='', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Página inicial"
        verbose_name_plural = "Página inicial"

class About(models.Model):
    title = models.CharField(max_length=150)
    content_text = models.TextField()
    about_image = models.ImageField(upload_to='', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=150)
    content_text = models.TextField()
    about_image = models.ImageField(upload_to='', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Message(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    name = models.CharField(max_length=150)
    email_adress = models.EmailField(max_length=150)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    message_text = models.TextField()

    def __str__(self):
        return self.name
    
class Social_Media(models.Model):
    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    GITHUB = "github"

    SOCIAL_MEDIA_CHOICES = {
        TWITTER: "X - TWITTER",
        INSTAGRAM: "INSTAGRAM",
        FACEBOOK: "FACEBOOK",
        GITHUB: "GITHUB",
    }
    type_media = models.CharField(
        max_length=15,
        choices=SOCIAL_MEDIA_CHOICES,
        default=FACEBOOK,
    )
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.name