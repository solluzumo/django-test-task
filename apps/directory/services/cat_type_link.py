from apps.directory.models import(
    TransactionStatus,
    TransactionCategory,
    TransactionSubCategory,
    TransactionType,
    CategoryType,
    CategorySubCategory
)
from rest_framework.exceptions import ValidationError

#Привязываем категорию к типу
def link_cat_to_type(category:str, tType:str):    
        
    #Проверяем существуют ли объекты перед связкой
    catObj = TransactionCategory.objects.filter(name=category).first()
    tTypeObj = TransactionType.objects.filter(name=tType).first()

    if not catObj or not tTypeObj:
        raise ValidationError("такой категории или типа не существует")

    #Проверяем на дубликат
    already_exists = CategoryType.objects.filter(category=catObj.id,t_type=tTypeObj.id)
    if already_exists:
        raise ValidationError("такая связка уже существует")       

    
    return CategoryType.objects.create(category=catObj, t_type=tTypeObj)

#Обновляем связь категория-тип
def update_category_type(instance, category_name: str, t_type_name: str):

    category = TransactionCategory.objects.filter(name=category_name.strip()).first()
    t_type = TransactionType.objects.filter(name=t_type_name.strip()).first()

    if not category or not t_type:
        raise ValidationError("такой категории или типа не существует")

    # Проверка дубликата (кроме текущего)
    if CategoryType.objects.filter(
            category=category,
            t_type=t_type
    ).exclude(id=instance.id).exists():
        raise ValidationError("такая связка уже существует")

    instance.category = category
    instance.t_type = t_type
    instance.save()

    return instance
