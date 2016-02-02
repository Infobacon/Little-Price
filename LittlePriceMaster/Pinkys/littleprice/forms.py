#encoding:utf-8
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *
from django_bootstrap_typeahead.fields import *





class SignUpForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']
		widgets = {'password':forms.PasswordInput(),
		}

class PerfilForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre_usuario','correo']

#Para el Typeahead
class ProductoForm(ModelForm):
    class Meta:
        model=ProductoPrecio
        fields=['precio','fecha','id_usuario','id_producto','id_supermercado']
class VotoForm(ModelForm):
    class Meta:
        model=Valoracion
        fields=['id_usuario','id_producto_precio','valoracion','fecha']
def build_thing(value):
    created = Thing.objects.get_or_create(name=value)
    return created


class TestForm(forms.Form):
    typeahead = TypeaheadField(
        queryset=Producto.objects.all(),
        builder=build_thing,
        required=False
    )

