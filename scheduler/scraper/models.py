from django.db import models


class Department(models.Model):
    full_name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s (%s)', self.full_name, self.abbreviation


class Instructor(models.Model):
    # a department can have many instructors
    department = models.ForeignKey(to=Department, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __unicode__(self):
        return '%s %s', self.first_name, self.last_name


class Course(models.Model):
    # a department can have many courses
    department = models.ManyToManyField(to=Department)
    course_number = models.CharField(max_length=8)
    course_name = models.CharField(max_length=128)

    def __unicode__(self):
        return '%s %s %s', self.department, self.course_number, self.course_name


class Section(models.Model):
    # a course can have many sections
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    section_number = models.CharField(max_length=8)
    location = models.CharField(max_length=128)
    # an instructor can have many sections, and a section can have many instructors
    instructor = models.ManyToManyField(to=Instructor)

    def __unicode__(self):
        return '%s %s %s', self.section_number, self.location, self.instructor


class TimeSlot(models.Model):
    # a section can have many timeslots
    section = models.ForeignKey(to=Section, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __unicode__(self):
        return '%s', self.duration


class EmoryAtlasCourse(models.Model):
    related_courses = models.CharField(max_length=128)
    grading = models.CharField(max_length=32)
    opus_number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    credit = models.IntegerField()
    notes = models.CharField(max_length=128)
    ger = models.CharField(max_length=32)
    resources = models.TextField()
    description = models.TextField()
    topic = models.CharField(max_length=128)
    schedule = models.CharField(max_length=512)
