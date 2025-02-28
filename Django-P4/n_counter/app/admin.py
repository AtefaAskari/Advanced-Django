from django.contrib import admin  # type: ignore
from .models import Food, Consume, HealthGoal

admin.site.register(Food)
admin.site.register(Consume)
admin.site.register(HealthGoal)