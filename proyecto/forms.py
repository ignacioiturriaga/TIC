from django import forms

from proyecto.models import proyecto, Galeria, Comment


class ProyectoForm(forms.ModelForm):
	#galeria_imagenes = forms.ImageField()
	class Meta:
		model = proyecto

		fields = [
			'titulo',
			'logo',
			'descripcion_general',
			'descripcion_detallada',
			'definicion_problema',
			'definicion_solucion',
			'galeria_imagenes',
			'video',
		]
		labels = {
			'titulo': 'Nombre del Proyecto',
		#	'logo' : 'Logo',
			'descripcion_general': 'Descripcion General',
			'descripcion_detallada': 'Visión general del negocio',
			'definicion_problema':'Definicion del Problema',
			'definicion_solucion': 'Solucion propuesta',
		#   'galeria_imagenes' : 'Galeria de Imagenes',
		}
		widgets = {
			'titulo': forms.TextInput(attrs={'class':'form-control'}),
			'descripcion_detallada': forms.Textarea(attrs={'class':'form-control'}),
			'descripcion_general': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_problema': forms.Textarea(attrs={'class':'form-control'}),
			'definicion_solucion': forms.Textarea(attrs={'class':'form-control'}),
		}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)