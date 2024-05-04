from django.db import models

class SplinterDataPoint(models.Model):
	# Tag Name
	tag_name = models.CharField(max_length=256)
	# Tag Value/ Status
	tag_value = models.IntegerField()
	# Timestamp
	timestamp = models.DateTimeField()