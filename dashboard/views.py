from rest_framework.decorators import api_view
from rest_framework.response import Response

from customer.models import Customer
from income.models import Income
from expense.models import Expense



# Create your views here.
@api_view(['GET'])
def customer_dashboard(request,id):
    customer = Customer.objects.get(id=id)
    customer_income = Income.objects.filter(customer=customer)

    total_income = 0

    for income in customer_income:
        total_income += income.amount

    customer_expenses = Expense.objects.filter(customer=customer)

    total_expense = 0

    for expense in customer_expenses:
        total_expense += expense.amount

    remaining_balance = total_income - total_expense

    return Response({
        "customer": f"{customer.first_name} {customer.last_name}",
        "total_income": total_income,
        "total_expense": total_expense,
        "remaining_balance": remaining_balance,
    })

