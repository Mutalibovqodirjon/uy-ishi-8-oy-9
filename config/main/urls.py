from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomUserViewSet,
    ClassViewSet,
    GroupViewSet,
    LessonViewSet,
    TeacherViewSet,
    StudentViewSet
)

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
