from django.urls import path
from .views import index, produto_list, create_produto, estoque

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produto_list, name='produto_list'),
    path('produtos/create/', create_produto, name='create_produto'),
    path('estoque/', estoque, name='estoque'),
]