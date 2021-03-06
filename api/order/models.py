from django.db import models
from api.user.models import CustomUser
from api.product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product_names = models.CharField(max_length=500)
    total_product = models.IntegerField(default=0)
    transaction_id = models.CharField(max_length=50,default=0)
    total_amount = models.CharField(default=0,max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return str(self.user) +"-["+ self.product_names + "]"
