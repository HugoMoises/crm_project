from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.forms import modelformset_factory
from .forms import ProdutoForm, ProdutoVenda
from .models import Produto, Venda, ItemVenda

def index(request):
    return render(request, 'produtos/index.html')

#CRUD Produtos

def produto_list(request):

    search = request.GET.get('search')
    page = request.GET.get('page')

    if search:
        produtos_list = Produto.objects.filter(nome__icontains=search).order_by('nome')

    else:
        produtos_list = Produto.objects.all().order_by('nome')
        
    paginator = Paginator(produtos_list, 5)
    produtos = paginator.get_page(page)

    context = {
        'produtos': produtos,
    }
    return render(request, 'produtos/produtos_list.html', context)

def create_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
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
    
def produto_detail(request, id):
    produto = get_object_or_404(Produto, id=id)
    context ={
        'produto': produto,
    }
    return render(request, 'produtos/produto_detail.html', context)

#Estoque
def estoque(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'produtos/estoque.html', context)


#CRUD Vendas

def vendas(request):
    vendas = Venda.objects.all().order_by('-data')
    
    search = request.GET.get('search')

    if search:
        vendas = Venda.objects.filter(produto__nome__icontains=search).order_by('-data')
    
    else:

        paginator = Paginator(vendas, 5)

        page = request.GET.get('page')

        vendas = paginator.get_page(page)

    faturamento_total = sum(venda.valor_total() for venda in vendas)

    context = {
        'vendas': vendas,
        'faturamento_total': faturamento_total
    }
    return render(request, 'vendas/vendas.html', context)

def create_venda(request):
    ItemVendaFormSet = modelformset_factory(ItemVenda, form=ProdutoVenda, extra=1, can_delete=True)
    if request.method == 'POST':
        formset = ItemVendaFormSet(request.POST, queryset=ItemVenda.objects.none())
        if formset.is_valid():
            form_preenchido = [form for form in formset if form.cleaned_data]

            if not form_preenchido:
                context = {
                    'erro': 'Nenhum item preenchido.',
                    'formset': formset
                }
                return render(request, 'vendas/vendas_create.html', context)
            
            venda = Venda.objects.create()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    produto = form.cleaned_data.get('produto')
                    quantidade = form.cleaned_data.get('quantidade')
                
                    if produto.estoque >= quantidade:
                        produto.estoque -= quantidade
                        produto.save()

                        ItemVenda.objects.create(
                            venda=venda,
                            produto=produto,
                            quantidade=quantidade,
                            preco_unitario = produto.preco
                        )   
                
                    else:
                        form.add_error('quantidade', 'Quantidade em estoque insuficiente.')
                        return render(request, 'vendas/vendas_create.html', {'formset': formset})
            
            return redirect('vendas')

    else:
        formset = ItemVendaFormSet(queryset=ItemVenda.objects.none())
    return render(request, 'vendas/vendas_create.html', {'formset': formset})

def detail_venda(request, id):
    vendas = get_object_or_404(Venda, id=id)
    itens = vendas.itens.all()

    total = vendas.valor_total()
    
    context = {
        'vendas': vendas,
        'itens': itens,
        'total': total    
}
    return render(request, 'vendas/detail_venda.html', context)

