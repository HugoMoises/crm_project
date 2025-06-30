from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data = models.DateTimeField(auto_now_add=True)

    def valor_total(self):
        return sum(item.preco_unitario * item.quantidade for item in self.itens.all())
    
    def __str__(self):
        return f"Venda {self.id} - {self.data.strftime('%d/%m/%Y %H:%M:%S')} - {self.valor_total()}"


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=15, decimal_places=2)