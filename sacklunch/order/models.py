from django.db import models
from sacklunch.entry.models import Entry
from sacklunch.employee.models import Employee
from datetime import datetime, timedelta
from sacklunch.item.models import *
from django import forms
from django.forms import ModelForm
from sacklunch.sandwich.models import Sandwich
from rest_framework import permissions
from django.contrib.auth.models import User


# Create your models here.
class Order(models.Model):
	readonly_fields= ('duedate')
	orderid = models.AutoField(db_column='OrderID', primary_key=True) # Field name made lowercase.
	entryid = models.ForeignKey(Entry, db_column='EntryID', blank=True, null=True, default=776) # Field name made lowercase.
	authenticated = models.BooleanField(db_column='Authenticated', default=False) # Field name made lowercase.
	processed = models.BooleanField(db_column='Processed', default=False) # Field name made lowercase.
	processedbyid = models.IntegerField(db_column='ProcessedByID', default=0, blank=True, null=True) # Field name made lowercase.
	processedon = models.DateField(db_column='ProcessedOn', blank=True, null=True) # Field name made lowercase.
	duedate = models.DateField(db_column='DueDate', default=datetime.now() + timedelta(days=1), blank=True, null=True) # Field name made lowercase.
	modified = models.DateTimeField(db_column='Modified', auto_now=True, editable=False) # Field name made lowercase.
	created = models.DateField(db_column='Created', editable=False, auto_now_add=True, null=True) # Field name made lowercase.
	itementreeid = models.ForeignKey(ItemEntree, db_column='ItemEntreeID', verbose_name='Entree')
	itemdrinkid = models.ForeignKey(ItemDrink, db_column='ItemDrinkID', verbose_name='Drink')
	itemfruitid = models.ForeignKey(ItemFruit, db_column='ItemFruitID', verbose_name='Fruit')
	itemsideid = models.ForeignKey(ItemSide, db_column='ItemSideID', verbose_name='Side')
	sandwichid = models.ForeignKey(Sandwich, db_column='SandwichID', verbose_name='Sandwich', blank=True, null=True)
	owner = models.ForeignKey(User, db_column='owner')
	class Meta:
		managed = False
		db_table = 'Order'

	def __unicode__(self):
		return str(self.duedate)+" - "+self.entryid.namefirst+" "+self.entryid.namelast

	def get_field_values(self):
		return [field.value_to_string(self) for field in Order._meta.fields]


class OrderFailureEnum(models.Model):	
	orderfailureenumid = models.AutoField(db_column='OrderFailureEnumID', primary_key=True) # Field name made lowercase.
	description = models.CharField(db_column='Description', max_length=100, blank=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'OrderFailureEnum'
	def __unicode__(self):
		return self.description


class OrderFailure(models.Model):
	orderfailureid = models.AutoField(db_column='OrderFailureID', primary_key=True) # Field name made lowercase.
	orderid = models.ForeignKey(Order, db_column='OrderID', blank=True, null=True) # Field name made lowercase.
	failuredate = models.DateField(db_column='FailureDate') # Field name made lowercase.
	orderfailureenumid = models.ForeignKey(OrderFailureEnum, db_column='OrderFailureEnumID') # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'OrderFailures'

	def __unicode__(self):
		return self.orderfailureid

class OrderItems(models.Model):
	orderitemsid = models.AutoField(db_column='OrderItemsID', primary_key=True) # Field name made lowercase.
	orderid = models.ForeignKey(Order, db_column='OrderID') # Field name made lowercase.
	itemid = models.ForeignKey(Item, db_column='ItemID') # Field name made lowercase.
	itemquantity = models.IntegerField(db_column='ItemQuantity') # Field name made lowercase.
	orderfilled = models.BooleanField(db_column='OrderFilled') # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'OrderItems'
		verbose_name='Order Item'
	def __unicode__(self):
		return self.orderitemsid


