from rest_framework import serializers
from .models import TransactionType,TransactionStatus,TransactionCategory,TransactionSubCategory, CategoryType, CategorySubCategory


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["id","name"]


class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = ["id","name"]


class TransactionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionCategory
        fields = ["id","name"]


class TransactionSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionSubCategory
        fields = ["id","name"]
    
class CategorySubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    sub_category_name = serializers.CharField(source="sub_category.name", read_only=True)

    class Meta:
        model = CategorySubCategory
        fields = ["id", "category", "sub_category", "category_name", "sub_category_name"]
    
class CategoryTypeSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    t_type_name = serializers.CharField(source="t_type.name", read_only=True)

    class Meta:
        model = CategoryType
        fields = ["id", "category", "t_type", "category_name", "t_type_name"]
    
