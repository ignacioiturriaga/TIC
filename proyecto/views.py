from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#Modelo proyecto
from proyecto.models import proyecto, Galeria
from proyecto.forms import ProyectoForm, CommentForm
#Vistas
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
# Create your views here.
def index(request):
	return render(request, 'index.html')

#CLASES  PARA GALERIA
class GaleriaDetail(DetailView):
	model = Galeria
	template_name = 'proyecto/proyecto_detalle.html'


class GaleriaList(ListView):
	model = Galeria
	template_name = 'proyecto/proyecto_list.html'
	paginate_by = 6

class GaleriaCreate(CreateView):
	model = Galeria
	form_class = ProyectoForm
	template_name = 'galeria/galeria_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class GaleriaUpdate(UpdateView):
	model = Galeria
	form_class = ProyectoForm
	template_name ='galeria/galeria_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class GaleriaDelete(DeleteView):
	model = Galeria
	template_name = 'proyecto/proyecto_delete.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')

#CLASES DE PROYECTO

class proyectoDetail(DetailView):
	model = proyecto
	template_name = 'proyecto/proyecto_detalle.html'

class proyectoList(ListView):
	model = proyecto
	template_name = 'proyecto/proyecto_list.html'
	paginate_by = 4

class proyectoList2(ListView):
	model = proyecto
	template_name = 'proyecto/proyecto_list0.html'
	paginate_by = 12

class proyectoCreate(CreateView):
	model = proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class proyectoUpdate(UpdateView):
	model = proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')


class proyectoDelete(DeleteView):
	model = proyecto
	template_name = 'proyecto/proyecto_delete.html'
	success_url = reverse_lazy('proyecto:proyecto_listar')

@login_required
def agregar_comentario(request, pk):
    proyecto_instancia = get_object_or_404(proyecto, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.proyecto = proyecto_instancia
            comment.save()
            return redirect('proyecto:proyecto_detalle', pk=proyecto_instancia.pk)
    else:
        form = CommentForm()
    return render(request, 'proyecto/agregar_comentario.html', {'form': form})