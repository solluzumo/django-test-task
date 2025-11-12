from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    DirectoryView,
    TransactionStatusViewSet,
    TransactionCategoryViewSet,
    TransactionSubCategoryViewSet,
    TransactionTypeViewSet,
    CategorySubCategoryViewSet,
    CategoryTypeViewSet, 
    DirectoryView, 
    SubCategoriesByCategoryView,
    directories
)

router = DefaultRouter()
router.register(r"statuses", TransactionStatusViewSet, basename="statuses")
router.register(r"categories", TransactionCategoryViewSet, basename="categories")
router.register(r"subcategories", TransactionSubCategoryViewSet, basename="subcategories")
router.register(r"types", TransactionTypeViewSet, basename="types")
router.register(r"category_sub_links", CategorySubCategoryViewSet, basename="category_sub_links")
router.register(r"category_type_links", CategoryTypeViewSet, basename="category_type_links")

urlpatterns = [
    path("list/", DirectoryView.as_view(), name="directory-list"),
    path("get-subcategories/<int:category_id>/", SubCategoriesByCategoryView.as_view()),
    path("edit/",directories),
    path("", include(router.urls)),   
]