from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('reference', 'title', 'description', 'bedrooms', 'bathrooms', 'price')
admin.site.register(Property, PropertyAdmin)


