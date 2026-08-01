from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import CreateIncomeSerializer, IncomeSerializer


# Create your views here.
@api_view(['POST'])
def income_register(request):
    serializer = CreateIncomeSerializer(data=request.data)

    if serializer.is_valid():
        income = serializer.save()
        return Response({
            "message": "Income successfully registered",
            "income": IncomeSerializer(income).data
        },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def income_list(request):
    incomes = Income.objects.all()
    serializer = IncomeSerializer(incomes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def income_detail(request, id):
    income = Income.objects.get(id=id)
    serializer = IncomeSerializer(income)
    return Response(serializer.data)

@api_view(['GET'])
def customer_income(request, id):
    income = Income.objects.filter(customer__id=id)
    serializer = IncomeSerializer(income, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer_income_by_first_name(request, first_name):
    income = Income.objects.filter(customer__first_name=first_name)
    serializer = IncomeSerializer(income, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer_income_by_last_name(request, last_name):
    income = Income.objects.filter(customer__last_name=last_name)
    serializer = IncomeSerializer(income, many=True)
    return Response(serializer.data)



@api_view(['PATCH'])
def income_update(request, id):
    income = Income.objects.get(id=id)
    serializer = IncomeSerializer(income, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({"message":"income updated successfully","income":serializer.data
                         },
                        status=status.HTTP_200_OK
                        )
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )


@api_view(['DELETE'])
def income_delete(request, id):
    income = Income.objects.get(id=id)
    income.delete()
    return Response({"message":"income deleted succesfully"
                     },
                    status =status.HTTP_204_NO_CONTENT
                    )
