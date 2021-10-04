from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    field_list_display = (
        'sku',
        'name',
        'description',
        'detail_01',
        'detail_02',
        'detail_03',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    field_list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
