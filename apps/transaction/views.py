from rest_framework.views import APIView
from .serializers import TransactionQuerySerializer, TransactionSerializer
from .models import Transaction
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .services.transaction_list import get_transaction_list

from apps.directory.models import(
    TransactionStatus,
    TransactionCategory,
    TransactionSubCategory,
    TransactionType,
)

class TransactionListView(APIView):

    #Получение отфильтрованного списка транзакций
    def post(self, request):
        validator = TransactionQuerySerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        data = validator.validated_data
        result = get_transaction_list(data)

        return Response(result)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
#Функция рендера для редактирования/создания формы
def transaction_form(request, id=None):
    
    #Если создаём транзакций
    transaction = None
    transaction_id = None

    #Если редактируем транзакцию
    if id:
        transaction = get_object_or_404(Transaction, id=id)
        transaction_id = transaction.id

    context = {
        "transaction": transaction,
        "statuses": TransactionStatus.objects.all(),
        "types": TransactionType.objects.all(),
        "categories": TransactionCategory.objects.all(),
        "sub_categories": TransactionSubCategory.objects.all(),
        "id":transaction_id,
    }

    return render(request, "transaction_form.html", context)
