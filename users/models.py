from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    @property
    def is_admin(self):
        return self.is_superuser

    def __str__(self):
        return self.email
