==========================================
Introducción a Django_
==========================================

:Author: Manuel Kaufmann
:Contact: humitos@gmail.com
:Revision: 29
:Date: jue sep 11 22:17:12 ART 2008
:Copyright: GNU Free Document License


¿Qué es Django?
---------------

Django es un ``framework`` de alto nivel hecho en Python_ para el desarrollo de
páginas web y a su vez fomenta el desarrollo de aplicaciones rápidas y limpias.
Este framework nos permite preocuparnos únicamente por las partes específicas
de nuestro sitio web en vez de las tareas comunes y repetitivas de cualquier
sitio, como pueden ser, autenticación, permisos, sesiones, formularios,
listados, etc.

¿Para qué se utiliza?
~~~~~~~~~~~~~~~~~~~~~

Django permite ser utilizarlo para el desarrollo de un blog, una encuesta, o
hasta un ``sistema completo`` sin tener ningún tipo de inconveniente y
facilitando mucho el trabajo. La abstracción que posse en cuanto a las tareas
comunes permite un rápido diseño como así también su desarrollo.

Historia
~~~~~~~~

Django nace por una necesidad. En el año 2003, programadores del diario
``Lawrence Journal-World``, Adrian Holovaty y Simon Willison recibían por parte de
los periodístas muchos pedidos de modificaciones del sitio con muy poco previo
aviso pero sí con fechas límites.

En el verano del 2005, luego de haber desarrollado el framework hasta que haga
funcionar la mayoría de los sitios, el equipo, que ahora incluía a Jacob
Kaplan-Moss decidió liberar este framework como software de código abierto. El
nombre Django viene por el guitarrista de jazz Django Reinhardt.

Patrón de diseño MVC
--------------------

Es un patrón de arquitectura de software que separa los datos de una
aplicación, la interfaz de usuario, y la lógica de control en tres componentes
distintos. El patrón MVC se ve frecuentemente en aplicaciones web, donde la
vista es la página HTML y el código que provee de datos dinámicos a la página,
el modelo es el Sistema de Gestión de Base de Datos y la Lógica de negocio y el
controlador es el responsable de recibir los eventos de entrada desde la vista.

    Wikipedia_

Aunque esta definición es bien clara, Django cambia un poco la sigla y utiliza
MTV para describir su patrón de diseño, significando Models Templates Views. En
dónde la anología sería Models-Models, Templates-Views y Views-Controler
comparado con la anterior definición.

Modelo (models.py)
~~~~~~~~~~~~~~~~~~

Este archivo contiene la descripción de las tablas para una aplicación,
definidas como clases de Python. Usando estas clases de Python se pueden crear,
buscar, actualizar y borrar entradas de la base de datos usando código Python
en vez de sentencias SQL.

Vista (views.py)
~~~~~~~~~~~~~~~~

En él se encuentra toda la lógica que se necesita para mostrar los resultados
en la pantalla. Por ejemplo, procesar un ingreso de datos proveniente del
usuario. A cada una de estas funciones se las llama ``vista``.

Plantillas (index.html)
~~~~~~~~~~~~~~~~~~~~~~~

Las plantillas son simplemente código ``HTML`` el cual describe el aspecto que
tendrá nuestra página al ser renderizada por el navegador. Además se puede
escribir en el lenguaje de plantillas de Django para realizar algunas cosas
especiales.

Instalación
-----------

::

    [humitos]$ wget -c http://www.djangoproject.com/download/1.0/tarball/
    [humitos]$ tar xzvf Django-1.0.tar.gz
    ......
    [humitos]$ cd Django-1.0
    [humitos]$ sudo python setup.py install

Prueba
~~~~~~

