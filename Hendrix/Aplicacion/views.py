
#-----------------------LibreriasCRUD------------------------------------------------
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

#-----------------------Login , Registro  y Auntenticaciones--------
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#------------------------Modificacion de claves----------------------------

from django.contrib.auth.views import PasswordChangeView

#----------------------Permisos---------------------------------------------

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required


#-----------------OtrasLibreriasImportantes---------------------------------
from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from.forms import *
from .models import *






#-----------------------Inicio-----------------------------------
@login_required
def inicio (request):
    return render(request , "Aplicacion/Estetica/index.html")


def prelogin (request):
    return render(request , "Aplicacion/Estetica/inicioprelogin.html")

def acercademi (request):
    return render(request , "Aplicacion/Acerca de mi/Acercademi.html")


#-----------------------AlumnoCRUD-------------------------------
class AlumnoList(LoginRequiredMixin,ListView):
    model = Alumno

class AlumnoCreate(LoginRequiredMixin,CreateView):
    model = Alumno
    fields = ["nombre","apellido","legajo","comision"]
    success_url= reverse_lazy("alumno")

class AlumnoUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "Aplicacion | alumno.change_alumno"
    model = Alumno
    fields = ["nombre","apellido","legajo","comision"]
    success_url= reverse_lazy("alumno")

class AlumnoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "Aplicacion | alumno.delete_alumno"
    model = Alumno
    success_url= reverse_lazy("alumno")




#-----------------------CursadoCRUD------------------------------

class CursadoList(LoginRequiredMixin,ListView):
    model = Cursado

class CursadoCreate(LoginRequiredMixin,CreateView):
    model = Cursado
    fields = ["nombrealumno","numcomision","turno"]
    success_url= reverse_lazy("cursado")

class CursadoUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "Aplicacion | Cursado.change_cursado"
    model = Cursado
    fields = ["nombrealumno","numcomision","turno"]
    success_url= reverse_lazy("cursado")

class CursadoDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "Aplicacion | Cursado.delete_cursado"
    model = Cursado
    success_url= reverse_lazy("cursado")


#-----------------------ExamenCRUD--------------------------------
class ExamenList(LoginRequiredMixin,ListView):
    model = Examen

class ExamenCreate(LoginRequiredMixin,CreateView):
    model = Examen
    fields = ["nombrealumno","numcomision","nombreProfesor","nombreMateria"]
    success_url= reverse_lazy("examen")

class ExamenUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "Aplicacion | Examen.change_examen"
    model = Examen
    fields = ["nombrealumno","numcomision","nombreProfesor","nombreMateria"]
    success_url= reverse_lazy("examen")

class ExamenDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "Aplicacion | Examen.delete_examen"
    model = Examen
    success_url= reverse_lazy("examen")       

#-----------------------CalificacionCRUD--------------------------

def calificacion (request):
    contexto = {'calificacion': Calificacion.objects.all().order_by("id")}
    return render(request, "Aplicacion/Calificacion/calificacion.html", contexto) 


@permission_required("Aplicacion | Calificacion.add_calificacion")   
def calificacionCreate(request):
    if request.method == "POST":
        miForm = CalificacionForm(request.POST)
        if miForm.is_valid():
            calificacion_NombreMateria = miForm.cleaned_data.get("NombreMateria")
            calificacion_NombreAlumno = miForm.cleaned_data.get("NombreAlumno")
            calificacion_nota=miForm.cleaned_data.get("nota")
            calificacion = Calificacion(NombreMateria=calificacion_NombreMateria,NombreAlumno=calificacion_NombreAlumno,nota=calificacion_nota)
            calificacion.save()
            return redirect(reverse_lazy('calificacion'))
    else:
        miForm = CalificacionForm()

    return render(request, "Aplicacion/Calificacion/calificacion_form.html", {"form": miForm} )    


@permission_required("Aplicacion | Calificacion.change_calificacion")      
def calificacionUpdate(request, id_calificacion):
    calificacion = Calificacion.objects.get(id=id_calificacion)
    if request.method == "POST":
        miForm = CalificacionForm(request.POST)
        if miForm.is_valid():
            calificacion.NombreMateria = miForm.cleaned_data.get("NombreMateria")
            calificacion.NombreAlumno = miForm.cleaned_data.get("NombreAlumno")
            calificacion.nota=miForm.cleaned_data.get("nota")
            calificacion.save()
            return redirect(reverse_lazy('calificacion'))
    else:
        miForm = CalificacionForm(initial={'NombreMateria': calificacion.NombreMateria, 'NombreAlumno': calificacion.NombreAlumno,"nota":calificacion.nota})

    return render(request, "Aplicacion/Calificacion/calificacion_form.html", {"form": miForm} )

