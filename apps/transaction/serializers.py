from rest_framework import serializers
from .models import Transaction,TransactionCategory,TransactionSubCategory,TransactionStatus,TransactionType

class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)
    status_name = serializers.CharField(source="status.name", read_only=True)
    t_type_name = serializers.CharField(source="t_type.name", read_only=True)
    sub_category_name = serializers.CharField(source="sub_category.name", read_only=True)

    category = serializers.PrimaryKeyRelatedField(queryset=TransactionCategory.objects.all(), write_only=True)
    sub_category = serializers.PrimaryKeyRelatedField(queryset=TransactionSubCategory.objects.all(), write_only=True)
    status = serializers.PrimaryKeyRelatedField(queryset=TransactionStatus.objects.all(), write_only=True)
    t_type = serializers.PrimaryKeyRelatedField(queryset=TransactionType.objects.all(), write_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "created_at",
            "money",
            "comment",

            # поля только для чтения с именем
            "category_name",
            "status_name",
            "t_type_name",
            "sub_category_name",

            # поля для записи id
            "category",
            "sub_category",
            "status",
            "t_type",
        ]



class TransactionQuerySerializer(serializers.Serializer):
    filters = serializers.DictField(required=False)
    order_by = serializers.ListField(
        child=serializers.CharField(), required=False
    )

    def validate_order_by(self, value):
        allowed_order_fields = ["created_at", "money", "category", "status"]

        for field in value:
            field_name = field.lstrip("-")
            if field_name not in allowed_order_fields:
                raise serializers.ValidationError(f"Invalid order field: {field}")

        return value