from django.contrib import admin
from .models import Location, House

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Location,LocationAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'address', 'created', 'update']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10
admin.site.register(House,HouseAdmin)



