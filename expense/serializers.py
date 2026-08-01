from rest_framework import serializers
from .models import Expense


class CreateExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "customer",
            "expense_name",
            "category",
            "amount",
            "date_spent",
            "payment_method",
        ]





class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "id",
            "customer",
            "expense_name",
            "category",
            "amount",
            "date_spent",
            "payment_method",

        ]

