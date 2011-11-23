from django.db import models

class Event(models.Model):
	title = models.CharField('event title', max_length=200)
	date = models.DateTimeField('event date')
	description = models.TextField('event description', null=True, blank=True)
	location = models.CharField('event location', max_length=200)
	#photo = models.ImageField('preview photo', null=True, blank=True)
	
class Person(models.Model): 
	first_name = models.CharField('first name', max_length=200)
	last_name = models.CharField('last name', max_length=200)
	event = models.ForeignKey(Event)
	
# Create your models here.
