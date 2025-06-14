from django.urls import path
from .views import index, produto_list, create_produto, estoque, vendas, create_venda, produto_update, produto_delete

urlpatterns = [
    path('', index, name='index'),
    #Produtos
    path('produtos/', produto_list, name='produto_list'),
    path('produtos/create/', create_produto, name='create_produto'),
    path('produtos/update/<int:id>/', produto_update, name='produto_update'),
    path('produtos/delete/<int:id>/', produto_delete, name='produto_delete'),
    #Vendas
    path('estoque/', estoque, name='estoque'),
    path('vendas/', vendas, name='vendas'),
    path('vendas/create/', create_venda, name='create_venda'),
]