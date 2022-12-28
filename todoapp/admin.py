from django.contrib import admin

# Register your models here.
from .models import user,task

admin.site.register(user)
admin.site.register(task)