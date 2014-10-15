from django.db import models
from django.contrib.auth.models import User
import urllib

# Create your models here.
class Entry(models.Model):
	user = models.OneToOneField(User)
	entryid = models.IntegerField(default=0, null=False)
	username = models.EmailField(null=False)


	class Meta:
		managed = False
		db_table = 'Entry'

	def __unicode__(self):
		return u'%s %s' % (self.user.first_name, self.user.last_name)

	def isStarRez(self):

		return True