from django.db import models

class Reporter(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	alias = models.CharField(max_length=16)
	phone = models.CharField(max_length=30)
	email = models.EmailField(blank=True)

	def __unicode__(self):
		return "%s %s" %\
		(self.first_name, self.last_name)

class Supply(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=4)

	def __unicode__(self):
		return self.name

class Location(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=4)

	def __unicode__(self):
		return self.name

class SupplyLocation(models.Model):
	supply = models.ForeignKey(Supply)
	location = models.ForeignKey(Location)
	quantity = models.IntegerField()
	
	def __unicode__(self):
		return "%s at %s" %\
		(self.supply.name, self.location.name)

