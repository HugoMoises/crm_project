from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm, ProdutoVenda
from .models import Produto, Venda

def index(request):
    return render(request, 'produtos/index.html')

#CRUD Produtos

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

def produto_update(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    
    context = {
        'form': form,
        'produto': produto
    }
    return render(request, 'produtos/produtos_update.html', context)

def produto_delete(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('produto_list')
    

#Estoque
def estoque(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos/estoque.html', context)


#CRUD Vendas

def vendas(request):
    vendas = Venda.objects.all()
    faturamento_total = sum(venda.valor_total() for venda in vendas)
    context = {
        'vendas': vendas,
        'faturamento_total': faturamento_total
    }
    return render(request, 'produtos/vendas.html', context)

def create_venda(request):
    if request.method == 'POST':
        form = ProdutoVenda(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            produto = venda.produto
            if produto.estoque >= venda.quantidade:
                produto.estoque -= venda.quantidade
                print(f"Produto: {produto.nome} | Novo estoque: {produto.estoque}")
                produto.save()
                venda.save()
                return redirect('vendas')
            else:
                form.add_error('quantidade', 'Quantidade em estoque insuficiente.')
    else:
        form = ProdutoVenda()
    
    context = {
        'form': form
    }
    return render(request, 'produtos/vendas_create.html', context)