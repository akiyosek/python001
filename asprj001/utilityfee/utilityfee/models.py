from django.db import models

# Create your models here.
class Utilityfee(models.Model):
    billing_date = models.DateTimeField('請求日')
    billing_type = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    detail = models.CharField(max_length=200)
    def __str__(self):
        return self.detail + ' ￥' + str(self.cost)