::

    [humitos]$ python
    Python 2.5.2 (r252:60911, Aug  6 2008, 09:17:29)
    [GCC 4.3.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>> django.VERSION
    (1, 0, 'final')
    >>>

Comenzar un proyecto
--------------------

::

    [humitos]$ django-admin.py startproject blog
    [humitos]$ ls blog/
    __init__.py  manage.py  settings.py  urls.py
    [humitos]$ python manage.py runserver

¡Ya está! Ahora si vamos a un navegador web y en la url ponemos
http://localhost:8000 veremos que Django nos muestra la página de bienvenida:
``It worked!``.

Anteriormente vimos que al ejecutar ``startproject`` Django nos crea cuatro
archivos de Python:

    * ``___init___.py``: es un archivo requerido por Python para indicarle que
      trate a este directorio como un paquete (conjunto de módulos).

    * ``manage.py``: utilidad de línea de comandos para interactuar con el
      proyecto de Django creado anteriormente.

    * ``settings.py``: archivo de configuraciones para el proyecto actual,
      entre ellas idioma, base de datos, etc.

    * ``urls.py``: aquí se encuentran las declaraciones de las urls del sitio
      web que estamos desarrollando.

Mapear URL's
------------

Django concuerda cada url que se escribe en el navegador con una función vista,
de tal manera que al acceder a un determinado lugar del sitio se llame a la
función que nosotros indicamos. Esto se hace mediante expresiones regulares, en
comparación con otros frameworks que es de acuerdo a la estructura de los
directorios.

Expresiones Regulares
~~~~~~~~~~~~~~~~~~~~~

Este mapeo del que hablamos se indica mediante expresiones regulares, lo que
nos permite tener el control absoluto sobre las url y poder hacer fácilmente lo
que queramos: restringir una url a que contenga cierta cantidad de números
en un lugar predeterminado, por ejemplo.

Django además nos permite utilizar grupos (nombrados o no) en las expresiones
regulares, que luego serán pasados como argumento a nuestra función vista. Si
utilizamos grupos nombrados, no importa el orden de los argumentos en la
definición de la función, pero por el contario, el primer argumento será el
primer grupo que aparezca en la expresión regular.

Funcion para la url
~~~~~~~~~~~~~~~~~~~

La forma de indicarle a Django cual es la función vista que debe utilizar para
cada una de las urls que queramos es pasarle una cadena de caracteres con la
ruta para llegar a esta función (en sintaxis de Python) o bien pasarle
diréctamente el objeto función que queremos. Cada una de estas vistas debe
devolver un objeto HttpResponse.

Crear una aplicación
--------------------

¿Qué es una aplicación?
~~~~~~~~~~~~~~~~~~~~~~~

Una aplicación es un conjunto de archivos de código fuente de Python,
incluyendo sus propios modelos y vista y que se encuentran agrupados en un
mismo paquete. Por otro lado, un proyecto es un conjunto de aplicaciones, el
cual establece las configuraciones globales para cada una de ellas, por ejemplo
la conexión a la base de datos.

Lo bueno de tener separadas las distintas aplicaciones, es que luego se pueden
reutilizar sin modificar nada en el código ya que las cosas que están
relacionadas con el proyecto no se encuentran dentro de estas. Django viene con
una cantidad de aplicaciones listas para usar, entre ellas, el sistema de
administración.

Ejemplo
~~~~~~~

::

    [humitos]$ python manage.py startapp posts

Notar que utilizamos ``manage.py`` en vez de ``django-admin.py``. Estos
archivos tiene una funcionabilidad muy similar, pero utilizando el primero nos
evitamos tener que indicarle la ruta del proyecto que queremos utilizar.

Luego de ejecutar esta senticia se crea un directorio ``posts`` con tres
archivos: ``__init__.py``, ``models.py`` y ``views.py``, que son los mismos que
explicamos anteriormente pero para esta aplicación específica. Todos se
encuentran vacíos y es dónde pondremos el código que corresponda en cada caso.

Modelos
-------

Los modelos hacen referencia a todo lo que esté relacionado con la base de
datos. En cada una de las aplicaciones definimos las clases (tablas en SQL)
necesarias para que esta aplicación pueda funcionar correctamente.

Configuración del motor
~~~~~~~~~~~~~~~~~~~~~~~

Como la elección del motor de base de datos a utilizar es una configuración a
nivel de proyecto, necesitamos indicar esto en el archivo ``settings.py`` que
nos creó Django al momento de iniciar el proyecto.

En este archivo se encuentra una sección con campos similares a estos::

    DATABASE_ENGINE = ''
    DATABASE_NAME = ''
    DATABASE_USER = ''
    DATABASE_PASSWORD = ''
    DATABASE_HOST = ''
    DATABASE_PORT = ''

En donde se puede indicar el nombre del motor a utilizar, nombre de la base de
datos, nombre del usuario, contraseña y demás. En caso de utilizar SQLite hay
que indicar únicamente el campo ``DATABASE_NAME`` con un path al archivo en el
disco. Para empezar y también para proyectos chicos es recomendable utilizar
este motor, ya que es sencillo de configurar y no requiere módulos extras.

Definición de modelos
~~~~~~~~~~~~~~~~~~~~~

Para crear un modelo debemos editar el archivo ``models.py`` de la aplicación
que necesite de estos. En principio vamos a crear la tabla ``post`` definiendo
una clase en el archivo de esta aplicación::

    from django.db import models

    class Post(models.Model):
        titulo = models.CharField(max_length=50)
        contenido = models.TextField()
        etiquetas = models.ManyToManyField(Etiqueta)

Definimos una clase ``Post`` que contendrá un *título* y será un string de
longitud máxima igual a 50, un campo *contenido* que será un string largo al
cual luego el administrador lo representará como un ``<textarea>`` (entrada
multilínea) en el que se guardará el contenido mismo del post y *etiquetas*
que establece una relación muchos a muchos con ``Etiqueta``.

Ahora definamos los modelos ``Etiqueta`` y ``Comentario``::

    class Etiqueta(models.Model):
        nombre = models.CharField(max_length=25)

    class Comentario(models.Model):
        autor = models.CharField(max_length=25)
        contenido = models.TextField()
        post = models.ForeignKey(Post)

Una vez que tenemos esto creado en el modelo, lo que resta es instalar esta
nueva aplicación en el proyecto y sincronizar la base de datos con el
modelo. Para la instalación, editamos el archivo ``settings.py`` y agregamos
nuetra aplicación a la variable ``INSTALLED_APPS`` que no es más que una tupla
de strings::

    INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'blog.posts',
    )

