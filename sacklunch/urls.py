#from django.conf.urls import patterns, include, url
from django.conf.urls import *
from django.contrib import admin
from sacklunch import views
admin.autodiscover()

#from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from sacklunch.order.models import Order
from sacklunch.entry.models import Entry
from sacklunch.item.models import *
from sacklunch.sandwich.models import *

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








# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.Home.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.Home.as_view(), name='home'),
    url(r'^order/', include('sacklunch.order.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^order/app/','order.views.hello'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
