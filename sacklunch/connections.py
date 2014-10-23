#connections

import urllib
import hashlib


class URLFetcher():
	url = None
	result = None

	def __init__(self):
		self.url = ''

	def getResponse(self, data):
		self.result = urllib.urlOpen(url=url, data=data).read()



