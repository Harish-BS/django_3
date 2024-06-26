from django.contrib import admin
from . import models

admin.site.register(models.dept)
admin.site.register(models.role)
admin.site.register(models.user)