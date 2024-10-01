# **CLI Task Tracker**

## Descripción
CLI Task Tracker es una herramienta de línea de comandos para gestionar tareas de manera eficiente. El programa permite crear, actualizar, listar, mostrar y eliminar tareas mediante una interfaz CLI sencilla. Las tareas se almacenan en un archivo JSON.

## Características
  - Crear una nueva tarea: Proporciona un título, descripción y estado opcional para agregar una tarea.
  - Actualizar una tarea existente: Modifica los detalles de una tarea específica utilizando su ID.
  - Listar todas las tareas: Muestra todas las tareas almacenadas en un archivo JSON.
  - Mostrar una tarea por ID: Obtiene los detalles de una tarea en particular.
  - Eliminar una tarea: Elimina una tarea existente a partir de su ID.

## Instalación
  - 1 Clona este repositorio:
  ~~~
git clone https://github.com/lesterdavid31/CLI-Task-Tracker.git
cd CLI-Task-Tracker

  ~~~

  - 2 Crea un entorno virtual e instala las dependencias:

~~~
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate  # Windows
pip install -r requirements.txt

~~~

## Uso

  - 1 Crear una nueva tarea
Para crear una nueva tarea, utiliza el comando newTask con las opciones --title y --description. También puedes agregar el estado opcionalmente con --status:

~~~
py cli.py newTask --title "Aprender Django" --description "Completar el tutorial de Django" --status "in-progress"
~~~

  - 2 Listar todas las tareas
Para listar todas las tareas almacenadas, ejecuta:
~~~
py cli.py users
~~~

Este comando mostrará una lista de tareas con el formato:

~~~
Id: 1  -  Title: Aprender Python  -  Description: Completar conceptos básicos de Python  
- Status: in-progress  -  Create at: 2024-09-25  -  Update at: 2024-09-25

~~~

  - 3 Obtener una tarea por ID
Para obtener los detalles de una tarea específica, utiliza el comando getTask seguido del ID de la tarea:

~~~
py cli.py getTask 3
~~~

Salida:
~~~
Id: 3
Title: Aprender Django
Description: Completar el tutorial de Django
Status: in-progress
Created at: 2024-09-25
Update at: "Not update"
~~~

  - 4 Actualizar una tarea existente
Para actualizar una tarea, utiliza el comando update pasando el ID de la tarea y los nuevos valores de título, descripción o estado tambien actualiza el horario (puedes actualizar solo uno de estos campos o varios a la vez):

~~~
py cli.py update 3 --title "Aprender Flask" --description "Completar el tutorial de Flask" --status "completed"

~~~

Salida:
~~~
Id: 3
Title: Aprender Flask
Description: Completar el tutorial de Flask
Status: completed
Created at: 2024-09-25
Update at: 2024-09-25 10:20:50
~~~

  - 5 Eliminar una tarea
Para eliminar una tarea existente, utiliza el comando deleteTask pasando el ID de la tarea:

~~~
py cli.py deleteTask 3
~~~
Este comando elimina la tarea con el ID especificado.

## Estructura del proyecto
  - **cli.py**: Archivo principal que contiene los comandos y la lógica para la gestión de tareas.
  - **file.py**: Módulo que maneja la lectura y escritura de datos en un archivo JSON.
  - **data.json**: Archivo donde se almacenan las tareas en formato JSON.

### Contribuciones
  Las contribuciones son bienvenidas. Por favor, crea un issue o un pull request si tienes alguna sugerencia o mejora.

### Licencia
  Este proyecto está bajo la licencia MIT.




