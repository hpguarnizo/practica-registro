from django.shortcuts import render
from.forms import RegModelForm, ContactForm, Acercaform
from .models import Registrado, Info_contacto, Info_acerca

#******************************************** V I S T A S ********************************************************

def inicio(request):
    titulo="HOLA"
    abc= "xD"
    if request.user.is_authenticated():
        titulo= "Bienvenido %s" %(request.user)

    form= RegModelForm(request.POST or None)
    context = {
        "titulo": titulo,
        "el_form": form,

    }
    if form.is_valid():
        instance= form.save(commit=False)
        nombre= form.cleaned_data.get("nombre")
        email = form.cleaned_data.get("email")
        if not nombre:
            nombre= "PERSONA"
        instance.save()
        context= {
            "titulo": "Gracias %s!"%(nombre)
        }
        if not nombre:
            context = {
            "titulo": "Gracias %s!" % (nombre)
        }
        print (instance)
        print (instance.timestamp)
       #form_data =form.cleaned_data
       #abc =form_data.get("email")
       #abc2= form_data.get("nombre")
       #obj = Registrado.objects.create(email=abc, nombre=abc2)

    if request.user.is_authenticated():
            queryset= Registrado.objects.all().order_by("-timestamp")
            context = {
            "queryset": queryset,
        }
    return render(request, "inicio.html", context)
#*********************************************************************************
def contact(request):
    titulo = "Contacto"
    form= ContactForm(request.POST or None)
    context = {
        "form": form,
        "titulo": titulo,
    }
    if form.is_valid():
        #for key, value in form.cleaned_data.iteritems():********PYTHON 2
           # print (key,value)
        a= form.cleaned_data.get("nombre")
        b= form.cleaned_data.get("email")
        titulo = "Gracias %s!" % (a)
        asd= Info_contacto.objects.create(nombre=a,email=b)
        #print (a,b)
    context= {
        "form":form,
        "titulo":titulo,

    }
    return render(request,"forms.html",context)
#**************************************************************************************************
def about(request):
    titulo = "Acerca de"
    form= Acercaform(request.POST or None)
    context = {
        "form": form,
        "titulo": titulo,

    }
    if form.is_valid():
        #for key, value in form.cleaned_data.iteritems():********PYTHON 2
           # print (key,value)
        a= form.cleaned_data.get("nombre")
        b= form.cleaned_data.get("texto")
        titulo = "Gracias %s!" % (a)
        asd= Info_acerca.objects.create(nombre=a,texto=b)
        #print (a,b)
    context= {
        "form":form,
        "titulo":titulo,

    }
    return render(request,"forms.html",context)
