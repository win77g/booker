
from django.contrib import admin
from .models import *
# Register your models here.
class CategoriesAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
      list_display = [field.name for field in Categories._meta.fields]

class Meta:
    model = Categories
# Register your models here.
admin.site.register(Categories,CategoriesAdmin)
