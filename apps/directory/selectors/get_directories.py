from apps.directory.models import TransactionType, TransactionStatus, TransactionCategory, TransactionSubCategory


def get_transactions_statuses():
    return TransactionStatus.objects.all()

def get_transactions_types():
    return TransactionType.objects.all()

def get_transactions_categorys():
    return TransactionCategory.objects.all()

def get_transactions_sub_categorys():
    return TransactionSubCategory.objects.all()