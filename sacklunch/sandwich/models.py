from django.db import models

# Create your models here.
class Sandwich(models.Model):	
	sandwichid = models.AutoField(db_column='SandwichID', primary_key=True) # Field name made lowercase.
	orderid = models.IntegerField(db_column='OrderID') # Field name made lowercase.
	swbreadid = models.IntegerField(db_column='swBreadID') # Field name made lowercase.
	swmeatid = models.IntegerField(db_column='swMeatID') # Field name made lowercase.
	swcheeseid = models.IntegerField(db_column='swCheeseID') # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Sandwich'
	def __unicode__(self):
		return str(self.sandwichid)