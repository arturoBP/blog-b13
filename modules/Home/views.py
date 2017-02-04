from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Index(request):


	return render(request,'Home/index.html')

def Contacto(request):

	return HttpResponse('pagina de contactos')

def Otros(request,num):

	return HttpResponse('pagina de otros numero: <b> '+num+'')
def Suma(requests,num1,num2):
	suma = int(num1) + int(num2)

	return HttpResponse('la suma de los numeros: '+str(suma))
# def Comp(request,num1,num2)

# if num1 > num2:
# 	return HttpResponse('el primero es mayor ')
# elif:
# 	return HttpResponse('el segundo es mayor ')

