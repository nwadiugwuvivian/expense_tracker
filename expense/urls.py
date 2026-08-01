from django.urls import path
from expense import views

urlpatterns = [
    path('register_expense/',views.register_expense),
    path('expense_list/',views.expense_list),
    path('expense_detail/<int:id>/',views.expense_detail),
    path('customer_expense/<int:id>/',views.customer_expense),
    path('customer_expense_by_first_name/<str:first_name>/',views.customer_expense_by_first_name),
    path('customer_expense_by_last_name/<str:last_name>/',views.customer_expense_by_last_name),
    path('update_expense/<int:id>/',views.update_expense),
    path('delete_expense/<int:id>/',views.delete_expense),
]