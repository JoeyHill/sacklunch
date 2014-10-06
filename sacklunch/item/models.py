from django.db import models

# Create your models here.
class Item(models.Model):
	itemid = models.IntegerField(db_column='ItemID', primary_key=True) # Field name made lowercase.
	itemtypeid = models.IntegerField(db_column='ItemTypeID', blank=True, null=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	maxquantity = models.IntegerField(db_column='MaxQuantity', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Items'

	def __unicode__(self):
		return self.description