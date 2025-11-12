from django.contrib import admin
from .models import Transaction
from rangefilter.filters import DateRangeFilter

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "status",
        "t_type",
        "category",
        "sub_category",
        "money",
        "comment",
    )
    
    list_filter = ("status", "t_type", "category", "sub_category", ('created_at', DateRangeFilter))
    
    ordering = ("-created_at",)
    
    list_select_related = ("status", "t_type", "category", "sub_category")
    
    fieldsets = (
        ("Общие данные", {
            "fields": ("created_at", "money", "comment")
        }),
        ("Связанные объекты", {
            "fields": ("status", "t_type", "category", "sub_category")
        }),
    )
