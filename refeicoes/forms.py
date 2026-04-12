from django import forms

from .models import Refeicao


class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = ["nome", "descricao", "calorias", "tipo", "data"]
        widgets = {
            "nome": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ex: Almoço, Café da manhã..."}
            ),
            "descricao": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ex: Arroz, feijão, frango..."}
            ),
            "calorias": forms.NumberInput(
                attrs={"class": "form-control", "min": "1"}
            ),
            "tipo": forms.Select(attrs={"class": "form-select"}),
            "data": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }

    def clean_calorias(self):
        calorias = self.cleaned_data.get("calorias")
        if calorias is not None and calorias <= 0:
            raise forms.ValidationError("As calorias devem ser maiores que zero.")
        return calorias

    def clean_nome(self):
        nome = self.cleaned_data.get("nome", "").strip()
        if not nome:
            raise forms.ValidationError("O nome não pode estar vazio.")
        return nome