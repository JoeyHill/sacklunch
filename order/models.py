from django.db import models
from entry.models import Entry
from bonappetitemployee.models import Bonappetitemployee

# Create your models here.
class Order(models.Model):
	orderid = models.IntegerField(db_column='OrderID', primary_key=True) # Field name made lowercase.
	entryid = models.ForeignKey(Entry, db_column='EntryID', blank=True, null=True) # Field name made lowercase.
	namefirst = models.CharField(db_column='NameFirst', max_length=-1, blank=True) # Field name made lowercase.
	namelast = models.CharField(db_column='NameLast', max_length=-1, blank=True) # Field name made lowercase.
	authenticated = models.BooleanField(db_column='Authenticated') # Field name made lowercase.
	processed = models.BooleanField(db_column='Processed') # Field name made lowercase.
	processedbyid = models.ForeignKey(Bonappetitemployee, db_column='ProcessedByID', blank=True, null=True) # Field name made lowercase.
	processedon = models.DateField(db_column='ProcessedOn', blank=True, null=True) # Field name made lowercase.
	duedate = models.DateField(db_column='DueDate', blank=True, null=True) # Field name made lowercase.
	modified = models.DateTimeField(db_column='Modified') # Field name made lowercase.
	created = models.DateField(db_column='Created', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Order'

	def __unicode__(self):
		return self.orderid