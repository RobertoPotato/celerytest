from django.contrib import admin
from Input.models import DataInput

# Register your models here.
class DataInputAdmin(admin.ModelAdmin):
    list_display = ('data',)

admin.site.register(DataInput, DataInputAdmin)