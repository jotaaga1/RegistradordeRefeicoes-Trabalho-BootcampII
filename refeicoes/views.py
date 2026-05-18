from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import RefeicaoForm
from .models import TIPOS_REFEICAO, Refeicao

from django.shortcuts import render
from .services import buscar_alimento

def adicionar_refeicao(request):

    alimento = None

    if request.method == "POST":
        nome = request.POST.get("descricao")

        dados = buscar_alimento(nome)

        if dados["foods"]:
            alimento = dados["foods"][0]

    return render(request, "refeicoes/adicionar.html", {
        "alimento": alimento
    })

def index(request):
    refeicoes = Refeicao.objects.all()

    tipo_filtro = request.GET.get("tipo", "")
    if tipo_filtro:
        refeicoes = refeicoes.filter(tipo=tipo_filtro)

    total_calorias = refeicoes.aggregate(total=Sum("calorias"))["total"] or 0

    resumo = []
    for cod, nome in TIPOS_REFEICAO:
        subtotal = (
            Refeicao.objects.filter(tipo=cod).aggregate(s=Sum("calorias"))["s"]
            or 0
        )
        if subtotal > 0:
            resumo.append({"nome": nome, "total": subtotal})

    context = {
        "refeicoes": refeicoes,
        "total_calorias": total_calorias,
        "resumo": resumo,
        "tipos": TIPOS_REFEICAO,
        "tipo_filtro": tipo_filtro,
        "mes_atual": timezone.now().strftime("%B de %Y"),
    }
    return render(request, "refeicoes/index.html", context)


def adicionar(request):
    if request.method == "POST":
        form = RefeicaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Refeição adicionada com sucesso!")
            return redirect("refeicoes:index")
    else:
        form = RefeicaoForm(initial={"data": timezone.now().date()})

    return render(request, "refeicoes/refeicao_form.html", {"form": form, "titulo": "Adicionar Refeição"})


def editar(request, pk):
    refeicao = get_object_or_404(Refeicao, pk=pk)
    if request.method == "POST":
        form = RefeicaoForm(request.POST, instance=refeicao)
        if form.is_valid():
            form.save()
            messages.success(request, "Refeição atualizada com sucesso!")
            return redirect("refeicoes:index")
    else:
        form = RefeicaoForm(instance=refeicao)

    return render(request, "refeicoes/refeicao_form.html", {"form": form, "titulo": "Editar Refeição"})


def excluir(request, pk):
    refeicao = get_object_or_404(Refeicao, pk=pk)
    if request.method == "POST":
        refeicao.delete()
        messages.success(request, "Refeição removida com sucesso!")
        return redirect("refeicoes:index")

    return render(request, "refeicoes/confirmar_exclusao.html", {"refeicao": refeicao})
