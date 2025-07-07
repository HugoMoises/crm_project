from django.urls import path
from .views import index, produto_list, create_produto, produto_update, produto_delete, produto_detail, estoque, vendas, create_venda,detail_venda

urlpatterns = [
    path('', index, name='index'),
    #Produtos
    path('produtos/', produto_list, name='produto_list'),
    path('produtos/create/', create_produto, name='create_produto'),
    path('produtos/update/<int:id>/', produto_update, name='produto_update'),
    path('produtos/delete/<int:id>/', produto_delete, name='produto_delete'),
    path('produtos/detail/<int:id>/', produto_detail, name='produto_detail'),
    
    #Vendas
    path('estoque/', estoque, name='estoque'),
    path('vendas/', vendas, name='vendas'),
    path('vendas/create/', create_venda, name='create_venda'),
    path('vendas/detail/<int:id>/', detail_venda, name='detail_venda'),
]