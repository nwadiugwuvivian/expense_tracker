from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .models import Customer
from .serializers import (CustomerRegisterSerializer,LoginSerializer,CustomerSerializer)

# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = CustomerRegisterSerializer(data=request.data)

    if serializer.is_valid():
        customer = serializer.save()
        return Response(
            {"message": "Customer created successfully",
             "customer": CustomerSerializer(customer).data
             },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    try:
        customer = Customer.objects.get(email=email)
    except Customer.DoesNotExist:
        return Response(
            {"message": "Customer does not exist"
             },
            status=status.HTTP_404_NOT_FOUND
        )

    if check_password(password, customer.password):
        return Response(
            {"message": "Login successful",
             "customer": CustomerSerializer(customer).data
             },
            status=status.HTTP_200_OK
        )

    return Response({"detail":"invalid credentials"}, status=status.HTTP_401_UNAUTHORIZE)


@api_view(['GET'])
def customers(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)



