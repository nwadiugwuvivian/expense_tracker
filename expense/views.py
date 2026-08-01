from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import CreateExpenseSerializer, ExpenseSerializer


# Create your views here.
@api_view(['POST'])
def register_expense(request):
    serializer = CreateExpenseSerializer(data=request.data)

    if serializer.is_valid():
        expense = serializer.save()
        return Response({
            "message":"expense created",
            "expense":ExpenseSerializer(expense).data
        },
        status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def expense_list(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def expense_detail(request, id):
    expense = Expense.objects.get(id=id)
    serializer = ExpenseSerializer(expense)
    return Response(serializer.data)


@api_view(['GET'])
def customer_expense(request, id):
    expense = Expense.objects.filter(customer__id=id)
    serializer = ExpenseSerializer(expense,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def  customer_expense_by_first_name(request, first_name):
    expense = Expense.objects.filter(customer__first_name=first_name)
    serializer = ExpenseSerializer(expense,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customer_expense_by_last_name(request, last_name):
    expense = Expense.objects.filter(customer__last_name=last_name)
    serializer = ExpenseSerializer(expense,many=True)
    return Response(serializer.data)



@api_view(['PATCH'])
def update_expense(request, id):
    expense = Expense.objects.get(id=id)
    serializer = ExpenseSerializer(expense, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

        return Response({"message":"expense updated successfully",
                          "expense":serializer.data
                          },
                         status=status.HTTP_200_OK
                         )
    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )

@api_view(['DELETE'])
def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    expense.delete()
    return Response({"message":"expense deleted successfully",
                     },
                    status = status.HTTP_204_NO_CONTENT
                    )



