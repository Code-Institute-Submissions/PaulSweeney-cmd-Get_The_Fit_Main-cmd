from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_products, name='products'),
    path('<int:product_id>/', views.individual_product, name='individual_product'),
    path('add/<product_id>/', views.add_review, name='add_review'),
]
