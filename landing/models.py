from django.db import models
from django.contrib import admin

# Create your models here.
class Item(models.Model):
	titleru = models.CharField(max_length=1000)
	titleen = models.CharField(max_length=1000)
	discriptionru = models.TextField()
	discriptionen = models.TextField()
	image = models.ImageField(upload_to='uploaded')
	price = models.FloatField()
	date  = models.DateTimeField()

admin.site.register(Item)