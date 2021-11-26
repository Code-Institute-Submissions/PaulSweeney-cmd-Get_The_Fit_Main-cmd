from django.contrib import admin
from .models import Product, Category, Review, Blog


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_comment',
        'review_title',
    )


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_name',
        'blog_comment',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Blog, BlogAdmin)
