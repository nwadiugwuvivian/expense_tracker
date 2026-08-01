from django.db import models
from customer.models import Customer

# Create your models here.
class Income(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='incomes')
    income_source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()

    def __str__(self):
        return f"{self.income_source}"