from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Faqat admin foydalanuvchilar uchun yozish huquqi, boshqalar uchun faqat o'qish huquqi.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'

class IsTeacher(permissions.BasePermission):
    """
    Faqat o‘qituvchi foydalanuvchilar uchun ruxsat.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'teacher'

class IsStudent(permissions.BasePermission):
    """
    Faqat talaba foydalanuvchilar uchun ruxsat.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'student'
