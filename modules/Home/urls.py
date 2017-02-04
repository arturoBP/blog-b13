from django.conf.urls import url
from django.contrib import admin
from .views import Index,Contacto,Otros,Suma
urlpatterns = [
	url(r'^$', Index, name='index'),
	url(r'^contactos$', Contacto, name='Contacto'),
	url(r'^otros/(?P<num>[0-9]+)/$', Otros, name='otros'),
	url(r'^suma/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Suma, name='suma'),
	#url(r'^comp/(?P<num1>[0-9]+)/(?P<num2>[0-9]+)/$', Comp, name='suma'),

    #url(r'^admin/', admin.site.urls),
]