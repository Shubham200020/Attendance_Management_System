from rest_framework import serializers
from .models import USERS,Course,ClassScedule,Attendance
class UserSerilizer(serializers.ModelSerializer):
    class Meta:
        model=USERS
        fields='__all__'

class ClassSceduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassScedule
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'

