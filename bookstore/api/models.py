from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(_("Primeiro Nome"), max_length=30)
    last_name = models.CharField(_("Último Nome"), max_length=30)
    birthday = models.DateField(_("Data de nascimento"))
    created_at = models.DateTimeField(_("Criado em:"), auto_now_add=True)


class Book(models.Model):
    author = models.ForeignKey(
        "api.Author", verbose_name=_("Autor"), on_delete=models.CASCADE
    )
    title = models.CharField(_("Título"), max_length=100)
    pages = models.IntegerField(_("Páginas"))
    publish_date = models.DateField(_("Data da publicação"))
    price = models.FloatField(_("Preço"))
    created_at = models.DateTimeField(_("Criado em:"), auto_now_add=True)
