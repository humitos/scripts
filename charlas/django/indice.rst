---------------------
Introducción a Django
---------------------

Resumen: ``En esta charla se verán los conceptos básicos de Django, desde
         la instalación hasta la confección de un blog muy muy simple. Se
         explicará el patrón MVC y como se utiliza este en Django, el
         matcheo de urls, la definición de una vista y su interacción con
         los templates``

Nivel: ``Bajo-Medio``

Conocimientos previos: ``Mínimos conocimientos en Python``

Disertante: ``Manuel Kaufmann``

Email: ``humitos@gmail.com``

Teléfono: ``0343 - 154053434
            0342 - 4598908``

Localidad: ``Santa Fe - Capital``

Organizaciones: ``Python Argentina``

Blog: ``http://humitos.wordpress.com``

Índice de contenidos
====================

 * Qué es Django?
   * Para que se utiliza?
   * Historia

 * Patron de diseño MVC
   * Modelo
   * Vista
   * Controlador

   MTV -> Model Template Views

 * Instalación
   * Muy por arriba

 * Comenzar un proyecto
   * Ejemplo
   * Mostrar que inicia algo
   * Explicaciones de los archivos
     * __init__.py
     * settings.py
     * urls.py

 * Mapear URL's
   * Expresiones regulares
   * Argumentos en las URL's
   * Funcion de Python o cadena de caracteres
     * La funcion debe devolver un HttpResponse

 * Crear una aplicacion
   * ¿Qué es una aplicacion? Usos
   * Ejemplo
     * python manage.py startapp pools
     * __init__.py
     * models.py
     * views.py

 * Modelos
   * Definición de los modelos.
   * Campos y relaciones.
   * ABM en el sistema de administración (admin.py).

 * Vistas
   * Definir una vista
   * Escribir la url
   * Pasar argumentos (FALTA)

 * Sistema de plantillas
   * Contexto (argumentos)
   * Herencia (plantilla base) - extends/block/endblock
   * render_to_response (shortcuts)
   * Etiquetas (if, for, etc..) forloop, ifequal
   * Filtros (lower, truncatewords, con argumentos)
   * Extención... definir un filtro y una etiqueta
     * Mencionarlo

   * TEMPLATE_DIRS (en settings)

 * Sistema de Administracion
   * ABM autogenerado
   * Modificaciones
   * admin.py


