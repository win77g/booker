from django.contrib import admin
from .models import *
# Register your models here.
class BillAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Bill._meta.fields]

class Meta:
    model = Bill
# Register your models here.
admin.site.register(Bill,BillAdmin)
