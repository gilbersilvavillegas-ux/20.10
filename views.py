from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import entrenador
from .models import atleta
from .models import categoria
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .forms import EntrenadorForm
from .forms import AtletaForm
from .forms import CategoriaForm




#-------------------------------inicio de sesion--------------------------


# Create your views here.
def home(request):
    return render(request, 'home.html')


#-------------------------------inicio de sesion----------------------------














#-------------------------------inicio pagina-------------------------------

@login_required
def index(request):
    return render(request, 'index.html')

#-------------------------------inicio pagina--------------------------------












#------------------------------ENTRENADOR-----------------------------------


@login_required
def Entrenador(request):
    lista_entrenadores = entrenador.objects.all().order_by('apell_entre')
    contexto = {
        'titulo_pagina': 'Lista de Entrenadores',
        'usuario_actual': request.user, 
        'entrenadores': lista_entrenadores, 
    }
    return render(request, 'entrenador/entrenador.html', contexto)



@login_required
def reg_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()

            #MENSAJE DE ÉXITO PARA EL REGISTRO
            messages.success(request, 'Registro de entrenador realizado exitosamente.')

            return redirect('entrenador') 
        else:
            print("Errores de Validación:", form.errors)
    else:
        form = EntrenadorForm()

    return render(request, 'entrenador/reg_entrenador.html', {'form': form})



@login_required # Aseguramos que solo usuarios logueados puedan editar
def editar_entrenador(request, ci_entrenador):
    # Obtener el objeto Entrenador por su CI
    entrenador_obj = get_object_or_404(entrenador, ci_entrenador=ci_entrenador)
    
    if request.method == 'POST':
        # CORRECCIÓN 1: Añadir request.FILES para manejar la subida de fotos
        form = EntrenadorForm(request.POST, request.FILES, instance=entrenador_obj)
        
        if form.is_valid():
            # CORRECCIÓN 2: Lógica de guardado y redirección
            form.save()
            messages.success(request, 'Entrenador editado exitosamente.')
            return redirect('entrenador') # Redirige al nombre de URL 'entrenador'
        else:
            messages.error(request, 'Error al editar el entrenador. Verifique los campos.')
    else:
        # Inicializar el formulario con los datos actuales
        form = EntrenadorForm(instance=entrenador_obj)
        
    # CORRECCIÓN 3: Ruta de plantilla corregida
    return render(request, 'entrenador/editar_entrenador.html', {'form': form, 'entrenador_obj': entrenador_obj})

@require_POST
def eliminar_entrenador(request, ci_entrenador):
    try:
        # Usar 'entrenador' (minúscula) para referirse al modelo
        entrenador_obj = get_object_or_404(entrenador, ci_entrenador=ci_entrenador)
        entrenador_obj.delete()
        messages.success(request, 'Eliminación de entrenador realizada exitosamente.')


    except Exception as e:
        print(f"Error al eliminar entrenador: {e}")
        messages.error(request, 'No se pudo eliminar el entrenador.')
    return redirect('entrenador')


#-----------------------------ENTRENADOR---------------------------------------

















#------------------------------ATLETAS-----------------------------------------



@login_required
def atletas(request):
    atletas = atleta.objects.all()
    
    contexto = {
        'lista_atletas': atletas,
        'titulo': 'Lista Completa de Atletas'
    }
    return render(request, 'atletas/atletas.html', contexto)



@login_required
def reg_atleta(request):
    if request.method == 'POST':
        form = AtletaForm(request.POST)
        if form.is_valid():
            form.save()

            #MENSAJE DE ÉXITO PARA EL REGISTRO
            messages.success(request, 'Registro del atleta realizado exitosamente.')

            return redirect('atletas') 
        else:
            print("Errores de Validación:", form.errors)
    else:
        form = AtletaForm()

    return render(request, 'atletas/reg_atleta.html', {'form': form})



@require_POST
def eliminar_atleta(request, id_atleta):
    try:
        # Usar 'entrenador' (minúscula) para referirse al modelo
        atleta_obj = get_object_or_404(atleta, id_atleta=id_atleta) 
        atleta_obj.delete()
        messages.success(request, 'Eliminación del atleta realizada exitosamen.')
    
    
    except Exception as e:
        print(f"Error al eliminar atleta: {e}")
        messages.error(request, 'No se pudo eliminar el atleta.')
    return redirect('atletas')

