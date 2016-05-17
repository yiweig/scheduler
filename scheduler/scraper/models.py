from django.db import models


class Department(models.Model):
    full_name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=32)


class Instructor(models.Model):
    # a department can have many instructors
    department = models.ForeignKey(to=Department, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Course(models.Model):
    # a department can have many courses
    department = models.ManyToManyField(to=Department)
    course_number = models.CharField(max_length=8)
    course_name = models.CharField(max_length=128)


class Section(models.Model):
    # a course can have many sections
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    # an instructor can have many sections, and a section can have many instructors
    instructor = models.ManyToManyField(to=Instructor)
    location = models.CharField(max_length=128)


class TimeSlot(models.Model):
    # a section can have many timeslots
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)
    duration = models.DurationField()
