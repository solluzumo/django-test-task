from apps.directory.models import CategoryType

#Возвращаем категории для определенного типа по id
def get_cats_by_type(type_id):
    return CategoryType.objects.filter(t_type_id=type_id)\
                        .values("category__id", "category__name")