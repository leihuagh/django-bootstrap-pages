from django.urls import path
from .views import index, list_view, detail_view

app_name = 'blog'
urlpatterns = [
    path('', index, name='index'),
    path('list', list_view, name='list'),
    path('detail', detail_view, name='detail'),
]
