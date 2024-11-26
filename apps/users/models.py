from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=25, verbose_name="номер телефона", null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name="адрес проживания", null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
