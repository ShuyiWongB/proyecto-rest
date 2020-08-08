# API REST
Trabajo de Computación Paralela

### Lenguaje y Librerias necesarias

#### Lenguaje

* Python 3.8
_Descargar python desde la pagina oficial o desde su terminal y revisar la version_

```
python --version
```

#### Librerias

* Flask

```
pip install flask
```

* Flask_HTTPAuth

```
pip install flask-httpauth
```

* Flask_CORS

```
pip install flask-cors
```

### Rutas y Metodos

_Ruta para buscar UNA carrera dependiendo de su codigo unico_
```
/carrera/<codigo> 
METODO GET
```

_Ruta para buscar todas las carreras que tengan una palabra en comun_
```
 /carreras/<nombre> 
METODO GET
```

_Ruta para mostrar las diez mejores carreras que puede postular un estudiante_
```
/topcarreras 
METODO POST - Request Body formato JSON
```

### Usuarios autorizados

```
user1
rest1
```

```
user2
rest2
```

```
user3
rest3
```

### Autores
* Janira Navarro
* Sion-jei Mamani
* Shu-yi Wong
