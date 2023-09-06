# API RESTful para gestion de Inventario de Librería

## Requerimientos iniciales

* [Python](https://www.python.org) Requerimientos necesarios.
```Python 3.11.3 o superior```

## Instalar Django.
[Install Django](https://docs.djangoproject.com/en/4.2/topics/install/#installing-official-release).

```bash
# Instalar Django en nuestra maquina.
$ python -m pip install Django
```

## Crear un proyecto.
[Documentación Djago](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
```bash
# Crear nuevo proyecto.
$ django-admin startproject 'Project-name'

# Crear apliación dentro de Django
$ python manage.py startapp 'new-model'
```

## Migraciones para la base de datos
[Database Django](https://docs.djangoproject.com/en/4.2/intro/tutorial02/)

<p>Por defecto, Django usa la configuracion de SQLite, la cual esta incluida en Python<p>

```bash
#Buscar Cambios para realizar migraciones
$ python manage.py makemigrations

#Realizar migraciones
$ python manage.py migrate
```

## Instalar RESF Framework para API
[Documentación Instalación Django REST Framework](https://www.django-rest-framework.org)
```bash
# Instalar Django REST Framework
$ pip install djangorestframework
```
## Instalar un entorno virtual para API RESTful
* Instalar un entorno virtual.

```bash
$ pip install virtualenv
```
* Instalar carpeta para entorno virtual
```bash
$ pip install virtualenv venv
```

