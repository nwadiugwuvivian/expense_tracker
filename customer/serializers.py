from rest_framework import serializers
from .models import Customer
from django.contrib.auth.hashers import make_password
from .validators import validate_password, validate_phone_number

class CustomerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )
    phone_number = serializers.CharField(
        validators=[validate_phone_number]
    )
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password",
        ]

    def create(self, validated_data):

         validated_data["password"] = make_password(
             validated_data["password"]
         )

         customer = Customer.objects.create(**validated_data)

         return customer

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = Customer
        fields = [
            "email",
            "password"
        ]



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]

