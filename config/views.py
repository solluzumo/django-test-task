from django.shortcuts import render
from apps.directory.models import TransactionCategory,TransactionType, TransactionStatus
from apps.directory.serializers import TransactionCategorySerializer,TransactionTypeSerializer, TransactionStatusSerializer

def home(request):
    categories = TransactionCategorySerializer(TransactionCategory.objects.all(), many=True).data
    types = TransactionTypeSerializer(TransactionType.objects.all(), many=True).data
    statuses = TransactionStatusSerializer(TransactionStatus.objects.all(), many=True).data

    return render(request, "home.html",{"categories":categories,"types":types,"statuses":statuses})