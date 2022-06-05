# Prueba Técnica 
* Prueba técnica realizada para la empresa Tangelo
## Stack 

* Python 
* Pandas
* SQLite

## Requerimientos para la prueba
 
 ![alt](https://user-images.githubusercontent.com/62122521/172021432-7a38dce8-d48f-4bf2-98f2-3fb8fd625aa1.png)

* Desarrolle una aplicación en python que genere la tabla anterior teniendo las siguientes consideraciones:

  * De https://restcountries.com/ obtenga el nombre del idioma que habla el país y encriptelo con SHA1. 

  * Para esta prueba se requirie solo la región de **Africa** y el pais **Angola**.

  * En la columna Time ponga el tiempo que tardó en armar la fila (debe ser automático).

  * La tabla debe ser creada en un DataFrame con la librería PANDAS. 

  * Con funciones de la librería pandas muestre el tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo en procesar todas las filas de la tabla.

  * Guarde el resultado en sqlite.

  * Genere un Json de la tabla creada y guárdelo como data.json.

* La prueba debe ser entregada en un repositorio git.

  * Es un plus si:
    * No usa framework
    * Entrega Test Unitarios
    * Presenta un diseño de su solución

## Diagrama de solución 

![alt](https://user-images.githubusercontent.com/62122521/172021888-5dc99775-7e42-4946-a513-5c1cead90c9f.jpg)

## Pre requisitos
Es necesario contar con SQLite en local, se recomienda contar con una herramienta para poder visualizar en una interfaz la base de datos, recomiendo usar  DB Browser for SQLite(https://sqlitebrowser.org/).

## Ejecutar en local
Para ejecutar en local descargue o clone el proyecto, después de haber clonado o descargado habrá el proyecto en su editor de código, originalmente se desarrollo en VS.
Ejecute los siguientes comandos:

    pip install -r requirements.txt

    python3 app.py
## Ejecutar Test
Para ejecutar las pruebas unitarias establecidas, ejecute el archivo test_countries.py para que corran las pruebas establecidas, es necesario contar con el archivo mock_countries.py ya que se requiere para las pruebas

    pytest test_countries.py