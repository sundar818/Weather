from django.contrib import admin
from weather_app.models import register

# Register your models here.

class weatherAdmin(admin.ModelAdmin):
    list_display=['name','location']


admin.site.register(register,weatherAdmin)
