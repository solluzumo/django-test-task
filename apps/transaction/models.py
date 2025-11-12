from django.db import models
from apps.directory.models import TransactionType,TransactionStatus,TransactionCategory,TransactionSubCategory
from datetime import date
from config import settings

#Транзакция - ДДС
class Transaction(models.Model):
    
    created_at = models.DateField(default=date.today, verbose_name="Дата")

    status = models.ForeignKey(TransactionStatus, on_delete=models.PROTECT, verbose_name="Статус")

    t_type = models.ForeignKey(TransactionType, on_delete=models.PROTECT, verbose_name="Тип")

    category = models.ForeignKey(TransactionCategory, on_delete=models.PROTECT, blank=False, verbose_name="Категория")

    sub_category = models.ForeignKey(TransactionSubCategory, on_delete=models.PROTECT, blank=False, verbose_name="Подкатегория")

    money = models.IntegerField(default=0, blank=False, verbose_name="Сумма")

    comment = models.TextField(default=None, verbose_name="Комментарий",blank=True)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"