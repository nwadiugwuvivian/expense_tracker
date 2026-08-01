from rest_framework import serializers
from .models import Income



class CreateIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            "customer",
            "income_source",
            "amount",
            "date_received",
        ]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            "id",
            "customer",
            "income_source",
            "amount",
            "date_received",
        ]

