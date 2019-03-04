from django.urls import path
from .views import index, list_view

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('list', list_view, name='list'),
]
