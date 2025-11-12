from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from django.shortcuts import render
from .services.cat_sub_cat_link import link_cat_to_sub, update_category_subcategory
from .services.cat_type_link import update_category_type,link_cat_to_type
from .selectors.cat_sub_cat_link import get_subs_by_cat
from .selectors.cat_type_link import get_cats_by_type

from .models import(
    TransactionStatus,
    TransactionCategory,
    TransactionSubCategory,
    TransactionType,
    CategoryType,
    CategorySubCategory
)

from .serializers import (
    TransactionStatusSerializer,
    TransactionCategorySerializer,
    TransactionSubCategorySerializer,
    TransactionTypeSerializer,
    CategoryTypeSerializer,
    CategorySubCategorySerializer
)

class DirectoryView(APIView):
    
    #Получение списка всех статусов, категорий, подкатегорий, типов и связей между ними
    def get(self, request):
        statuses = TransactionStatusSerializer(TransactionStatus.objects.all(), many=True).data
        categories = TransactionCategorySerializer(TransactionCategory.objects.all(), many=True).data
        subCategories = TransactionSubCategorySerializer(TransactionSubCategory.objects.all(), many=True).data
        types = TransactionTypeSerializer(TransactionType.objects.all(), many=True).data
        catSubLinksRaw = CategorySubCategorySerializer(CategorySubCategory.objects.all(), many=True).data
        catTypeLinksRaw = CategoryTypeSerializer(CategoryType.objects.all(), many=True).data
       
        catSubLinks = []
        for item in catSubLinksRaw:
            catSubLinks.append({
                "id": item["id"],
                "category": item["category_name"],  
                "sub_category": item["sub_category_name"] 
            })

        catTypeLinks = []
        for item in catTypeLinksRaw:
            catTypeLinks.append({
                "id": item["id"],
                "category": item["category_name"], 
                "t_type": item["t_type_name"]         
            })

        return Response({
            "statuses": statuses,
            "categories": categories,
            "sub_categories": subCategories,
            "types": types,
            "cat_sub_links": catSubLinks,
            "cat_type_links": catTypeLinks,
        })


class CategoryTypeView(APIView):
    #Получение списка категорий определенного типа по id
    def get(self, request, type_id):

        categories = get_cats_by_type(type_id)

        return Response(list(categories))
    

class SubCategoriesByCategoryView(APIView):
    #Получение списка подкатегорий определенной категории по id
    def get(self, request, category_id):
        subcategories = get_subs_by_cat(category_id)

        return Response(list(subcategories))
    
#----------VIEWSETS----------
    
class CategorySubCategoryViewSet(viewsets.ModelViewSet):
    queryset = CategorySubCategory.objects.all()
    serializer_class = CategorySubCategorySerializer
    #Создание связки категория-подкатегория
    def create(self, request, *args, **kwargs):

        #Парсим запрос
        subCategory = request.data.get("sub_category", "")
        category = request.data.get("category", "")

        obj = link_cat_to_sub(category, subCategory)   

        return Response(CategorySubCategorySerializer(obj).data, status=status.HTTP_201_CREATED)
    
    #Обновление связки категория-подкатегория
    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        updated_instance = update_category_subcategory(
            instance,
            request.data.get("category", ""),
            request.data.get("sub_category", "")
        )

        serializer = self.get_serializer(updated_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer
    #Создание связки категория-тип
    def create(self, request, *args, **kwargs):

        #Парсим запрос
        t_type = request.data.get("t_type", "")
        category = request.data.get("category", "")

        obj = link_cat_to_type(category, t_type)   

        return Response(CategoryTypeSerializer(obj).data, status=status.HTTP_201_CREATED)
    #Обновление связки категория-тип
    def update(self, request, *args, **kwargs):

        instance = self.get_object()

        updated_instance = update_category_type(
            instance,
            request.data.get("category", ""),
            request.data.get("t_type", "")
        )

        serializer = self.get_serializer(updated_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TransactionStatusViewSet(viewsets.ModelViewSet):
    queryset = TransactionStatus.objects.all()
    serializer_class = TransactionStatusSerializer


class TransactionCategoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionCategory.objects.all()
    serializer_class = TransactionCategorySerializer


class TransactionSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = TransactionSubCategory.objects.all()
    serializer_class = TransactionSubCategorySerializer

class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer

#Рендер странцы редактирования статусов, категорий, подкатегорий, типов и связей между ними
def render_directory_home(request):
    return render(request, "directory.html")
