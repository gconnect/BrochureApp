from django.contrib import admin
from .models import Blog, Course, Event


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']
    # prepopulated_fields = {"slug": ("title",)}
admin.site.register(Blog, BlogAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
admin.site.register(Course, CourseAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'created_at')
    list_filter = ['created_at']
    search_fields = ['title']
admin.site.register(Event, EventAdmin)