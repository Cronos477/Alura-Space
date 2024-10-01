from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicar',]
        labels = {
            'descricao': 'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Foto'
            }),
            'legenda': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Legenda da Foto'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Categoria'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição da Foto'
            }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Foto'
            }),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'usuario': forms.Select(attrs={
                'class': 'form-control'
            }),
        }