from django.db import models


class Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name




class  Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    price= models.IntegerField()
    class_name = models.ManyToManyField(Class)

    def __str__(self):
        return self.full_name




class Student(models.Model):
    full_name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class,on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

