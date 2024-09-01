## Configuración de contenedor virtual
```py -m venv venv ```(Crea el entorno virtual)
```.\venv\scripts\activate``` (Activar el contenedor(windows))
```pip install django``` (Instalación del paquete dentro de nuestro contenedor)

## creación del proyecto
 ```django-admin startproject djangcrud .``` (el punto es para que no nos haga otra carpeta dentro de nuestra carpeta)
 ```python manage.py runserver``` (levantar nuestro django)

 ## Creación de mi aplicación tasks
 ``` python manage.py startapp tasks ```