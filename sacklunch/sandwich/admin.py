from django.contrib import admin
from models import *

# Register your models here.
# admin.site.register(Sandwich)
admin.site.register(swBread)
admin.site.register(swMeat)
admin.site.register(swCheese)

admin.site.register(Topping)

class ToppingInline(admin.TabularInline):
	model=SandwichTopping
	extra=1
class SandwichToppingAdmin(admin.ModelAdmin):
	inlines = [ToppingInline]
admin.site.register(Sandwich, SandwichToppingAdmin)
#admin.site.register(SandwichTopping)