import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def was_published_recently(self):
		# recent means within 1 day
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
	def __str__(self):
		return self.question_text
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
		
class Person(models.Model):
	name = models.CharField(max_length=200)
	question = models.ForeignKey(Question)
	
	def __str__(self):
		return self.name