from django.contrib import admin
from .models import Project, Task, Priority, User, Category
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Priority)
admin.site.register(User)
admin.site.register(Category)