@login_required 
def editar_atleta(request, id_atleta):
    atleta_obj = get_object_or_404(atleta, id_atleta=id_atleta)
    
    if request.method == 'POST':
        form = AtletaForm(request.POST, request.FILES, instance=atleta_obj) # Añadir request.FILES para manejar la foto
        if form.is_valid():
            form.save()

            # CORRECCIÓN: Redirección inmediata después de guardar
            messages.success(request, 'Atleta editado exitosamente.')
            return redirect('atletas') # Redirige a la lista de atletas
        else:
            messages.error(request, 'Error al editar el atleta. Verifique los campos.')        
    else:

        form = AtletaForm(instance=atleta_obj)
        
    return render(request, 'atletas/editar_atleta.html', {'form': form, 'atleta_obj': atleta_obj})


#-----------------------------ATLETAS---------------------------------------------

@login_required

def horarios(request):
    return render(request, 'horarios/horarios.html')

@login_required
def mensualidad(request):
    return render(request, 'mensualidades/mensualidad.html')

@login_required
def rendi_atleta(request):
    return render(request, 'atletas/rendi_atleta.html')

def exit(request):
    logout(request)
    return redirect('home')


@login_required
def reg_mensualidades(request):
    return render(request, 'mensualidad/reg_mensualidad.html')

@login_required
def registro_pruebas(request):
    return render(request, 'atletas/registro_pruebas.html')







#-----------------------------------CATEGORIAS----------------------------------------------
@login_required
def categorias(request):
    Categorias = categoria.objects.all()
    
    contexto = {
    'lista_categorias': Categorias,
    'titulo': 'Lista de Categorias'
    }
    return render(request, 'categorias/categorias.html', contexto)


@login_required
def registros_categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()

            #MENSAJE DE ÉXITO PARA EL REGISTRO
            messages.success(request, 'Registro de la Categoria realizado exitosamente.')

            return redirect('categorias') 
        else:
            print("Errores de Validación:", form.errors)
    else:
        form = CategoriaForm()

    return render(request, 'categorias/registros_categoria.html', {'form': form})

@login_required
def eliminar_categoria(request, id_categoria):
    try:
        categoria_obj = get_object_or_404(categoria, id_categoria=id_categoria)
        categoria_obj.delete()
        messages.success(request, 'Eliminación de la categoria realizada exitosamente.')

    except Exception as e:
        print(f"Error al eliminar la categoría:{e}")
        messages.error(request, 'No se pudo eliminar la categoría.')
    return redirect('categorias')

@login_required
def editar_categorias(request, id_categoria):
    categoria_obj = get_object_or_404(categoria, id_categoria=id_categoria)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria_obj)
        if form.is_valid():
            form.save()

            messages.success(request, 'Categoría editada exitosamente.')
            return redirect('categorias')
        else:
            messages.error(request, 'Error al editar la categoría. Verifique los campos')
    else:

        form = CategoriaForm(instance=categoria_obj)

    return render(request, 'categorias/editar_categorias.html', {'form':form, 'categoria_obj': categoria_obj})

@login_required
def registrar_mensualidad(request):
    if request.method == 'POST':
        # Instancia el formulario con los datos POST y los archivos
        form = MensualidadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # El form.save() crea y guarda el nuevo objeto Mensualidad en la BD
            mensualidad_nueva = form.save()
            
            # Opcional: Muestra un mensaje de éxito
            messages.success(request, f"Mensualidad para {mensualidad_nueva.id_atleta.nombre} registrada correctamente.")
            
            # Redirige a donde quieras después de guardar (ej: a la lista de mensualidades)
            return redirect('nombre_de_tu_lista_de_mensualidades') 
        else:
            # Si el formulario no es válido, se mostrará con los errores
            pass
            
    else:
        # Para peticiones GET, crea una instancia vacía del formulario
        form = MensualidadForm()
        
    context = {
        'form': form,
        'titulo': 'Registro de Nueva Mensualidad'
    }
    
    return render(request, 'mensualidades/registro_mensualidad.html', context)
