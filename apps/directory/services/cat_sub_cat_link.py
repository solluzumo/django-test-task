from apps.directory.models import TransactionCategory, TransactionSubCategory, CategorySubCategory
from rest_framework.exceptions import ValidationError

#Привязывае подкатегорию к категории по названиям
def link_cat_to_sub(category:str, subCategory:str):    
        
    #Проверяем существуют ли объекты перед связкой
    catObj = TransactionCategory.objects.filter(name=category).first()
    
    subCatObj = TransactionSubCategory.objects.filter(name=subCategory).first()

    if not catObj or not subCatObj:

        raise ValidationError("Категория или подкатегория не найдена")
    
    #Проверяем на дубликат
    already_exists = CategorySubCategory.objects.filter(category=catObj.id,sub_category=subCatObj.id)
    
    if already_exists:

        raise ValidationError("Такая связка уже существует")
    
    return CategorySubCategory.objects.create(category=catObj, sub_category=subCatObj)

#Обновляем связь категори-подкатегория
def update_category_subcategory(instance, category_name: str, subcategory_name: str):

    #Проверяем существование перед обновлением
    category = TransactionCategory.objects.filter(name=category_name.strip()).first()    
    subcategory = TransactionSubCategory.objects.filter(name=subcategory_name.strip()).first()

    if not category or not subcategory:
        raise ValidationError("такой категории или подкатегории не существует")

    # Проверка дубликата (кроме текущего)
    if CategorySubCategory.objects.filter(
            category=category,
            sub_category=subcategory
    ).exclude(id=instance.id).exists():
        raise ValidationError("такая связка уже существует")

    instance.category = category
    
    instance.sub_category = subcategory

    instance.save()

    return instance
