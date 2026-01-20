# final.work.py
REST.API_maria_carmona
PAQUETES INSTALADOS
•	setpup tools 
a.	pip install setuptools
•	 Wheel
a.	pip install Wheel
•	 Flask y su conector mysql
a.	pip install flask flask_mysqldb
•	Para saber que tenemos instalado
a.	pip list 

CARPETAS CREADAS

1.CARPTERA CREADA DE VIRTUAL ENVIROMENT(ENV)
a.	python -m venv final_work-env
b.	source final_work.py-env/bin/actívate

2.CARPETA CREADA DE SOURCE 
Con este código escribiéndolo en la terminal creamos carpeta source.
 mkdir src
•	dentro de source creamos archivos (APP.PY / CONFIG.PY)

3.ARCHIVO REQUIEREMENTS 
se crea con el siguiente enlace escrita en la terminal pip freeze > requirements.txt (crea el archivo automáticamente)

CÓDIGO DE PROBAR EL PROYECTO
•	python . \src\app.py

4.GITINORE
En este archivo escribimos las partes de nuestro código que no queremos que se haga público

.env
venv
__pychache__/

Comandos: 
•	git init (nos confirma en color verde lo que se va a hacer público y color gris lo que no)
•	git st (status, nos devuelve nuestro estado)
•	git commit -m "my first commit"

IMPORTACIONES
from flask import FLASK
from flask_mysql import MYSQL
from config import config
from flask import jsonify
from flask import request

