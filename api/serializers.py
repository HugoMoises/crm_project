from rest_framework import serializers
from produtos.models import Produto, Venda, ItemVenda

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
        ordering = ['id']
    
class ItemVendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemVenda
        fields = [
            'id',
            'venda',
            'produto',
            'quantidade',
            'preco_unitario',
        ]
        ordering = ['id']

class VendaSerializer(serializers.ModelSerializer):
    itens = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='itemvenda-detail')
    class Meta:
        model = Venda
        fields = [
            'id',
            'data',
            'valor_total',
            'itens',
        ]
        ordering = ['id']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        venda = Venda.objects.create(**validated_data)
        for item_data in itens_data:
            ItemVenda.objects.create(venda=venda, **item_data)
        return venda
