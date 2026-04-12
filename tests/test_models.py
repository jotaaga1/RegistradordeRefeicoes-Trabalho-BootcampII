import pytest
from django.utils import timezone
from refeicoes.models import Refeicao


@pytest.mark.django_db
def test_criar_refeicao():
    refeicao = Refeicao.objects.create(
        nome="Almoço",
        calorias=500,
        tipo="almoco",
        data=timezone.now().date(),
    )
    assert refeicao.pk is not None
    assert refeicao.nome == "Almoço"
    assert refeicao.calorias == 500
    assert refeicao.tipo == "almoco"


@pytest.mark.django_db
def test_str_refeicao():
    refeicao = Refeicao(nome="Jantar", calorias=700)
    assert str(refeicao) == "Jantar — 700 kcal"


@pytest.mark.django_db
def test_listagem_refeicoes():
    Refeicao.objects.create(
        nome="Café da manhã",
        calorias=300,
        tipo="cafe",
        data=timezone.now().date(),
    )
    Refeicao.objects.create(
        nome="Lanche",
        calorias=200,
        tipo="lanche",
        data=timezone.now().date(),
    )

    refeicoes = Refeicao.objects.all()
    assert refeicoes.count() == 2