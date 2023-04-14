from rest_framework import generics

from menu.models import (
    CategoryFood, Topping, Food
)

from menu.serializers import (
    CategoryFoodSerializer, 
    ToppingSerializer, 
    FoodSerializer,
)


class CategoryFoodListAPIView(generics.ListAPIView):
    queryset = CategoryFood.objects.filter(is_publish=True)
    serializer_class = CategoryFoodSerializer



class ToppingListAPIView(generics.ListAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer



class FoodListAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer       