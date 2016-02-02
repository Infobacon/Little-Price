from django.shortcuts import render_to_response,render, get_object_or_404,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import Context,loader, RequestContext
from .models import *
from .forms import  *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
import json
import datetime
from chartit import DataPool, Chart



def index_view(request):
	#listo
	dato = Producto.objects.all()
	supers=Supermercado.objects.all()
	return render(request,"index.html",{'dprod':dato,'dsuper':supers})

def supnames(month_num):
    names ={0: 'Tottus', 1: 'Ekono', 2: 'Lider'}
    return names[month_num]
def canasta_basica_view(request,id_producto):
	#listo
	form = VotoForm()
	dato = get_object_or_404(Producto, id_producto=id_producto)
	precios = get_list_or_404(ProductoPrecio, id_producto=id_producto)
	votos=get_list_or_404(Valoracion, id_producto_precio=id_producto)
	supers=Supermercado.objects.all()
	contador=0
	suma=0
	for element in votos:
		suma=suma+element.valoracion
		contador=contador+1
	suma=suma/contador
	pool=DataPool(
           series=
            [{'options': {
               'source': ProductoPrecio.objects.filter(id_producto=id_producto)},
              'terms': [
                'precio',
                'id_producto_precio',
                'id_supermercado']}

             ])
	cht = Chart(
            datasource = pool,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'id_supermercado': [
                    'precio'
                    ]
                  }}],
            chart_options =
              {'title': {
                   'text': 'Comparacion de precios'},
               'xAxis': {
                    'title': {
                       'text': 'Supermercados'}}},
        x_sortf_mapf_mts = (None, supnames, False))
	return render(request,"producto.html",{"dprod":dato,"dprecio":precios,"nota":suma,"dsuper":supers,'form':form,'cht': cht})

def supermercados_detalle_view(request,id_supermercado):
	#listo
	supermercado =  get_object_or_404(Supermercado, id_supermercado=id_supermercado) #Capturo todos los cines
	return render(request,"detalles_supermercados.html",{'supermercado':supermercado})

def supermercados_view(request):
	#listo
	supermercado = Supermercado.objects.all() #Capturo todos los cines
	return render(request,"supermercados.html",{'dsuper':supermercado})


def lista_productos(request):
	#listo
	dato = Producto.objects.all()
	return render(request,"lista_productos.html",{'dprod':dato})

def estrellitas(request,id_producto_precio):
	#listo
	usuario=request.user.id	
	now = datetime.datetime.now()
	if request.POST:
		form = VotoForm(request.POST.copy())
		form.data['id_usuario']=usuario		
		form.data['fecha']=now
		form.data['id_producto_precio']=id_producto_precio
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/index/')
	else:
		form = VotoForm()
	return HttpResponse(json.dumps(response_data),content_type="application/json")
def perfil(request):
	#listo
	perfil = Usuario.objects.all()	
	usuario=request.user.id
	if request.POST:
		form = PerfilForm(request.POST.copy())
		form.data['id_usuario']=usuario
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/index/')
	else:
		form = PerfilForm()
	return render(request,"myaccount.html",{'dperfil':perfil, 'form':form})

#login_user 1, solo puede estar aca si esta logeado
def mis_productos_view(request):
	#listo
	us=request.user.id
	dato2=[]
	usa=get_object_or_404(Usuario, id_usuario=us)
	dato = get_list_or_404(ProductoPrecio, id_usuario=usa)
	for e in dato:
		aux=get_object_or_404(Producto, id_producto=e.id_producto.id_producto)
		dato2.append(aux)
	return render(request,"mis_productos.html",{'dprod':dato2,'object':dato})

	#login_user 1, solo puede estar aca si esta logeado

def ingresar_producto_view(request):
	#listo
	usuario=request.user.id
	now = datetime.datetime.now()
	if request.POST:
		form = ProductoForm(request.POST.copy())
		form.data['id_usuario']=usuario
		form.data['fecha']=now
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home')
		else:
			return HttpResponseRedirect('/index/')
	else:
		form = ProductoForm()
	return render(request,'ingresar_producto.html',{'form':form})

def grafico_view(request):
	#incompleto - fallo en la base de datos
	productos=Producto.objects.all()
	precios=ProductoPrecio.objects.all()
	return render(request,'grafico.html',{'dprod':productos,'dprecio':precios})

#def comparar_productos_view(request):
	#incompleto
	#login_user = 1
	#productos = ['Arroz','Harina']
	
	#return render_to_response('web/grafico.html',locals())


#no existe tabla para favoritos
def favoritos_view(request):
	login_user = 1
	return render_to_response('web/favoritos.html',locals())
	
