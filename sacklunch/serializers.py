
from sacklunch.order.models import Order
from rest_framework import routers, serializers, viewsets, permissions, generics

from django.contrib.auth.models import User
from sacklunch.order.models import Order
from sacklunch.entry.models import Entry
from sacklunch.item.models import *
from sacklunch.sandwich.models import *
from rest_framework.decorators import detail_route, list_route

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry

class ItemEntreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemEntree
        fields = ('description',)

class ItemDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDrink
        fields = ('description',)

class ItemSideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSide
        fields = ('description',)

class ItemFruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFruit
        fields = ('description',)


#Sandwich
class BreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = swBread
        fields = ('description',)

class MeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = swMeat
        fields = ('description',)

class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = swCheese
        fields = ('description',)

class SandwichSerializer(serializers.ModelSerializer):
    swbreadid = BreadSerializer()
    swmeatid = MeatSerializer()
    swcheeseid = CheeseSerializer()
    class Meta:
        model = Sandwich

#ORDER VIEW
# Serializers define the API representation.
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

class NestedOrderSerializer(serializers.ModelSerializer):
    entryid = EntrySerializer(many=False)
    itementreeid = ItemEntreeSerializer(many=False)
    itemdrinkid = ItemDrinkSerializer(many=False)
    itemsideid = ItemSideSerializer(many=False)
    itemfruitid = ItemFruitSerializer(many=False)
    sandwichid = SandwichSerializer(many=False)
    class Meta:
        model = Order        


# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class SandwichViewSet(viewsets.ModelViewSet):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer

class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



