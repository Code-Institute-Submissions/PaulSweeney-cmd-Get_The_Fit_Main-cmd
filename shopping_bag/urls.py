from django.urls import path
from . import views


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
]
