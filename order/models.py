from django.db import models
from entry.models import Entry
from bonappetitemployee.models import Bonappetitemployee
from datetime import datetime, timedelta

# Create your models here.
class Order(models.Model):
	orderid = models.AutoField(db_column='OrderID', primary_key=True) # Field name made lowercase.
	entryid = models.ForeignKey(Entry, db_column='EntryID', default=True, blank=True, null=True) # Field name made lowercase.
	namefirst = models.CharField(db_column='NameFirst', max_length=-1, blank=True) # Field name made lowercase.
	namelast = models.CharField(db_column='NameLast', max_length=-1, blank=True) # Field name made lowercase.
	authenticated = models.BooleanField(db_column='Authenticated', default=False) # Field name made lowercase.
	processed = models.BooleanField(db_column='Processed', default=False) # Field name made lowercase.
	processedbyid = models.IntegerField(db_column='ProcessedByID', default=0, blank=True, null=True) # Field name made lowercase.
	processedon = models.DateField(db_column='ProcessedOn', blank=True, null=True) # Field name made lowercase.
	duedate = models.DateField(db_column='DueDate', default=datetime.now() + timedelta(days=30), blank=True, null=True) # Field name made lowercase.
	modified = models.DateTimeField(db_column='Modified', auto_now=True) # Field name made lowercase.
	created = models.DateField(db_column='Created', auto_now_add=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Order'

	def __unicode__(self):
		return str(self.orderid)
	def create():
		entryid=0
		namefirst=""
		namelast=""
		authenticated=False
		processed=False
		processedon='null'
		processedbyid='null'
		modified = datetime.datetime.now()
		created = datetime.datetime.now()