from django.db import models

# Create your models here.
class Feedback(models.Model):
	email = models.CharField(max_length=255)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.email} | {self.message}"
