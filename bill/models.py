from django.db import models

# Create your models here.
class Bill(models.Model):

    # value = models.DecimalField(max_digits=10,decimal_places=2, default=0)#total price for all products in order
    # customer_name = models.CharField(max_length=120,blank=True, null=True, default=None)
    value = models.CharField(max_length=120,blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Сумма %s " % (self.id )
    class Meta:
        verbose_name = 'Сумма'
        verbose_name_plural = 'Сумма'

    # def save(self, *args, **kwargs):
    #
    #      super(Order, self).save(*args, **kwargs)
