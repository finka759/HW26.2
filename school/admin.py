from django.contrib import admin

from school.models import Course, Lesson

# admin.site.register(Course)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Админка юзера"""
    list_display = ('id', 'name', 'description', 'image', 'owner')


admin.site.register(Lesson)
