from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_products, name='products'),
    path('<product_id>/', views.individual_product, name='individual_product'),
]
