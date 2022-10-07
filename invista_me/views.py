from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoForms
from django.contrib.auth.decorators import login_required



def investimentos(request):
    dados = {
        'dados' : Investimento.objects.all()
    }
    return render(request, 'investimentos/investimentos.html', context=dados)


def detalhe(request, id_investimento):
    dados = {
        'dados' : Investimento.objects.get(pk=id_investimento)
        }
    return render(request, 'investimentos/detalhe.html', dados)

@login_required
def criar_investimento(request):
    if request.method == 'POST':
        investimento_forms = InvestimentoForms(request.POST)
        if investimento_forms.is_valid():
            investimento_forms.save()
        return redirect('investimentos')
    else:
        investimento_forms = InvestimentoForms()
        formulario = {
            'formulario' : investimento_forms
        }
        return render(request, 'investimentos/novo_investimento.html', context=formulario)
    
    
@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method== 'GET':
        formulario = InvestimentoForms(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html',{'formulario':formulario})
    if request.method== 'POST':
        formulario = InvestimentoForms(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/excluir.html', {'item':investimento})
        