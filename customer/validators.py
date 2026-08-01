import re
from rest_framework import serializers

def validate_password(password):
    if len(password) < 8:
        raise serializers.ValidationError(
            "Password must be at least 8 characters long"
        )
    if not re.search(r"[a-z]", password):
        raise serializers.ValidationError(
            "Password must contain at least one lowercase letter "
        )
    if not re.search(r"[A-Z]", password):
        raise serializers.ValidationError(
            "Password must contain at least one uppercase letter "
        )
    if not re.search(r"\d", password):
        raise serializers.ValidationError(
            "Password must contain at least one number"
        )
    return password

def validate_phone_number(phone_number):
    if not phone_number.isdigit():
        raise serializers.ValidationError(
            "Phone number must contain only digits"
        )

    if len(phone_number) != 11:
        raise serializers.ValidationError(
            "Phone number must be 11 digits"
        )
    return phone_number


