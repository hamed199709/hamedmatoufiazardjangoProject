from django.contrib import admin
from .models import Car,Driver,Brand,Representation

class CarAdmin(admin.ModelAdmin):
    list_display = ['name','color','price','photo']
    list_editable = ['price']
    list_filter = ['name', 'price', 'color']
    prepopulated_fields = {'slug': ['name', 'color']}

class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

class RepresentationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}

class DriverAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}



admin.site.register(Car,CarAdmin)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Driver,DriverAdmin)
admin.site.register(Representation,RepresentationAdmin)


