from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/contactos/<id>')
def lista_contactos(id):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT * id, nombre, phone, email FROM contactos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        contactos=[]
        for fila in datos:
            contacto={'id':fila[0], 'nombre':fila[1], 'phone':fila[2], 'email':fila[3]}
            contactos.append(contacto)
        return jsonify({'contactos': contactos, 'mensaje':"Contactos listados."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})
    
@app.route('/contactos/<id>', methods=['GET'])
def leer_contacto(id):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT id, nombre, phone, email FROM contactos WHERE id = '{0}".format(id)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            contacto = {'id': datos[0], 'nombre': datos[1], 'phone': datos[2], 'email': datos[3]}
            return jsonify({'contacto': contacto, 'mensaje': "Contacto encontrado."})
        else: 
            return jsonify({'mensaje': "Contacto no encontrado"})
    except Exception as ex:
            return jsonify({'mensaje': "Error"})

@app.route('/contactos/<id>', methods=['POST'])
def crear_contacto():
    # print(request.json)
    try: 
        cursor = conexion.connection.cursor()
        sql="""INSERT INTO contacto(id, nombre, phone, email) VALUES ('{0}', '{1}', '{2}', 
        '{3}')""".format(request.json['id'], request.json['nombre'], request.json['phone'], 
        request.json['email'])
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción de insercción
        return jsonify({'mensaje': "Contacto registrado."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/contactos/<id>', methods=['PUT'])
def actualizar_contacto(id):
    try: 
        cursor = conexion.connection.cursor()
        sql= """UPDATE contacto SET nombre = '{0}', phone = '{1}', email = '{2}' WHERE 
        id = {3}""".format(request.json['nombre'], request.json['phone'], request.json['email'], id)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción de insercción
        return jsonify({'mensaje': "Contacto actualizado."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

@app.route('/contactos/<id>', methods=['DELETE'])
def eliminar_contacto(id):
    try: 
        cursor = conexion.connection.cursor()
        sql= "DELETE FROM contacto WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        conexion.connection.commit() #Confirma la acción de insercción
        return jsonify({'mensaje': "Contacto eliminado."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

 
def pagina_no_encontrada(error):
    return "<H1> La página que intentas buscar no existe...<H1>", 404
    
class DevelopmentConfig():
   DEBUG = True
   MYSQL_HOST = 'localhost'
   MYSQL_USER = 'root'
   MYSQL_PASSWORD = 'Dax070385'
   MYSQL_DB = 'clínica_odontológica'

config = {
    'development': DevelopmentConfig,
}

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
    