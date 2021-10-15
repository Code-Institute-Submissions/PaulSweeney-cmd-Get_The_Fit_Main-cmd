from django.urls import path
from . import views


urlpatterns = [
    path('', views.bag, name='bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
    path('update/<item_id>', views.update_bag, name='update_bag'),
    path('delete/<item_id>', views.delete_item, name='delete_item'),
]
