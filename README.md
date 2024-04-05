librerias o plugins usados 

- https://tom-select.js.org/  (para la seleccion y busqueda en un formulario)

- https://www.chartjs.org/ (para los graficos estadisticos)

## PASOS PARA HACER PULL REQUEST

crear un fork del repositorio original , ya creado el fork hacer un git clone en tu pc local y poner los siguientes comandos 

````bash
git clone repositorio_forkeado
````

luego renombraremos nuestros upstream de nuestro repositorio

````bash
git remote rename origin fork
````

despues agregaremos el original del repositorio base 

````bash
git remote add origin https://github.com/BarretoPalacios/SAN_SEBASTIAN_PV.git
````

para visualizar nuestros upstreams remotos utilizamos el siguiente comando

````bash
git remote -v
````

ya con esto estamos listo para crear una nueva rama y cambiarnos a ella usamos el comando 
````bash
git checkout -b nueva-rama
````


ya creada nuestra rama hacemos los cambios necesarios 
````bash
git add .
````
````bash
git commit -m "comentario del commit"
````
````bash
git push fork nueva-rama
````

en la interfaz puede que te salga un boton color verde que te pida hacer el pull request 

![boton de pull](https://opensource.com/sites/default/files/uploads/compare-and-pull-request-button.png)


por si no sale iran a su repoitorio forkeado  en la seccion de pull request ,y crean una

![creacion de pull](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG45-NABixwgXhGTPaoSt0F4XIMUJuR-_It8fU8NQSlA&s)

con eso crear las pull y el admin la verificara


## BAJAR CAMBIOS DEL REPOSITORIO ORIGINAL

![sync](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcaxYiC-ggBsDsb3CQjOANSGfqO_Frask32g&s)

y el la bash de tu repositorio forkeado utilizas el git pull

````bash
git pull fork main
````
Rojas Vargas 

### por ahora esto es un ejemplo mejoraremos con el tiempo .....