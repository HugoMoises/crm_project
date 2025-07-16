from rest_framework import generics
from rest_framework.generics import get_object_or_404
from produtos.models import Produto, Venda, ItemVenda
from .serializers import ProdutoSerializer, VendaSerializer, ItemVendaSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# v1 da API: Estou usando generic views
class ProdutosAPIView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendasAPIView(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaAPIView(generics.RetrieveAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


#v2 da API usando viewsets

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class VendaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    @action(detail=True, methods=['get'])
    def itens(self, request, pk=None):
        venda = self.get_object()   
        itens = venda.itens.all()
        serializer = ItemVendaSerializer(itens, many=True)
        return Response(serializer.data)