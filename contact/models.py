"""Models of CONTATO E MIDIAS SOCIAIS"""
from django.db import models
from django.core.validators import RegexValidator

class Message(models.Model):
    """ Messages sent by website users"""

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    user_name = models.CharField("Nome", max_length=150)
    email_adress = models.EmailField("Email", max_length=150)
    message_text = models.TextField("Mensagem")
    sent_on = models.DateTimeField("Data de envio", blank=True, null=True)
    phone_number = models.CharField(
        "Telefone", 
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

    def __str__(self):
        return f"{self.user_name}"


class SocialMedia(models.Model):
    """ Social networks displayed on the site """

    TWITTER = "twitter"
    INSTAGRAM = "instagram"
    FACEBOOK = "facebook"
    GITHUB = "github"
    LINKEDIN = "linkedin"

    SOCIAL_MEDIA_CHOICES = {
        TWITTER: "X - TWITTER",
        INSTAGRAM: "INSTAGRAM",
        FACEBOOK: "FACEBOOK",
        GITHUB: "GITHUB",
        LINKEDIN: "LINKEDIN"
    }
    type_media = models.CharField(
        "Rede Social",
        max_length=15,
        choices=SOCIAL_MEDIA_CHOICES,
        default=FACEBOOK,
    )
    name = models.CharField("Nome identificador", max_length=150, blank=True, null=True)
    url = models.URLField("*URL", max_length=200, unique=True)
    active = models.BooleanField("*Rede Social ativa", default=False) # Only the elements with
    #the field active=True will be displayed on the site"

    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"

    def __str__(self):
        return f"{self.name}"
