from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID field
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=254, unique=True)  # Increased max length for email
    password = models.CharField(max_length=128)  # Increased length for secure hashed passwords

    def __str__(self):
        return self.username

class Expense(models.Model):
    username = models.CharField(max_length=20)  # Not unique
    day = models.PositiveIntegerField()
    month = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    item = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.username
