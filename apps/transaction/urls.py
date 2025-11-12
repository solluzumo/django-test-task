from rest_framework.routers import DefaultRouter
from .views import TransactionListView, TransactionViewSet
from django.urls import path, include
from .views import transaction_form

router = DefaultRouter()

router.register(r"detail", TransactionViewSet, basename="transaction")

urlpatterns = [
    path("list/", TransactionListView.as_view(), name="transaction-list"),
    path("", include(router.urls)),  
    path("edit/<int:id>/", transaction_form),
    path("create/", transaction_form),
]