from rest_framework import serializers
from .models import TransactionType,TransactionStatus,TransactionCategory,TransactionSubCategory, CategoryType, CategorySubCategory


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["name"]


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ["name"]


class TransactionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ["name"]


class TransactionSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSubCategory
        fields = ["name"]
    
class CategorySubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorySubCategory
        fields = ["sub_category","category"]
    
class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ["category","t_type"]
    