Lo que resta entonces es sincronizar la base de datos, para esto se debe
ejecutar la siguiente sentencia de línea de comandos::

    [humitos]$ python manage.py syncdb

En este momento nos pregunta si queremos crear una cuenta para el
administrador, luego nos pedirá un email y su password. Una vez que este
comando finalice tendremos creadas nuestras tablas.

Prueba
~~~~~~

::

    [humitos]$ python manage.py shell
    Python 2.5.2 (r252:60911, Aug  6 2008, 09:17:29)
    [GCC 4.3.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from posts.models import Post
    >>> Post.objects.all()
    []
    >>> p = Post(titulo='Hola Mundo!', contenido='Hola a todos, este es mi primer post')
    >>> p.save()
    >>> Post.objects.all()
    [<Post: Post object>]
    >>>

Lo que acabamos de hacer es insertar en el modelo un nuevo objeto post, con
título *Hola Mundo!* y un contenido. Además no se encuentra relacionado con
ninguna etiqueta. Una vez guardado el objeto, consultamos nuevamente la base de
datos y nos dice que se encuetra un Post como resultado.


Sistema de Administración
~~~~~~~~~~~~~~~~~~~~~~~~~

Django trae consigo una aplicación muy interesante: el sistema de
administración. Éste nos permite agregar, quitar y modificar usuarios con un
enterno web muy agradable y sencillo. Por ejemplo podemos probar lo que hicimos
en la sección anterior únicamente haciendo clicks.

Primero se debe ``instalar`` la aplicación en Django por lo que las
aplicaciones instaladas quedarían así::

    INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'blog.posts',
    )

Luego hay que sincronizar nuevamente la base de datos, ya que el sistema de
administración tiene sus propias tablas. Si no estamos seguros qué va a suceder
antes de ejecutar ``syncdb`` lo podemos comprobar utilizando este comando::

    [humitos]$ python manage.py sql admin
    BEGIN;
    CREATE TABLE "django_admin_log" (
        "id" integer NOT NULL PRIMARY KEY,
        "action_time" datetime NOT NULL,
        "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
        "content_type_id" integer NULL REFERENCES "django_content_type" ("id"),
        "object_id" text NULL,
        "object_repr" varchar(200) NOT NULL,
        "action_flag" smallint unsigned NOT NULL,
        "change_message" text NOT NULL
    )
    ;
    COMMIT;

Una vez que estamos seguro que es esto lo que queremos hacer, ejecutamos estas
sentencias con el comando ``syncdb``::

    [humitos]$ python manage.py syncdb
    Creating table django_admin_log
    Installing index for admin.LogEntry model

Descomentamos las líneas del archivo ``urls.py``::

    from django.contrib import admin
    admin.autodiscover()
    ...
    (r'^admin/(.*)', admin.site.root),

Ahora accediendo a la dirección http://localhost:8000/admin nos debe mostrar
una pantalla de login. Si indicamos el nombre de usuario y la contraseña que
pusimos al crear el proyecto deberíamos poder ingresar al sitio de
administración.

En este momento aún no aparecen nuestra aplicaciones que hemos creados, le
tenemos que indicar a Django que deseamos que las muestre. Para esto basta con
crear un archivo ``admin.py`` dentro de la aplicación que queremos mostrar, en
este caso ``posts``::

    from blog.posts.models import Post
    from django.contrib import admin

    admin.site.register(Post)

Vistas
------

Una función de vista no es más que una función de Python que recibe como
argumento una petición web y retorna una respuesta web. Esta respuesta puede
ser código HTML, una imágen, un archivo de texto, o cualquier otra cosa.

Al estar separadas las aplicaciones cada una de estas pueden tener lsa vistas
que necesite, al igual que ocurría con los modelos. En este caso vamos a hacer
la vista para agregar un nuevo post al blog::

    from django.shortcuts import render_to_response
    from django.http import HttpResponseRedirect
    from django.forms import ModelForm
    from blog.posts.models import PostForm, Post

    def agregar_post(request):
        if request.method == 'GET':
            formulario = PostForm()
            return render_to_response('agregar_post.html', {'formulario': formulario})
        else:
            formulario = PostForm(request.POST)
            if formulario.is_valid():
                formulario.save()
            return HttpResponseRedirect('/')

Quedaría modificar el archivo ``urls.py`` para que cuando se ingrese a
http://localhost:8000/posts/agregar se ejecute la vista que acabamos de
definir. Una vez hecho esto al ingresar a esta dirección se presenta un
formulario para completar con los campos del modelo Post. Al presionar el
botón se guarda este formulario en el modelo y se redirecciona a la página
principal del blog.

Sistema de plantillas
---------------------



.. _Django: http://www.djangoproject.com
.. _Python: http://www.python.org
.. _Wikipedia: http://www.wikipedia.com.ar
