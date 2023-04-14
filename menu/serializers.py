from rest_framework import serializers

from menu.models import (CategoryFood, Food, Topping)


class CategoryFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryFood
        fields = (
            'id',
            'name',
            'is_publish',
        )


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = (
            'id',
            'name',
        )


class FoodSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=CategoryFood.objects.all(),
        verbose_name='категория',
    )
    class Meta:
        model = Food
        fields = (
            'id',
            'category',
            'name',
            'description',
            'price',
            'is_special',
            'is_vegan',
            'toppings',
        )