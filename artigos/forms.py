from django import forms
from .models import Artigo, Comentario


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ["titulo", "texto", "fotografia", "link_externo"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "texto": forms.Textarea(
                attrs={
                    "rows": 12,
                    "class": "form-control",
                    "placeholder": "Conteúdo sobre tecnologia ou soft skills…",
                }
            ),
            "fotografia": forms.FileInput(attrs={"class": "form-control"}),
            "link_externo": forms.URLInput(attrs={"class": "form-control"}),
        }


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(
                attrs={"rows": 3, "placeholder": "O teu comentário…", "class": "form-control"}
            ),
        }
