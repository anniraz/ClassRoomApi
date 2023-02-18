from django.contrib import admin

from apps.courses.models import Courses, CourseMembers

admin.site.register(Courses)
admin.site.register(CourseMembers)
