from apps.transaction.models import Transaction
from apps.transaction.serializers import TransactionSerializer

def get_transaction_list(data):
    
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

        return TransactionSerializer(queryset, many=True).data