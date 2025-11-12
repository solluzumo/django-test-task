from rest_framework.views import APIView
from .serializers import TransactionQuerySerializer, TransactionSerializer
from .models import Transaction
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404

from apps.directory.models import(
    TransactionStatus,
    TransactionCategory,
    TransactionSubCategory,
    TransactionType,
)

class TransactionListView(APIView):

    #Получение списка
    def post(self, request):
        validator = TransactionQuerySerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        data = validator.validated_data

        queryset = Transaction.objects.all()
        filters = data.get("filters", {})

        # Маппинг фильтров запроса на поля модели
        related_filters = {
            "category": "category__name__icontains",
            "status": "status__name__icontains",
            "t_type": "t_type__name__icontains",
            "sub_category": "sub_category__name__icontains",
        }

        applied_filters = {}

        for key, value in filters.items():
            if key in related_filters:
                applied_filters[related_filters[key]] = value
            else:
                applied_filters[key] = value

        if applied_filters:
            queryset = queryset.filter(**applied_filters)

        order_by = data.get("order_by", [])
        if order_by:
            queryset = queryset.order_by(*order_by)

        result = TransactionSerializer(queryset, many=True).data
        return Response(result)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    

def transaction_form(request, id=None):
    transaction = None
    if id:
        transaction = get_object_or_404(Transaction, id=id)

    context = {
        "transaction": transaction,
        "statuses": TransactionStatus.objects.all(),
        "types": TransactionType.objects.all(),
        "categories": TransactionCategory.objects.all(),
        "sub_categories": TransactionSubCategory.objects.all(),
        "id":transaction.id,
    }
    return render(request, "transaction_form.html", context)
