from apps.directory.models import CategorySubCategory

def get_subs_by_cat(category_id):
    return CategorySubCategory.objects.filter(category_id=category_id)\
                        .values("sub_category__id", "sub_category__name")