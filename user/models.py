from django.db import models

#User inner class only with basic fields
class User(models.Model):
    name = models.CharField("Nome", max_length=100, null=True, default=None, blank=True)
    age = models.IntegerField("Idade", default=0)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"