from django.db import models


class TransactionType(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
    

class TransactionStatus(models.Model):

    name = models.CharField(max_length=50, unique=True, verbose_name="Название")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class TransactionCategory(models.Model):

    name = models.CharField(max_length=50, verbose_name="Название")

    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"  

class TransactionSubCategory(models.Model):

    name = models.CharField(max_length=50, verbose_name="Название")
    
    def __str__(self):        
        return self.name
      
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
   
#Связь категория-тип 
class CategoryType(models.Model):

    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE, verbose_name="Категория")
   
    t_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, verbose_name="Тип")

    class Meta:

        verbose_name = "Связь категория-тип"

        verbose_name_plural = "Связи категория-тип"

        unique_together = ('category','t_type')

#Связь категория-подкатегория
class CategorySubCategory(models.Model):
    
    sub_category = models.ForeignKey(TransactionSubCategory, on_delete=models.CASCADE, verbose_name="Подкатегория")
    
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE, verbose_name="Категория")

        
    class Meta:
       
        verbose_name = "Связь категория-подкатегория"

        verbose_name_plural = "Связи категория-подкатегория"
        
        unique_together = ('sub_category','category')