@permission_required("Aplicacion | Calificacion.delete_calificacion")   
def calificacionDelete(request, id_calificacion):
    calificacion= Calificacion.objects.get(id=id_calificacion)
    calificacion.delete()
    return redirect(reverse_lazy('calificacion'))

#-----------------------MesaCRUD----------------------------------

class MesaList(LoginRequiredMixin,ListView):
    model = Mesa

class MesaCreate(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "Aplicacion | mesa.add_calificacion"
    model = Mesa
    fields = ["NombreMateria","horario","dia","nombreProfesor"]
    success_url= reverse_lazy("mesa")

class MesaUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = "Aplicacion | mesa.change_calificacion"
    model = Mesa
    fields = ["NombreMateria","horario","dia","nombreProfesor"]
    success_url= reverse_lazy("mesa")

class MesaDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "Aplicacion | mesa.delete_calificacion"
    model = Mesa
    success_url= reverse_lazy("mesa")

#----------------------------Modelo------------------------------
def modelo (request):
    contexto = {'modelo': Modelo.objects.all().order_by("id")}
    return render(request, "Aplicacion/Modelos/modelo.html", contexto) 

@permission_required("Aplicacion | modelo.add_modelo")   
def SubirModelo(request):
    if request.method == "POST":
        miForm = ModeloForms(request.POST , request.FILES)
        examen = Modelo()
        if miForm.is_valid():
            modelo_NombreMateria=miForm.cleaned_data.get("NombreMateria")
            modelo_dia=miForm.cleaned_data.get("dia")
            modelo_imagen=request.FILES.get("imagen")
            modelo= Modelo(NombreMateria=modelo_NombreMateria,dia=modelo_dia,imagen=modelo_imagen)
            modelo.save()
            return redirect(reverse_lazy('modelo'))
    else:
        miForm = ModeloForms()

    return render(request, "Aplicacion/Modelos/model_form.html", {"form": miForm} )  

#-----------------OtrasClases-------------------------------------
    

class MateriaList(LoginRequiredMixin,ListView):
    model = Materia

class ComisionList(LoginRequiredMixin,ListView):
    model = Comision



#------------------------Buscar y Encontrar Calificacion----------------------

def BuscarCalificacion(request):
    return render(request, "Aplicacion/Calificacion/buscar.html") 



def EncontrarCalificacion(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        calificacion = Calificacion.objects.filter(NombreAlumno__icontains=patron)
        contexto = {"calificacion": calificacion}
        return render(request, "Aplicacion/Calificacion/calificacion.html", contexto)
    

    contexto = {'calificacion': Calificacion.objects.all()}
    return render(request, "Aplicacion/Calificacion/calificacion.html", contexto) 



#------------------------Login and Register-----------------------------

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "Aplicacion/Estetica/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AuthenticationForm()

    return render(request, "Aplicacion/Login , Logout y Registro/login.html", {"form": miForm} )

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('inicio'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "Aplicacion/Login , Logout y Registro/registro.html", {"form": miForm} )  



#------------------------------------Perfil y Avatar--------------------------------------

@login_required
def EditarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('inicio'))
    else:   
        miForm = UserEditForm(instance=usuario)

    return render(request, "Aplicacion/Avatar, Edicion y Clave/editarPerfil.html", {"form": miForm} ) 

@login_required
def SubirAvatar(request):
    if request.method == "POST":
        #Recupero los datos binarios y no binarios
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            #Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('inicio'))
    else:
        miForm = AvatarForm()

    return render(request, "Aplicacion/Avatar, Edicion y Clave/SubirAvatar.html", {"form": miForm} ) 


#-----------------------------------Cambio de contraseña------------------------------------

class CambiarClave(PasswordChangeView):
    template_name = "Aplicacion/Avatar, Edicion y Clave/cambiar_contraseña.html"
    success_url = reverse_lazy("inicio")









