from apps.directory.models import CategoryType

def get_cats_by_type(type_id):
    return CategoryType.objects.filter(t_type_id=type_id)\
                        .values("category__id", "category__name")