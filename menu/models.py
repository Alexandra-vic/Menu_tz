from django.db import models


class CategoryFood(models.Model):
    name = models.CharField(
        max_length=75, 
        verbose_name='название',
    )
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Topping(models.Model):
    name = models.CharField(
        max_length=75, 
        verbose_name='название',
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'topping'
        verbose_name_plural = 'toppings'


class Food(models.Model):
    category = models.ForeignKey(
        CategoryFood, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='foods',
        verbose_name='категория',
    )
    name = models.CharField(
        max_length=75, verbose_name='название'
    )
    description = models.TextField(verbose_name='описание')
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='цена',
    )
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    toppings = models.ManyToManyField(
        Topping, 
        related_name='foods',
        verbose_name='ингредиенты'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'food'
        verbose_name_plural = 'foods'