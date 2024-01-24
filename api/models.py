from django.db import models

# Create your models here.
class Invoice(models.Model):
    date=models.DateField()
    customer_name=models.CharField(max_length=150)

class InvoiceDetail(models.Model):
    description=models.TextField()
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    price=models.IntegerField()
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
# nvoice (ForeignKey), description, quantity, unit_price, price