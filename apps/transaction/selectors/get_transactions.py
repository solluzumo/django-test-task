from apps.transaction.models import Transaction

def get_transcations():
    return Transaction.objects.all()