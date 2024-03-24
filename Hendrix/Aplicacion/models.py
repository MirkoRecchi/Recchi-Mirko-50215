from django.db import models
from django.contrib.auth.models import User



#---------------------------------ModelosHendrix-----------------------------------------


class Alumno (models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    legajo= models.IntegerField()
    comision= models.IntegerField()

    def __str__(self):
        return f"{self.nombre},{self.apellido}"
    



class Comision (models.Model):
    turno= models.CharField(max_length=50)
    horario= models.CharField(max_length=60)
    numcomision= models.IntegerField()
    def __str__(self):
        return f"{self.numcomision}"
    
    class Meta:
        verbose_name = "Comision"
        verbose_name_plural= "Comisiones"




class Cursado (models.Model):
    nombrealumno= models.CharField(max_length=50)
    numcomision= models.IntegerField()
    turno= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.numcomision}"
    
    class Meta:
        verbose_name = "Cursado"
        verbose_name_plural= "Cursados"




class Materia (models.Model):
    nombre= models.CharField(max_length=50)
    año= models.CharField(max_length=20)
    correlatividad= models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"





class Mesa (models.Model):
    NombreMateria= models.CharField(max_length=50)
    horario= models.CharField(max_length=50)
    dia= models.CharField(max_length=50)
    nombreProfesor = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.NombreMateria}"
    




class Examen (models.Model):
    nombrealumno= models.CharField(max_length=50)
    numcomision= models.IntegerField()
    nombreProfesor = models.CharField(max_length=50)
    nombreMateria = models.CharField(max_length=50,default='DEFAULT VALUE')
    def __str__(self):
        return f"{self.nombreMateria}"
    
    class Meta:
        verbose_name = "Examen"
        verbose_name_plural= "Examenes"




class Calificacion (models.Model):
    NombreMateria= models.CharField(max_length=50)
    NombreAlumno = models.CharField(max_length=50)
    nota= models.IntegerField()
    def __str__(self):
        return f"{self.NombreMateria}"
    
    class Meta:
        verbose_name = "Calificacion"
        verbose_name_plural= "Calificaciones"





class Modelo (models.Model):
    NombreMateria= models.CharField(max_length=50)
    dia= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to="modelos",null=True)
    def __str__(self):
        return f"{self.NombreMateria}"
    

    


    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    #Si el usuario se borra , la imagen tambien    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"


    

