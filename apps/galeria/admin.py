from django.contrib import admin
from apps.galeria.models import Fotografia

class ListarFotografias(admin.ModelAdmin):
    list_display=("id", "nome", "categoria", "data_fotografia", "legenda", "publicar", "usuario",)
    list_display_links = ("id", "nome", "categoria", "data_fotografia",)
    search_fields=("nome",)
    list_filter=("categoria","usuario",)
    list_editable = ("publicar",)
    list_per_page=10

admin.site.register(Fotografia, ListarFotografias)