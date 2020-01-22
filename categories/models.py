from django.db import models
# Create your models here.
class Categories(models.Model):
    # catname = models.CharField(max_length=100,blank=True, null=True, default=None)
    name = models.CharField(max_length=120,blank=True, null=True, default=None)
    capacity = models.DecimalField(max_digits=10,decimal_places=2, default=0)#total price for all products in order
    # вывод одного поля
    def __str__(self):
        return "Категори %s " % (self.id )
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
