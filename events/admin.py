from django.contrib import admin
from .models import *
# Register your models here.
class EventsAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Events._meta.fields]

class Meta:
    model = Events
# Register your models here.
admin.site.register(Events,EventsAdmin)
