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
    render_directory_home,
    CategoryTypeView
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
    path("get-categories-by-type/<int:type_id>/", CategoryTypeView.as_view()),
    path("edit/",render_directory_home),
    path("", include(router.urls)),   
]