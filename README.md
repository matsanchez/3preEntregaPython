# 3° Pre-Entrega Proyecto Final

## Ecommerce

## Comenzamos:

### Ejecutar el proyecto:

Para ejecutar el proyecto, el mismo puede descargarse como .zip o git clone

[Clic aqui para descargar repo formato zip](https://github.com/matsanchez/preEntregaPython/archive/refs/heads/main.zip)

Copiar y pegar en la terminal :

```
git clone https://github.com/matsanchez/3preEntregaPython.git

```

> Instalar las dependencias:
Cuenta con un archivo donde estan las dependencias usadas "requeriments.txt.
Ejecutar el siguiente comando dentro de la carpeta raiz TercerEntregaProyecto
```
pip install -r requirements.txt
```

> Modos de ejecucion Local:
>
> > Nos ubicamos en la carpeta principal de la app llamada project, dentro de la misma vamos a ejecutar el siguiente comando en el entorno virtual de python

```
python manage.py runserver
```

Si todo sale bien, nos informara que podemos visitar el sitio en la siguiente direccion por defecto http://127.0.0.1:8000/, chequeen igual en su terminal, que direccion le informa donde esta corriendo el servidor.

## Pruebas de desarrollo:



 Ingresando en http://127.0.0.1:800/admin .
 Obtendran acceso con usuario y contraseña al panel administrativo de django.

La pagina cuenta con las siguientes funcionalidades.

Si bien, desde la navegabilidad de la pagina podran recorrer la seccion del home, clientes, productos y contacto desde el navbar, como tambien cuenta con un buscador tanto en la seccion clientes, como productos, la misma funcionalidad esta en version beta y solo reacciona a la busqueda por nombre unicamente.

Tambien de modo "administrador" podran ingresar en:

http://127.0.0.1:800/cliente/crear
Desde esta vista, podran crear nuevos clientes completando los campos y quedaran guardardos en la base de datos.

http://127.0.0.1:800/producto/crear
Tambien podran crear productos completando todo los campos del formulario, los mismos tambien quedan guardados en la base de datos.


Desarrollo en su version beta por Matias Sanchez.