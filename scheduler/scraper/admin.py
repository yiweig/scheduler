from django.contrib import admin

from .models import Department, Instructor, Course, Section, TimeSlot

admin.site.register([Department, Instructor, Course, Section, TimeSlot])
