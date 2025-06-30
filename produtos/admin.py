from django.contrib import admin
from .models import Produto, Venda

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)
    list_filter = ('estoque',)

class VendaAdmin(admin.ModelAdmin):
    list_display = ('data', 'valor_total')
    search_fields = ('data',)
    list_filter = ('data',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)  