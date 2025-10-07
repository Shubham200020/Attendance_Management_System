from django.db import models

# Create your models here.
class USERS(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"
    class Gender(models.TextChoices):
        Male='Male','MALE'
        Female='Female','FEMALE'
        Others='Others','OTHERS'
    id=models.AutoField(primary_key=True)
    #totalAtten=models.IntegerField()
    #totalDays=models.IntegerField()
    name=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10,choices=Gender.choices)
    role=models.CharField(max_length=50,choices=Role.choices)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=16)

class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.name

# class Subject(models.Model):
#     course=models.ForeignKey(Course)
#     course_name=models.CharField()
class ClassScedule(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    teacher=models.ForeignKey(USERS,on_delete=models.CASCADE,limit_choices_to={
        'role':USERS.Role.TEACHER
    })
    start=models.TimeField()
    end=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return f"{self.course.name} by {self.teacher.username}"


class Attendance(models.Model):
    class Status(models.TextChoices):
        PRESENT = "PRESENT", "Present"
        ABSENT = "ABSENT", "Absent"
        LATE = "LATE", "Late"
    id=models.AutoField(primary_key=True)
    student=models.ForeignKey(USERS,on_delete=models.CASCADE)
    date=models.DateField()
    #time=models.TimeField()
    class_schedule=models.ForeignKey(ClassScedule,on_delete=models.CASCADE)

    state=models.CharField(max_length=50,choices=Status.choices)
