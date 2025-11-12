from apps.directory.models import CategorySubCategory

#Возвращаем подкатегории для определенной категории по id
def get_subs_by_cat(category_id):
    return CategorySubCategory.objects.filter(category_id=category_id)\
                        .values("sub_category__id", "sub_category__name")