from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def valor_total(self):
        valor_total = self.quantidade * self.produto.preco
        return valor_total

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} - {self.data.strftime('%Y-%m-%d %H:%M:%S')}"