from django.core.validators import MinValueValidator
from django.db import models


TIPOS_REFEICAO = [
    ("cafe", "Café da manhã"),
    ("almoco", "Almoço"),
    ("jantar", "Jantar"),
    ("lanche", "Lanche"),
]


class Refeicao(models.Model):
    nome = models.CharField("Nome", max_length=200)
    descricao = models.TextField("Descrição", blank=True)
    calorias = models.IntegerField(
        "Calorias",
        validators=[MinValueValidator(1)],
    )
    tipo = models.CharField(
        "Tipo",
        max_length=20,
        choices=TIPOS_REFEICAO,
        default="outros",
    )
    data = models.DateField("Data")
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)

    class Meta:
        ordering = ["-data", "-criado_em"]
        verbose_name = "Refeição"
        verbose_name_plural = "Refeições"

    def __str__(self):
        return f"{self.nome} — {self.calorias} kcal"

    def get_tipo_display_label(self):
        return dict(TIPOS_REFEICAO).get(self.tipo, self.tipo)