from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Language)
admin.site.register(Unit)
admin.site.register(UnitContent)
admin.site.register(CourseRegistration)
admin.site.register(Question)
admin.site.register(Answer)