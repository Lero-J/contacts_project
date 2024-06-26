from django.db import models

# Create your models here.



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


