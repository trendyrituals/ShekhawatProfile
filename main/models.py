from django.db import models

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=50,blank=False)
	img = models.ImageField(blank=False)
	bio = models.TextField(blank=False)


	def __str__(self):
		return self.name
