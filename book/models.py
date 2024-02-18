from django.db import models

# Create your models here.

class Books(models.Model):
    Name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    genre=models.CharField(max_length=200)

    def __str__(self):
        return self.Name
    
    