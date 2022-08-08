from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ("completed",)


admin.site.register(Task)

