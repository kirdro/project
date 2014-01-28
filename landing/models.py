from django.db import models
from django.contrib import admin

# Create your models here.
class Item(models.Model):
	titleru 		= models.CharField(max_length=1000)
	titleen 		= models.CharField(max_length=1000, blank=True)
	discriptionru 	= models.TextField()
	discriptionen 	= models.TextField(blank=True)
	image 			= models.ImageField(upload_to='uploaded')
	price 			= models.FloatField()
	date  			= models.DateTimeField()
	def __unicode__(self):
		return self.titleru

class CallMe(models.Model):
	email  			= models.CharField(max_length=100)
	phone 			= models.CharField(max_length=100)
	item 			= models.ForeignKey(Item, blank=True, null=True)
	date 			= models.DateTimeField()
	def __unicode__(self):
		return '%s / %s / %s' % (self.phone, self.email, self.item)

class GetAction(models.Model):
	email  			= models.CharField(max_length=100)
	phone 			= models.CharField(max_length=100)
	date 			= models.DateTimeField()
	def __unicode__(self):
		return '%s / %s' % (self.phone, self.email)

admin.site.register(Item)
admin.site.register(CallMe)
admin.site.register(GetAction)