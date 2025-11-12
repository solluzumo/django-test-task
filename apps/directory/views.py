from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from django.shortcuts import render

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

    def get(self, request):
        statuses = list(TransactionStatus.objects.values("id", "name"))
        categories = list(TransactionCategory.objects.values("id", "name"))
        subCategories = list(TransactionSubCategory.objects.values("id", "name"))
        types = list(TransactionType.objects.values("id", "name"))

        catSubLinksRaw = CategorySubCategory.objects.values("id", "sub_category__name", "category__name")
        catSubLinks = []
        for item in catSubLinksRaw:
            catSubLinks.append({
                "id": item["id"],
                "category": item["category__name"],  
                "sub_category": item["sub_category__name"] 
            })

        # Связи категория-тип
        catTypeLinksRaw = CategoryType.objects.values("id", "category__name", "t_type__name")
        catTypeLinks = []
        for item in catTypeLinksRaw:
            catTypeLinks.append({
                "id": item["id"],
                "category": item["category__name"], 
                "t_type": item["t_type__name"]         
            })

        return Response({
            "statuses": statuses,
            "categories": categories,
            "sub_categories": subCategories,
            "types": types,
            "cat_sub_links": catSubLinks,
            "cat_type_links": catTypeLinks,
        })


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


class CategorySubCategoryViewSet(viewsets.ModelViewSet):
    queryset = CategorySubCategory.objects.all()
    serializer_class = CategorySubCategorySerializer

    def create(self, request, *args, **kwargs):

        #Парсим запрос
        subCategory = request.data.get("sub_category", "")
        category = request.data.get("category", "")

        if (subCategory =="" or category==""):
            return Response({
                "error":"неверный формат запроса"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        subCategory = subCategory.strip()
        category = category.strip()

        #Проверяем существуют ли объекты перед связкой
        catObj = TransactionCategory.objects.filter(name=category).first()
        subCatObj = TransactionSubCategory.objects.filter(name=subCategory).first()

        if not catObj or not subCatObj:
            return Response({
                "error":"такой категории или подкатегории не существует"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        #Проверяем на дубликат
        already_exists = CategorySubCategory.objects.filter(category=catObj.id,sub_category=subCatObj.id)
        if already_exists:
            return Response({
                "error":"такая связка уже существует"
            },
            status=status.HTTP_400_BAD_REQUEST
            )
        
        #Сериализуем и сохраняем в бд
        serializer = self.get_serializer(data={
            "sub_category":subCatObj.id,
            "category":catObj.id
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object() 
        obj_id = request.data.get("id") 
        if not obj_id or int(obj_id) != instance.id:
            return Response({"error": "ID в JSON не совпадает с ID в URL"},
                            status=status.HTTP_400_BAD_REQUEST)
        category_name = request.data.get("category", "").strip()
        subCategory_name = request.data.get("sub_category", "").strip()

        if not category_name or not subCategory_name:
            return Response({"error": "неверный формат запроса"}, status=status.HTTP_400_BAD_REQUEST)
        
        catObj = TransactionCategory.objects.filter(name=category_name).first()
        subCatObj = TransactionSubCategory.objects.filter(name=subCategory_name).first()
              
        if not catObj or not subCatObj:
            return Response({"error": "такой категории или подкатегории не существует"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # Проверка на дубликат (кроме текущего объекта)
        if CategorySubCategory.objects.filter(category=catObj.id, sub_category=subCatObj.id).exclude(id=instance.id).exists():
            return Response({"error": "такая связка уже существует"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Сохраняем обновление
        serializer = self.get_serializer(instance, data={"category": catObj.id, "sub_category": subCatObj.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CategoryTypeViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer

    def create(self, request, *args, **kwargs):

        #Парсим запрос
        tType = request.data.get("t_type", "")
        category = request.data.get("category", "")

        if (tType =="" or category==""):
            return Response({
                "error":"неверный формат запроса"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        tType = tType.strip()
        category = category.strip()

        #Проверяем существуют ли объекты перед связкой
        catObj = TransactionCategory.objects.filter(name=category).first()
        tTypeObj = TransactionType.objects.filter(name=tType).first()

        if not catObj or not tTypeObj:
            return Response({
                "error":"такой категории или типа не существует"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        #Проверяем на дубликат
        already_exists = CategoryType.objects.filter(category=catObj.id,t_type=tTypeObj.id)
        if already_exists:
            return Response({
                "error":"такая связка уже существует"
            },
            status=status.HTTP_400_BAD_REQUEST
            )

        #Сериализуем и сохраняем в бд
        serializer = self.get_serializer(data={
            "category":catObj.id,
            "t_type":tTypeObj.id
        })

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):

        instance = self.get_object() 
        obj_id = request.data.get("id") 

        if not obj_id or int(obj_id) != instance.id:
            return Response({"error": "ID в JSON не совпадает с ID в URL"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        category_name = request.data.get("category", "").strip()
        tType_name = request.data.get("t_type", "").strip()

        if not category_name or not tType_name:
            return Response({"error": "неверный формат запроса"}, status=status.HTTP_400_BAD_REQUEST)
        
        catObj = TransactionCategory.objects.filter(name=category_name).first()
        tTypeObj = TransactionType.objects.filter(name=tType_name).first()
              
        if not catObj or not catObj:
            return Response({"error": "такой категории или типа не существует"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        if CategoryType.objects.filter(category=catObj.id, t_type=tTypeObj.id).exclude(id=instance.id).exists():
            return Response({"error": "такая связка уже существует"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Сохраняем обновление
        serializer = self.get_serializer(instance, data={"category": catObj.id, "t_type": tTypeObj.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class SubCategoriesByCategoryView(APIView):
    def get(self, request, category_id):
        subcategories = CategorySubCategory.objects.filter(category_id=category_id)\
                        .values("sub_category__id", "sub_category__name")

        return Response(list(subcategories))
    

def directories(request):
    return render(request, "directory.html")

def directories_form(request):
    return render(request, "directory_form.html")
