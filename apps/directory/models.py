from django.db import models


class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class TransactionStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class TransactionCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name    

class TransactionSubCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name   
   
#Сущности связки   
class CategoryType(models.Model):
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    t_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE)

    def __str__(self):
        return (self.category.name,self.t_type.name)
        
    class Meta:
        unique_together = ('category','t_type')


class CategorySubCategory(models.Model):
    sub_category = models.ForeignKey(TransactionSubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return (self.category.name,self.sub_category.name)

    class Meta:
        unique_together = ('sub_category','category')

