from django.urls import path
from income import views

urlpatterns = [
    path('income_register/',views.income_register),
    path('income_list/',views.income_list),
    path('income_detail/<int:id>/',views.income_detail),
    path('customer_income/<int:id>/',views.customer_income),
    path('customer_income_by_first_name/<str:first_name>/',views.customer_income_by_first_name),
    path('customer_income_by_last_name/<str:last_name>/',views.customer_income_by_last_name),
    path('income_update/<int:id>/',views.income_update),
    path('income_delete/<int:id>/',views.income_delete),
]