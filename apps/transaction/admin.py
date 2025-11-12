from django.contrib import admin
from .models import Transaction
from rangefilter.filters import DateRangeFilter

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    # Поля, которые показываем в списке
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
    
    # По каким полям можно фильтровать
    list_filter = ("status", "t_type", "category", "sub_category", ('created_at', DateRangeFilter))
    
    # Сортировка по умолчанию
    ordering = ("-created_at",)
    
    # Оптимизация ForeignKey (чтобы не было лишних SQL-запросов)
    list_select_related = ("status", "t_type", "category", "sub_category")
    
    # Разделение полей при редактировании
    fieldsets = (
        ("Общие данные", {
            "fields": ("created_at", "money", "comment")
        }),
        ("Связанные объекты", {
            "fields": ("status", "t_type", "category", "sub_category")
        }),
    )
