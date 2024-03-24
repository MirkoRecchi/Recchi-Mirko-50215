#----------------------Librerias------------------------------------
from django.urls import path , include
from .views import *
from django.contrib.auth.views import LogoutView
#-------------------------------------------------------------------


urlpatterns = [
    
  #---------------------------------------Menu Principal------------------------------------------------------------
  path('', inicio , name="inicio"),
  path('inicioprelogin/', prelogin , name="inicioprelogin"),
  path('acercademi/', acercademi , name="acercademi"),
  #-------------------------------------------Alumno-----------------------------------------------------------------
  path('alumno/', AlumnoList.as_view(template_name="Aplicacion/Alumno/alumno_list.html") , name="alumno"),
  path('alumno_create/', AlumnoCreate.as_view(template_name="Aplicacion/Alumno/alumno_form.html"), name="alumno_create"),
  path('alumno_update/<int:pk>/', AlumnoUpdate.as_view(template_name="Aplicacion/Alumno/alumno_form.html") , name="alumno_update"),
  path('alumno_delete/<int:pk>/', AlumnoDelete.as_view(template_name="Aplicacion/Alumno/alumno_confirm_delete.html") , name="alumno_delete"),
  #-------------------------------------------Cursado---------------------------------------------------------------
  path('cursado/', CursadoList.as_view(template_name="Aplicacion/Cursado/cursado_list.html") , name="cursado"),
  path('cursado_create/', CursadoCreate.as_view(template_name="Aplicacion/Cursado/cursado_form.html") , name="cursado_create"),
  path('cursado_update/<int:pk>/', CursadoUpdate.as_view(template_name="Aplicacion/Cursado/cursado_form.html") , name="cursado_update"),
  path('cursado_delete/<int:pk>/', CursadoDelete.as_view(template_name="Aplicacion/Cursado/cursado_confirm_delete.html") , name="cursado_delete"),
  #--------------------------------------------Examen---------------------------------------------------------------
  path('examen/', ExamenList.as_view(template_name="Aplicacion/Examen/examen_list.html") , name="examen"),
  path('examen_create/', ExamenCreate.as_view(template_name="Aplicacion/Examen/examen_form.html") , name="examen_create"),
  path('examen_update/<int:pk>/', ExamenUpdate.as_view(template_name="Aplicacion/Examen/examen_form.html") , name="examen_update"),
  path('examen_delete/<int:pk>/', ExamenDelete.as_view(template_name="Aplicacion/Examen/examen_confirm_delete.html") , name="examen_delete"),
  #----------------------------------------Calificacion--------------------------------------------------------------
  path('calificacion/', calificacion, name="calificacion"),
  path('calificacion_create/', calificacionCreate, name="calificacion_create"),
  path('calificacion_update/<id_calificacion>/', calificacionUpdate, name="calificacion_update"),
  path('calificacion_delete/<id_calificacion>/', calificacionDelete, name="calificacion_delete"),
  path('buscar_calificacion/', BuscarCalificacion, name="buscar_calificacion"),
  path('encontrar_calificacion/', EncontrarCalificacion, name="encontrar_calificacion"),
  #-------------------------------------------Mesa--------------------------------------------------------------------
  path('mesa/', MesaList.as_view(template_name="Aplicacion/Mesa/mesa_list.html") , name="mesa"),
  path('mesa_create/', MesaCreate.as_view(template_name="Aplicacion/Mesa/mesa_form.html") , name ="mesa_create"),
  path('mesa_update/<int:pk>/', MesaUpdate.as_view(template_name="Aplicacion/Mesa/mesa_form.html") , name="mesa_update"),
  path('mesa_delete/<int:pk>/', MesaDelete.as_view(template_name="Aplicacion/Mesa/mesa_confirm.delete.html") , name="mesa_delete"),
  #------------------------------------------Modelo---------------------------------------------------------------------
  path('modelo/', modelo, name="modelo"),
  path('SubirModelo/', SubirModelo , name="SubirModelo"),
  #----------------------------------Login , Logout and Register-------------------------------------------------------
  path('login/', login_request, name="login"),
  path('logout/', LogoutView.as_view(template_name="Aplicacion/Login , Logout y Registro/logout.html") , name="logout"),
  path('registro/', register, name="registro"),
  #------------------------------------Perfil , Clave y Avatar----------------------------------------------------------
  path('perfil/', EditarPerfil, name="perfil"),
  path('<int:pk>/password/', CambiarClave.as_view(),  name="cambiar_contraseña"),
  path('subir_avatar/', SubirAvatar, name="subir_avatar"),
  #-----------------------------------------Otras URLS------------------------------------------------------------------
  path('comision/', ComisionList.as_view(template_name="Aplicacion/Comision/comision_list.html") , name="comision"),
  path('materia/', MateriaList.as_view(template_name="Aplicacion/Materia/materia_list.html") , name="materia"),
]
