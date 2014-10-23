from django.db import models



# Create your models here.

class swBread(models.Model):	
	id = models.AutoField(db_column='swBreadID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100)
	
	class Meta:
		managed = False
		db_table = 'swBread'
		verbose_name = 'BreadType'

	
	def __unicode__(self):
		return self.description

class swMeat(models.Model):	
	id = models.AutoField(db_column='swMeatID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100)
	
	class Meta:
		managed = False
		db_table = 'swMeat'
		verbose_name = 'MeatType'
	
	def __unicode__(self):
		return self.description

class swCheese(models.Model):	
	id = models.AutoField(db_column='swCheeseID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100)
	
	class Meta:
		managed = False
		db_table = 'swCheese'
		verbose_name = 'CheeseType'
	
	def __unicode__(self):
		return self.description

class Topping(models.Model):
	toppingid = models.AutoField(db_column='ToppingID', primary_key=True)
	description = models.CharField(db_column='Description', max_length=100)
	class Meta:
		managed=False
		db_table='Topping'
		verbose_name='Topping'
	def __unicode__(self):
		return self.description

class Sandwich(models.Model):	
	sandwichid = models.AutoField(db_column='SandwichID', primary_key=True) # Field name made lowercase.
	orderid = models.IntegerField(db_column='OrderID', editable=False) # Field name made lowercase.
	swbreadid = models.ForeignKey(swBread, db_column='swBreadID') # Field name made lowercase.
	swmeatid = models.ForeignKey(swMeat,db_column='swMeatID') # Field name made lowercase.
	swcheeseid = models.ForeignKey(swCheese, db_column='swCheeseID') # Field name made lowercase.
	toppings = models.ManyToManyField(Topping, through='SandwichTopping')
	def description(self):
		oid = 0
		if self.orderid == None:
			oid = 0
		else:
			oid = self.orderid
		from sacklunch.order.models import Order
		o = Order.objects.get(pk=oid)
		return "["+self.swbreadid.description+", "+self.swmeatid.description+", "+self.swcheeseid.description+"]"

	class Meta:
		managed = False
		db_table = 'Sandwich'
		verbose_name_plural = 'Sandwiches'
	
	def __unicode__(self):
		
		return self.description()

class SandwichTopping(models.Model):
	sandwichtoppingid = models.AutoField(db_column='SandwichToppingID', primary_key=True)
	sandwichid=models.ForeignKey(Sandwich, db_column="SandwichID")
	toppingid=models.ForeignKey(Topping, db_column="ToppingID")
	class Meta:
		managed=False
		db_table='SandwichTopping'
		verbose_name = 'Sandwich Topping'


