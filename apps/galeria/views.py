from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicar=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem (request, foto_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicar=True)
    if "buscar" in request.GET:
        nome_busca = request.GET['buscar']
        
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
           
    return render(request, "galeria/index.html", {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova Fotografia Cadastrada!')
            return redirect('index')
    
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
   fotografia = Fotografia.objects.get(id=foto_id)
   form = FotografiaForms(instance=fotografia)
   
   if request.method == 'POST':
       form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
       if form.is_valid():
           form.save()
           messages.success(request, 'Fotografia Atualizada!')
           return redirect('index')
   
   return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Foto Deletada com Sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicar=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"cards": fotografias})