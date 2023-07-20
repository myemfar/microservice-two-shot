from django.urls import path
from .views import (api_detail_shoes, api_list_shoes)

urlpatterns = [
    path("shoes/", api_list_shoes, name="api_detail_shoe"),
    path("shoes/<int:pk>/", api_detail_shoes, name="api_detail_shoe"),
]
