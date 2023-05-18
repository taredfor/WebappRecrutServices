from django.contrib import admin
from .models import Questions, ObjectsPlanet, ObjectsSitx, ObjectsQuestion
# Register your models here.
admin.site.register(Questions)
admin.site.register(ObjectsPlanet)
admin.site.register(ObjectsSitx)
admin.site.register(ObjectsQuestion)