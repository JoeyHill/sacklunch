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


class ItemEntree(models.Model):
	itementreeid = models.AutoField(db_column='ItemEntreeID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	active = models.BooleanField(db_column="Active", default=True)
	activefrom = models.DateField(db_column="ActiveFrom", null=True, blank=True)
	activeto = models.DateField(db_column="ActiveTo", null=True, blank=True)
	class Meta:
		managed = True
		db_table = 'ItemEntree'
		verbose_name = 'Entree'


	def __unicode__(self):
		return self.description

class ItemDrink(models.Model):
	itemdrinkid = models.AutoField(db_column='ItemDrinkID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	active = models.BooleanField(db_column="Active", default=True)
	activefrom = models.DateField(db_column="ActiveFrom", null=True, blank=True)
	activeto = models.DateField(db_column="ActiveTo", null=True, blank=True)
	class Meta:
		managed = False
		db_table = 'ItemDrink'
		verbose_name = 'Drink'
		

	def __unicode__(self):
		return self.description


class ItemFruit(models.Model):
	itemfruitid = models.AutoField(db_column='ItemFruitID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	active = models.BooleanField(db_column="Active", default=True)
	activefrom = models.DateField(db_column="ActiveFrom", null=True, blank=True)
	activeto = models.DateField(db_column="ActiveTo", null=True, blank=True)
	class Meta:
		managed = False
		db_table = 'ItemFruit'
		verbose_name = 'Fruit'
		

	def __unicode__(self):
		return self.description


class ItemSide(models.Model):
	itemsideid = models.AutoField(db_column='ItemSideID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100) # Field name made lowercase.
	active = models.BooleanField(db_column="Active", default=True)
	activefrom = models.DateField(db_column="ActiveFrom", null=True, blank=True)
	activeto = models.DateField(db_column="ActiveTo", null=True, blank=True)
	class Meta:
		managed = False
		db_table = 'ItemSide'
		verbose_name = 'Side'
		

	def __unicode__(self):
		return self.description