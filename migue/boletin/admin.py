from django.contrib import admin

from .models import Registrado, Info_acerca, Info_contacto
#******************************** A D M I N****************************************
class Adminregistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp"]

    list_filter =["timestamp"]
    list_editable =["nombre"]
    search_fields =["email","nombre"]
    #class Meta:
         #model= Registrado
class Contregistrado(admin.ModelAdmin):
    list_display = ["nombre","email"]
    class Meta:
        model=Info_contacto

class Acregistrado(admin.ModelAdmin):
    list_display = ["nombre","texto"]
    class Meta:
        model=Info_acerca

admin.site.register(Registrado,Adminregistrado)
admin.site.register(Info_acerca,Acregistrado)
admin.site.register(Info_contacto,Contregistrado)