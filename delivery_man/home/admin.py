from django.contrib import admin
from .models import * 

class WorkerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'age', 'gender')

class OrderAdmin(admin.ModelAdmin):
	list_display = ('id','assignedTo', 'location', 'item', 'location', 'orderedBy')

admin.site.register(Order, OrderAdmin)
admin.site.register(Worker, WorkerAdmin)