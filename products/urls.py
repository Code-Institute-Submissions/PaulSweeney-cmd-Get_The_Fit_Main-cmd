from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_products, name='site_products')
]
