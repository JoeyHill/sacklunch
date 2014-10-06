from django.db import models

# Create your models here.
class ItemType(models.Model):
	itemtypeid = models.AutoField(db_column="ItemTypeID", primary_key=True)
	description = models.CharField(db_column="Description", max_length=100)
	class Meta:
		managed=False
		db_table="ItemType"

	def __unicode__(self):
		return self.description

class Item(models.Model):
	itemid = models.AutoField(db_column='ItemID', primary_key=True) # Field name made lowercase.
	itemtypeid = models.ForeignKey(ItemType, db_column='ItemTypeID', default=1) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	maxquantity = models.IntegerField(db_column='MaxQuantity', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Items'

	def __unicode__(self):
		return self.description

class SubItem(models.Model):
	subitemid=models.AutoField(db_column="SubItemID", primary_key=True)
	itemid = models.ForeignKey(Item, db_column='ItemID', default=True, blank=True, null=True)
	description=models.CharField(db_column="Description", max_length=100)
	class Meta:
		managed=False
		db_table="SubItem"
	def __unicode__(self):
		return self.description