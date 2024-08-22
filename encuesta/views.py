from django.shortcuts import render
import math

def index(request):
    context = {
        'titulo': "Formulario", 
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

from django.shortcuts import render

def calculo(request):
    context = {
        'titulo': "Calculadora",
    }
    return render(request, 'encuesta/calculo.html', context)

def resultado(request):
    num1 = int(request.POST['numero1'])
    num2 = int(request.POST['numero2'])
    operacion = request.POST['operacion']
    
    if operacion == 'suma':
        resultado = num1 + num2
        operacion_texto = "suma"
    elif operacion == 'resta':
        resultado = num1 - num2
        operacion_texto = "resta"
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
        operacion_texto = "multiplicación"
    
    context = {
        'titulo': "Resultado",
        'num1': num1,
        'num2': num2,
        'operacion': operacion_texto,
        'resultado': resultado,
    }
    
    return render(request, 'encuesta/resultado.html', context)

def cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def calcular_volumen(request):
    altura = float(request.POST['altura'])
    diametro = float(request.POST['diametro'])
    radio = diametro / 2
    volumen = math.pi * (radio ** 2) * altura 

    context = {
        'titulo': "Resultado del Volumen del Cilindro",
        'altura': altura,
        'diametro': diametro,
        'volumen': volumen,
    }
    
    return render(request, 'encuesta/result_cilindro.html', context)