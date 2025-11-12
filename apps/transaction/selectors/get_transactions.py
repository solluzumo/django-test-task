from apps.transaction.models import Transaction

#Получить список всех транзакций
def get_transcations():
    return Transaction.objects.all()