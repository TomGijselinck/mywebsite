from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	pub_date = models.DateTimeField('date published', default=datetime.now)
	mod_date = models.DateTimeField('date last modified', null=True, blank=True)
	tags = models.ManyToManyField('myblogapp.Tag')
	
	def __str__(self):
		return self.title

class Tag(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	
	def __str__(self):
		return self.title
