from django.db import models


class Todo(models.Model):
	text = models.CharField(max_length=120)
	done = models.BooleanField(default=False)

	def __str__(self):
		return self.text

