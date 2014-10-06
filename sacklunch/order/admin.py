from django.contrib import admin
from models import Order, OrderItems


class OrderItemsTabular(admin.TabularInline):
	model=OrderItems
	extra=1

class OrderItemAdmin(admin.ModelAdmin):
	# fields = ['description', 'itemtypeid']
	inlines=[OrderItemsTabular]

# Register your models here.
admin.site.register(Order, OrderItemAdmin)
# admin.site.register(OrderItems)
