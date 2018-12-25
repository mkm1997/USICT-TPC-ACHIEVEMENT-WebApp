from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    e_no = models.CharField(max_length=11,validators=[RegexValidator(regex='^.{11}$', message='Length has to be 4', code='nomatch')])
    # college = models.CharField(max_length=200,blank=True)
    # programme = models.CharField(max_length=200,blank=True)
    # stream = models.CharField()
    # current_year
    def __str__(self):
        return self.e_no




class Achivements(models.Model):
    image = models.ImageField(blank=True)
    heading = models.CharField(max_length=200,blank=True)
    discription = models.TextField(max_length=4000)
    student = models.ManyToManyField(Student)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.heading


