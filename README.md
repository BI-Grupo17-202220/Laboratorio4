# Laboratorio4
Pasos para la ejecucion del API y el consumo de recursos
Ejecutar el api:
-Se debe asegurar que el ambiente tenga descargado todas las librerias a usar
-Se debe asegurar de tener la version 1.0.2 de skitlearn para que funcione
-Se recomienda altamente correr el programa desde el ambiente virtual Anaconda
-La ejecucion se realiza por terminal con el comando uvicorn main:app --reload
-En caso de que salga un error del tipo "no se puede encontrar uvicornm" Correr el siguiente comando: python -m uvicorn main:app --reload
Consumo de APIs:
Para acceder a la base se debe correr el programa con normalidad, sera lo primero que se ejecute
Para acceder a items, se debe agregar un endpoint en la ip de la forma /items/{item_id} para obtener el resultado buscado (probar /items/4) 
Para acceder al modelo predictivo hay que seguir una serie de pasos:
 -Primero se debe acceder al endpoint /docs/
 -Luego, se debe buscar el request de tipo post llamado predict
 -Al desplegarlo podemos ver un json y un recuadro con posibles resultados
 -Le das click al boton try out y este permitira editar el json
 -Tras ingresar los datos al json se le da al boton execute
 -Retorna el resultado predicho por el modelo
 Probar:{
  "serial_no":117 ,
  "gre_score": 299,
  "toefl_score": 102,
  "university_rating": 3,
  "sop": 4,
  "lor": 3.5,
  "cgpa": 8.62,
  "research": 0
} como posible input del json
