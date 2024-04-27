from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    prerequisites = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    capacity = models.IntegerField()

class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    days = models.CharField(max_length=10)
    startTime = models.TimeField()
    endTime = models.TimeField()
    roomNo = models.CharField(max_length=10)

class StudentsReg(models.Model):
    id = models.AutoField(primary_key=True)
    studentId = models.ForeignKey('Student', on_delete=models.CASCADE)
    courseId = models.ForeignKey(Course, on_delete=models.CASCADE)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
