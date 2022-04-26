from django.contrib import admin
from Input.models import DataInput, TaskExecution

# Register your models here.
class DataInputAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', 'run_time')

class TaskExecutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'execution_date')

admin.site.register(DataInput, DataInputAdmin)
admin.site.register(TaskExecution, TaskExecutionAdmin)