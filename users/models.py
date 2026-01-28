from django.db import models

class Users(models.Model):

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    user_name = models.CharField(max_length=255, unique=True)

    email = models.EmailField(unique=True)

    age = models.PositiveIntegerField(null=True, blank=True)

    bio = models.TextField(null=True, blank=True)

    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)



