"""Pinkys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'/$', 'littleprice.views.index_view'),
    url(r'home/$', 'littleprice.views.index_view'),
    url(r'supermercados_detalle/(?P<id_supermercado>\d+)$', 'littleprice.views.supermercados_detalle_view'),
    url(r'^admin/', include(admin.site.urls)),     
    url(r'^estrellitas/(?P<id_producto_precio>\d+)$','littleprice.views.estrellitas'),
    url(r'^supermercados/$', 'littleprice.views.supermercados_view'),
    url(r'^perfil/$', 'littleprice.views.perfil'),
    url(r'^accounts/', include('registration.urls')),
    url(r'^mis_productos/$', 'littleprice.views.mis_productos_view'),
    url(r'^favoritos/$', 'littleprice.views.favoritos_view'),
    url(r'^canasta_basica/(?P<id_producto>\d+)$', 'littleprice.views.canasta_basica_view'),
    url(r'^grafico/$', 'littleprice.views.grafico_view'),
    url(r'^ingresar_producto/$', 'littleprice.views.ingresar_producto_view'),
    url(r'^lista_productos/$', 'littleprice.views.lista_productos'),
    


]


if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

