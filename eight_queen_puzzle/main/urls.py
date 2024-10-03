from django.urls import path
from .views import index, solve_view

urlpatterns = [
    path('', index, name='index'),
    path('solve/', solve_view, name='solve'),
]
