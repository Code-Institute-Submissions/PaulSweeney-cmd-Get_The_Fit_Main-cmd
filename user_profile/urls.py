from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('previous_orders/<order_number>', views.previous_orders, name='previous_orders'),
]
