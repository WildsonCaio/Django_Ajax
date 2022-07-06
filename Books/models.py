from unicodedata import name
from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    pages = models.IntegerField()
    cover = models.ImageField()
    author = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    
    def __str__(self):
        return self.name
