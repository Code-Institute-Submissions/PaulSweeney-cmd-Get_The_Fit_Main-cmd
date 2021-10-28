from django.contrib import admin
from .models import Product, Category, Review_product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
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
    list_display = (
        'friendly_name',
        'name',
    )


class Review_productAdmin(admin.ModelAdmin):
    list_display = (
        'review_comment',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review_product, Review_productAdmin)
