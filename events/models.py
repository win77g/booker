from django.db import models

class Events(models.Model):

    type = models.CharField(max_length=120,blank=True, null=True, default=None)
    amount = models.DecimalField(max_digits=10,decimal_places=2, default=0)#total price for all products in order
    category = models.CharField(max_length=120,blank=True, null=True, default=None)
    date = models.CharField(max_length=120,blank=True, null=True, default=None)
    description = models.CharField(max_length=120,blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Событие %s " % (self.id )
    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
