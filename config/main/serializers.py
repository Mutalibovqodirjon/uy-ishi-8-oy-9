from rest_framework import serializers
from .models import Teacher, Student, Class


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']



class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True, read_only=True)
    class_name = ClassSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id','full_name','teachers', 'class_name']

