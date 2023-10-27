from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from member.models import Client, Prestateur


class Category(models.Model):
    choice = (
        ("1", "En vente"),
        ("2", "En location"),
        ("3", "Les deux")
    )
    categorize = models.CharField(max_length=255, choices=choice)


class Boutique(models.Model):
    prix_loc = models.FloatField(blank=True, null=True)
    prix_achat = models.FloatField(blank=True, null=True)
    type = models.CharField(max_length=255)
    box = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Boutique"
        db_table = "boutique"


class Terrain(models.Model):
    prix_loc = models.FloatField(blank=True, null=True)
    prix_achat = models.FloatField(blank=True, null=True)
    superficie = models.CharField(max_length=255)
    chambre = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.superficie

    class Meta:
        verbose_name_plural = "Terrain"
        db_table = "terrain"


class Maison(models.Model):
    stat = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    way = models.CharField(max_length=255, blank=True, null=True)
    prix_loc = models.FloatField(blank=True, null=True)
    prix_achat = models.FloatField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to="images/" ,blank=True, null=True)

    @property
    def word_count(self):
        return len(self.description.split())

    def __str__(self):
        return self.stat

    class Meta:
        verbose_name_plural = "Maison"
        db_table = "maison"


class Chambre(models.Model):
    superficie = models.CharField(max_length=255)

    def __str__(self):
        return self.superficie

    class Meta:
        verbose_name_plural = "Chambre"
        db_table = "chambre"


class Caracteristics(models.Model):
    description = models.CharField(max_length=255)
    climatiser = models.BooleanField(default=False)
    ventiller = models.BooleanField(default=False)
    carreau = models.BooleanField(default=False)
    superficie = models.CharField(max_length=255)
    id_CH = models.ForeignKey(Chambre,
                              on_delete=models.CASCADE)
    id_Ma = models.ForeignKey(Maison, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.description

    @property
    def word_count(self):
        return len(self.description.split())

    class Meta:
        verbose_name_plural = "Caracteristics"
        db_table = "caracteristics"




class Categorize(models.Model):
    Category = (
        ("1", "Maison"),
        ("2", "Boutique"),
        ("3", "Terrain")
    )
    category = models.CharField(max_length=255)


class Poster(models.Model):
    titre = models.CharField(max_length=255, blank=False, null=False, default=None)
    slug = models.SlugField(blank=True)
    description = models.CharField(max_length=255, default=None)
    owner = models.ForeignKey(Prestateur, on_delete=models.CASCADE, null=False, blank=False)
    id_MA = models.ForeignKey(Maison, on_delete=models.CASCADE, null=True, blank=True)
    id_TE = models.ForeignKey(Terrain, on_delete=models.CASCADE, null=True, blank=True)
    id_BO = models.ForeignKey(Boutique, on_delete=models.CASCADE, null=True, blank=True)
    published = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    categorize = models.ManyToManyField(Categorize)

    def __str__(self):
        return self.id_PR

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super.save(*args, **kwargs)

    @property
    def word_count(self):
        return len(self.description.split())

    class Meta:
        verbose_name_plural = "Poster"
        db_table = "poster"

    def get_absolute_url(self):
        return reverse("poster", kwargs={"slug": self.slug})

class Commentaire(models.Model):
    id_Us = models.ForeignKey(User, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    id_Po = models.ForeignKey(Poster, on_delete=models.CASCADE, null=False, blank=True)

    @property
    def word_count(self):
        return len(self.commentaire.split())

    def __str__(self):
        return self.commentaire

    class Meta:
        verbose_name_plural = "Commentaire"
        db_table = "commentaire"


class Emplacement(models.Model):
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255)
    id_Ma = models.ForeignKey(Maison, on_delete=models.CASCADE, null=True, blank=True)
    id_Bo = models.ForeignKey(Boutique, on_delete=models.CASCADE, null=True, blank=True)
    id_Te = models.ForeignKey(Terrain, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.quartier

    class Meta:
        verbose_name_plural = "Emplacement"
        db_table = "emplacement"

class Sale(models.Model):
    vendeur = models.ForeignKey(Prestateur, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    marchandise_post = models.ForeignKey(Poster, on_delete=models.CASCADE)


class Louer(models.Model):
    vendeur = models.ForeignKey(Prestateur, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    marchandise_post = models.ForeignKey(Poster, on_delete=models.CASCADE)