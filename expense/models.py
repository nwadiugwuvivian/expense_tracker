from django.db import models
from customer.models import Customer


# Create your models here.
class Expense(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name="expenses")
    expense_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_spent = models.DateField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.expense_name}"
