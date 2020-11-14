from django.db import models

# Create your models here.


class Student(models.Model):
    s_name = models.CharField(max_length=32)
    my_class = models.ForeignKey(
        'Classes', related_name='students', on_delete=models.CASCADE)
    score = models.IntegerField()


class Teacher(models.Model):
    t_name = models.CharField(max_length=32)
    sex = models.IntegerField(choices=((1, 'male'), (2, 'female')))
    age = models.IntegerField()


class Classes(models.Model):
    c_name = models.CharField(max_length=32)
    teachers = models.ManyToManyField('Teacher', related_name='classes')
