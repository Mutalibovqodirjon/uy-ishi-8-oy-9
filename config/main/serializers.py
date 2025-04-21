from rest_framework import serializers
from .models import Class, Teacher, Student


class GroupSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='class_name')

    class Meta:
        model = Class
        fields = ['id', 'title']


class TutorSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, source='class_name')

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'price', 'groups']

    def create(self, validated_data):
        groups_data = validated_data.pop('class_name', [])
        teacher = Teacher.objects.create(
            full_name=validated_data['full_name'],
            price=validated_data['price']
        )
        for group_data in groups_data:
            group_obj, _ = Class.objects.get_or_create(**group_data)
            teacher.class_name.add(group_obj)
        return teacher


class LearnerSerializer(serializers.ModelSerializer):
    group_info = GroupSerializer(source='class_name', read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(queryset=Class.objects.all(), source='class_name')

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'group_info', 'group_id']