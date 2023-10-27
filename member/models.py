from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True, unique=True)
    username = models.CharField(max_length=255, blank=True, null=True, unique=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    telphone = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    quartier = models.CharField(max_length=255, blank=True, null=True)
    follow = models.ManyToManyField("self", symmetrical=True, related_name="followed_by")
    picture = models.ImageField(upload_to="images/", default="default.jpeg", blank=True, null=True)

    def __str__(self):
        return self.username
    
class Client(models.Model):
    id_Us = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_Us

    class Meta:
        verbose_name_plural = "Client"
        db_table = "client"


class Prestateur(models.Model):
    id_Us = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_Us

    class Meta:
        verbose_name_plural = "Prestateur"
        db_table = "prestateur"
