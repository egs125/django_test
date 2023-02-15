from django.db import models

# Create your models here.
#class Quiz(models.Model):
#  title = models.CharField(max_length=200)
#  body = models.TextField()
#  answer = models.IntegerField()


class Grade(models.Model):
    grade = models.CharField(primary_key=True, max_length=1)
    grade_name = models.CharField(max_length=45)

    class Meta:
      managed = False
      db_table = 'grade'

class User(models.Model):
    name = models.CharField(max_length=45)
    grade = models.CharField(max_length=1)

    class Meta:
      managed = False
      db_table = 'user'