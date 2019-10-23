from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1, related_name='user_profile')	
	referal = models.ForeignKey(User, on_delete = models.CASCADE, default = 1, related_name = 'referred_user', blank=True, null=True)
	level1 = models.PositiveIntegerField(default=0)
	level2 = models.PositiveIntegerField(default=0)
	level3 = models.PositiveIntegerField(default=0)
	level4 = models.PositiveIntegerField(default=0)
	level5 = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.user.username