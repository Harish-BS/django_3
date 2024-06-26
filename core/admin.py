from django.contrib import admin
from .models import project
from .models import solution
from .models import feature
from .models import task

admin.site.register(project)
admin.site.register(solution)
admin.site.register(feature)
admin.site.register(task)