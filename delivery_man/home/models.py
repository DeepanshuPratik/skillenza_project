from django.db import models

# Create your models here.
class Worker(models.Model):
	name = models.CharField(max_length=30)
	age = models.IntegerField()
	gender = models.CharField(max_length=10)
	def __str__(self) -> str:
		return self.name

class Order(models.Model):
	assignedTo = models.ForeignKey('home.Worker', on_delete=models.CASCADE, blank=-1, null=False)
	item = models.CharField(max_length=50)
	location = models.CharField(max_length=150)
	orderedBy = models.CharField(max_length=30)