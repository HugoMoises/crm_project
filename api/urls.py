from django.urls import path    
from .views import ProdutosAPIView, ProdutoAPIView, VendasAPIView, VendaAPIView, ProdutoViewSet, VendaViewSet

from rest_framework.routers import SimpleRouter
router = SimpleRouter()
router.register('produtos', ProdutoViewSet)
router.register('vendas', VendaViewSet)

urlpatterns = [
    path('produtos/', ProdutosAPIView.as_view(), name='produtos-list-create'),
    path('produtos/<int:pk>', ProdutoAPIView.as_view(), name=f'produto {id}'),
    path('vendas/', VendasAPIView.as_view(), name='vendas-list-create'),
    path('vendas/<int:pk>/', VendaAPIView.as_view(), name='venda-detail'),
]
