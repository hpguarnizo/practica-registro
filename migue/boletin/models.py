from django.db import models
#******************* M O D E L O S *************************************************
class Registrado(models.Model):
    nombre=models.CharField(max_length=100, blank=True, null=True)
    email= models.EmailField()
    timestamp= models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email

class Info_contacto(models.Model):
    nombre= models.CharField(max_length=100)
    email= models.EmailField()
    mensaje= models.TextField

    def __str__(self):
        return self.email

class Info_acerca(models.Model):
    nombre = models.CharField(max_length=100)
    texto= models.TextField()

    def __str__(self):
        return self.nombre
