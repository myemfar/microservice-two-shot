from django.urls import path
from .views import api_list_hats, api_hat_detail

urlpatterns = [
    path('hats/', api_list_hats, name='api_list_hats'),
    path('hats/<int:hat_id>/', api_hat_detail, name='api_hat_detail'),
]
