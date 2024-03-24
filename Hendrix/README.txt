Proyecto: Hendrix

Autor: Mirko Recchi
Fecha: 24/03/2024
Versión: 1.0

Objetivo:

El objetivo principal de Hendrix es la Autogestion de alumnos para inscribirse como alumno de la facultad y poder anotarse a las mesas de los finales.
Ademas los profesores tendran acceso para colocar las notas de los alumnos como tambien subir examenes tomados en una fecha determinada.

Consideraciones:
Instalar django 4.2.5 

Modelos usuados:

- Alumnos: En este modelo se observan los datos del alumno , el nombre , apellido , legajo y comision.
- Comision: En este modelo se encuentran el numero de las comisiones con sus horarios correspondientes. El alumno debera elegir el horario que le convenga para el cursado.
- Materia: Las materias que el alumno cursara con sus respectivas correlatividades. 
- Cursado: Una vez elegido la comision , tendra que anotarse en cursado para poder cursar las materias antes mencionadas.
- Mesa: En este modelo el profesor ingresara atraves del formulario las fechas de los examenes finales con su horario.
- Examen: Una vez que el alumno decide presentarse a rendir un examen viendo las mesas disponibles (Modelo Mesa) tendra que anotarse a rendir indicando su nombre , profesor con quien curso la materia y su comision.
- Calificacion: En este apartado el profesor se encarga de subir las notas correspondientes del alumno que rindio la materia para que luego el alumno se dirija a buscar su nota subida al sistema. Contara con una "Lupa" para encontrar su calificacion.
- Modelo: Una vez rendido el examen en una fecha determinada , unicamente el profesor tomara la decision de subir el examen final tomado en esa fecha para que otros alumnos tengan una idea de lo que se tomo en esa mesa
- Avatar: La foto de perfil que el Usuario/Alumno/Profesor elige colocar para su perfil.


NOTA:
-Puede ser que un profesor de clases de varias materias a la vez 

Ejemplo:
-Norman da clases de AM I , AM II y asi sucesivamente


Pruebas:

Usuario para acceder al Administrador de Django:
Usuario: Hendrix
Contraseña: 16905859df

Profesores(con permisos):
Usuario: Norman
Contraseña: 16905859df

Usuario: Ramiro
Contraseña: 16905859df

Usuario: Andres
Contraseña: 16905859df

Alumno:
Usuario: Mirko
Contraseña: 16905859df

Video presentacion:
https://www.youtube.com/watch?v=E0MtTBPc2vg