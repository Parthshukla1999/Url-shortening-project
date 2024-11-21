from django.db import models
# Create your models here.

class UrlLinks(models.Model):
    full_url = models.TextField(blank=True)
    short_url = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    