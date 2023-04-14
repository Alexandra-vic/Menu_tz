from django.contrib import admin

from menu.models import CategoryFood, Topping, Food


@admin.register(CategoryFood)
class CategoryFoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_publish',
    )

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'name',
        'description',
        'price',
        'is_special',
        'is_vegan',
    )
    filter_horizontal = ('toppings', )
