from django.db import models

# Create your models here.
class Employee(models.Model):
	bonappetitemployeeid = models.IntegerField(db_column='EmployeeID', primary_key=True) # Field name made lowercase.
	namefirst = models.CharField(db_column='NameFirst', max_length=-1, blank=True) # Field name made lowercase.
	namelast = models.CharField(db_column='NameLast', max_length=-1, blank=True) # Field name made lowercase.
	#permissionsid = models.ForeignKey('Permissions', db_column='PermissionsID', blank=True, null=True) # Field name made lowercase.
	class Meta:
		managed = False
		db_table = 'Employee'
	
	def __unicode__(self):
		return u'%s %s' % (self.namefirst, self.namelast)