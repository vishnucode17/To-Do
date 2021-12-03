from django.contrib import admin
from . models import Tasks,Tasktables
# Register your models here.

class TasksAdmin(admin.ModelAdmin):
    list_display=('user_id',)
    def active(self, obj): 
        return obj.is_active == 1

class TasktablesAdmin(admin.ModelAdmin):
    list_display=('title',)
    def active(self, obj): 
        return obj.is_active == 1

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Tasktables, TasktablesAdmin)