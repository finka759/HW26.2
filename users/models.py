from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="email",
        help_text="укажите email",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="телефон",
        help_text="укажите телефон",
        **NULLABLE,
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        **NULLABLE,
    )
    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=250,
        verbose_name="City",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return f"{self.email}"
