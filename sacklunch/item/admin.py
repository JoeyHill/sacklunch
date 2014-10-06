from django.contrib import admin
from models import Item, SubItem, ItemType
# Register your models here.
class SubItemTabular(admin.TabularInline):
	model=SubItem
	extra=1

class ItemAdmin(admin.ModelAdmin):
	fields = ['description', 'itemtypeid']
	inlines=[SubItemTabular]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemType)