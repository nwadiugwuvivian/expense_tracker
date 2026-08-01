from dashboard import views
from django.urls import path

urlpatterns = [
    path('customer_dashboard/<int:id>/', views.customer_dashboard),
]