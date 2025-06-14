from django.shortcuts import render
from .forms import ProdutoForm, ProdutoVenda
from .models import Produto, Venda

def index(request):
    return render(request, 'produtos/index.html')

def produto_list(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutoForm()

    context = {
        'produtos': produtos,
        'form': form
    }
    return render(request, 'produtos/produtos_list.html', context)

def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProdutoForm()
    context = {
        'form': form
    }
    return render(request, 'produtos/produtos_create.html', context)

def estoque(request):
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    if request.method == 'POST':
        form = ProdutoVenda(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            produto = venda.produto
            produto.estoque -= venda.quantidade
            produto.save()
            venda.save()
    else:
        form = ProdutoVenda()
    context = {
        'produtos': produtos,
        'vendas': vendas,
        'form': form
    }
    return render(request, 'produtos/estoque.html', context)