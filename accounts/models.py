from django.db import models

class User(models.Model):
    Username = models.CharField('Event Name', max_length=120)
    