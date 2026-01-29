from django.db import models

class Users(models.Model):

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    user_name = models.CharField(max_length=200, unique=True)

    email = models.EmailField(unique=True)

    age = models.PositiveIntegerField(null=True)

    bio = models.TextField(null=True)

    password = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)



