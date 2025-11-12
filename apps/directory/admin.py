from django.contrib import admin
from .models import (
    TransactionStatus, 
    TransactionCategory, 
    TransactionSubCategory, 
    TransactionType,
    CategoryType,
    CategorySubCategory
)

@admin.register(TransactionStatus)
class TransactionStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(TransactionCategory)
class TransactionCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(TransactionSubCategory)
class TransactionSubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)

@admin.register(CategorySubCategory)
class CategorySubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "sub_category")
    list_filter = ("category",)

@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "t_type")
    list_filter = ("category",)
