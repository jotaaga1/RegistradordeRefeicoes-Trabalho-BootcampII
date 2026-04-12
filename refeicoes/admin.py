from django.contrib import admin

from .models import Refeicao


@admin.register(Refeicao)
class RefeicaoAdmin(admin.ModelAdmin):
    list_display = ["nome", "calorias", "tipo", "data", "criado_em"]
    list_filter = ["tipo", "data"]
    search_fields = ["nome", "descricao"]
    date_hierarchy = "data"