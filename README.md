Aimme Vivas, Cohort 5, Sprint 6

Proyecto Sprint 6: Automatización de Pruebas

Este proyecto tiene como objetivo la automatización de pruebas para diversas funcionalidades, incluyendo la creación de un kit y pruebas específicas del campo "name". Las pruebas se ejecutan a través de una lista de comprobación con casos diseñados para verificar las limitaciones de número de caracteres, espacios y caracteres especiale; en total se realizaron 9 pruebas 

Pasos a seguir para instalar Pytest

1. Decsargar Pycharm desde su página web oficial
2. Una vez instalado, creamos un nuevo proyecto
3. Al crear el proyecto, nos situamos en "Pyhton package" y buscamos "Pytest" e instalamos la última versión
4. En el mismo menú "Python package" debemos instalar "pip" y "request" en sus versiones más nuevas
5. Una vez instalado "Pytest" " Pip" y "Request" nos aparecerán en el meù "installed" de "Python package"
   

Pasos para Ejecutar las Pruebas

 1. Clonar el Proyecto con el siguiente còdigo: 
git clone git@github.com:Aimmevivas/qa-project-06-es.git
Nota: En mi caso enfrentè un problema al abrir el proyecto en PyCharm, ya que no lo encontraba en documentos, la soluciòn fue descargarlo en formato zip y descomprimirlo, para luego arrastrar el documento a Pycharm y poder abrirlo


2.Revisar nuevamente que esten Instalados los Requisitos Esenciales para las pruebas: 
pip, pytest, request

3.Configuración del proyecto
En el archivo "configuracion.py",del proyecto, me asegurè de actualizar la URL del servidor, las APIs correspondientes y la ruta del documento.

4.Almacenamiento de Datos de Solicitudes
Revisè la documentación de la API y completè los datos necesarios en el archivo "data.py"

5. Crear un Usuario
Utilizcè la API POST /api/v1/users para crear un usuario, y coloquè los sigueintes datos en "data.py"

{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}

6:  Crear un Kit y Realizar Pruebas
Utilicè la API POST /api/v1/kits para crear un kit y vincularlo al usuario. Coloquè los siguientes datos del kit en sender_stand_request.py:

}

kit_body = {
    "name": "Mi conjunto",
    "card": {
        "id": 1,
        "name": "Para la situación"
    },
    "productsList": 1,
    "id": 7,



Después, empecè a ejecutar las pruebas en el siguiente orden:

1: Especifiquè la función a probar.

2: Realicè pruebas negativas antes que las positivas.

3: Nombrè a la función negative_asserts para los casos negativos y positive_asserts para los casos positivos.

4: En el menù superior se selecciona la opciòn "Pytest" en el menú desplegable que se encuentra al lado de la flecha verde 

5: Una vez colocado en "Pytest" se puede correr la prueba, dando clic en la flecha verde

Resultados de las Pruebas
Las pruebas positivas fueron exitosas, mientras que las pruebas negativas, diseñadas para fallar, no pasaron la prueba.
4 pruebas fallaron, 5 pruebas pasaron 
