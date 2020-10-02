from django.urls import path
from .views import recipes_list

urlpatterns = [
    path("", recipes_list),
]
