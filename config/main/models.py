from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


class Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.group_name

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='lessons')

    def __str__(self):
        return self.lesson_title

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='teacher_profile')
    full_name = models.CharField(max_length=100)
    price = models.IntegerField()
    classes = models.ManyToManyField(Class, related_name='teachers')

    def __str__(self):
        return self.full_name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

    def __str__(self):
        return self.full_name
