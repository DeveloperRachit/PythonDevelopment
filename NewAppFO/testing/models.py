from django.db import models
from _future_ import unicode_literals
# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=30)

class Meta:
    db_table="student"    