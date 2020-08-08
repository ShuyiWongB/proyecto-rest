from flask import Flask, request, jsonify, abort, make_response, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
auth = HTTPBasicAuth()
"""SE INICIALIZA LA EXTENSION CORS DE MANERA PREDETERMINADA PARA ṔERMITIR CORS EN TODAS LAS RUTAS"""
cors = CORS(app)
"""
    USUARIOS PARA INGRESAR CON SU RESPECTIVA CONTRASEÑA
"""
users = {
    'user1': generate_password_hash("rest1"),
    'user2': generate_password_hash("rest2"),
    'user3': generate_password_hash("rest3"),
}
"""
    VERIFICACION DE LOS USUARIOS
"""


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    else:
        abort(401)


"""
    ERRORES
"""
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error 400': 'No se puede procesar la solicitud, ingrese datos correctamente'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error 404': 'El recurso solicitado no existe'}), 404)

@app.errorhandler(401)
def not_authorized(error):
    return make_response(jsonify({'Error 401': 'No tiene autorizacion para realizar esta accion'}), 401)

@app.errorhandler(405)
def not_method(error):
    return make_response(jsonify({'Error 405': 'Metodo incorrecto'}), 405)

"""
    RUTA PRINCIPAL
"""


@app.route('/')
@auth.login_required
def index():
    return "Bienvenid@ a la API Rest"


"""
    TODA LA INFORMACION DE LAS CARRERAS
"""
carreras = [
    {'codigo': 21089, 'nombre': 'Administracion Publica', 'nem': 15, 'ranking': 20, 'lenguaje': 30, 'matematica': 25,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 35.0, 'primer matriculado 2019': 625.8,
     'ultimo matriculado 2019': 513.0},
    {'codigo': 21047, 'nombre': 'Arquitectura', 'nem': 15, 'ranking': 25, 'lenguaje': 20, 'matematica': 20,
     'ciencias o historia': 20, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 100.0, 'primer matriculado 2019': 640.2,
     'ultimo matriculado 2019': 527.4},
    {'codigo': 21046, 'nombre': 'Bachillerato en Ciencias de la Ingeniería', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 25.0, 'primer matriculado 2019': 586.45,
     'ultimo matriculado 2019': 504.25},
    {'codigo': 21002, 'nombre': 'Bibliotecologia y Documentacion', 'nem': 20, 'ranking': 20, 'lenguaje': 40,
     'matematica': 10, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 35.0, 'primer matriculado 2019': 675.3,
     'ultimo matriculado 2019': 453.6},
    {'codigo': 21012, 'nombre': 'Contador Publico y Auditor', 'nem': 20, 'ranking': 20, 'lenguaje': 30,
     'matematica': 15, 'ciencias o historia': 15, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 80.0, 'primer matriculado 2019': 635.55,
     'ultimo matriculado 2019': 452.2},
    {'codigo': 21071, 'nombre': 'Dibujante Proyectista', 'nem': 10, 'ranking': 25, 'lenguaje': 20, 'matematica': 35,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 25.0, 'primer matriculado 2019': 689.85,
     'ultimo matriculado 2019': 496.45},
    {'codigo': 21024, 'nombre': 'Diseño en Comunicacion Visual', 'nem': 10, 'ranking': 40, 'lenguaje': 30,
     'matematica': 10, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 100.0, 'primer matriculado 2019': 706.3,
     'ultimo matriculado 2019': 440.2},
    {'codigo': 21023, 'nombre': 'Diseño Industrial', 'nem': 10, 'ranking': 40, 'lenguaje': 30, 'matematica': 10,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 65.0, 'primer matriculado 2019': 642.2,
     'ultimo matriculado 2019': 439.9},
    {'codigo': 21073, 'nombre': 'Ingenieria en Biotecnologia', 'nem': 15, 'ranking': 25, 'lenguaje': 20,
     'matematica': 30, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 60.0, 'primer matriculado 2019': 675.8,
     'ultimo matriculado 2019': 540.9},
    {'codigo': 21075, 'nombre': 'Ingenieria Civil Electronica', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 80.0, 'primer matriculado 2019': 657.35,
     'ultimo matriculado 2019': 500.65},
    {'codigo': 21049, 'nombre': 'Ingenieria Civil en Ciencia de Datos', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 60.0, 'primer matriculado 2019': 673.65,
     'ultimo matriculado 2019': 539.35},
    {'codigo': 21041, 'nombre': 'Ingenieria Civil en Computación, mención Informática', 'nem': 10, 'ranking': 25,
     'lenguaje': 20, 'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 130.0, 'primer matriculado 2019': 673.65,
     'ultimo matriculado 2019': 539.35},
    {'codigo': 21096, 'nombre': 'Ingenieria Civil en Mecánica', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 90.0, 'primer matriculado 2019': 697.65,
     'ultimo matriculado 2019': 506.8},
    {'codigo': 21074, 'nombre': 'Ingenieria Civil en Obras Civiles', 'nem': 20, 'ranking': 20, 'lenguaje': 15,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 100.0, 'primer matriculado 2019': 625.0,
     'ultimo matriculado 2019': 476.1},
    {'codigo': 21087, 'nombre': 'Ingenieria Civil en Prevencion de Riesgos y Medioambiente', 'nem': 15, 'ranking': 35,
     'lenguaje': 20, 'matematica': 20, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 30.0, 'primer matriculado 2019': 615.2,
     'ultimo matriculado 2019': 462.85},
    {'codigo': 21076, 'nombre': 'Ingenieria Civil Industrial', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 200.0, 'primer matriculado 2019': 671.25,
     'ultimo matriculado 2019': 500.85},
    {'codigo': 21048, 'nombre': 'Ingenieria Comercial', 'nem': 10, 'ranking': 20, 'lenguaje': 30, 'matematica': 30,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 125.0, 'primer matriculado 2019': 652.9,
     'ultimo matriculado 2019': 496.9},
    {'codigo': 21015, 'nombre': 'Ingenieria en Administracion Agroindustrial', 'nem': 10, 'ranking': 20, 'lenguaje': 30,
     'matematica': 30, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 30.0, 'primer matriculado 2019': 628.8,
     'ultimo matriculado 2019': 461.8},
    {'codigo': 21081, 'nombre': 'Ingenieria en Comercio Internacional', 'nem': 10, 'ranking': 20, 'lenguaje': 30,
     'matematica': 30, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 90.0, 'primer matriculado 2019': 637.2,
     'ultimo matriculado 2019': 458.8},
    {'codigo': 21032, 'nombre': 'Ingenieria en Construccion', 'nem': 20, 'ranking': 20, 'lenguaje': 15,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 100.0, 'primer matriculado 2019': 716.3,
     'ultimo matriculado 2019': 476.95},
    {'codigo': 21031, 'nombre': 'Ingenieria en Geomensura', 'nem': 10, 'ranking': 25, 'lenguaje': 20, 'matematica': 35,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 60.0, 'primer matriculado 2019': 614.3,
     'ultimo matriculado 2019': 487.85},
    {'codigo': 21082, 'nombre': 'Ingenieria en Gestion Turistica', 'nem': 10, 'ranking': 20, 'lenguaje': 30,
     'matematica': 30, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 25.0, 'primer matriculado 2019': 659.4,
     'ultimo matriculado 2019': 448.1},
    {'codigo': 21039, 'nombre': 'Ingenieria en Industria Alimentaria', 'nem': 15, 'ranking': 25, 'lenguaje': 20,
     'matematica': 30, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 30.0, 'primer matriculado 2019': 680.2,
     'ultimo matriculado 2019': 464.9},
    {'codigo': 21030, 'nombre': 'Ingenieria en Informatica', 'nem': 10, 'ranking': 25, 'lenguaje': 20,
     'matematica': 35, 'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 105.0, 'primer matriculado 2019': 705.15,
     'ultimo matriculado 2019': 507.75},
    {'codigo': 21080, 'nombre': 'Ingenieria en Quimica', 'nem': 10, 'ranking': 25, 'lenguaje': 15, 'matematica': 30,
     'ciencias o historia': 20, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 80.0, 'primer matriculado 2019': 606.55,
     'ultimo matriculado 2019': 451.7},
    {'codigo': 21045, 'nombre': 'Ingenieria Industrial', 'nem': 10, 'ranking': 25, 'lenguaje': 20, 'matematica': 35,
     'ciencias o historia': 10, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 60.0, 'primer matriculado 2019': 584.75,
     'ultimo matriculado 2019': 476.25},
    {'codigo': 21083, 'nombre': 'Quimica Industrial', 'nem': 10, 'ranking': 25, 'lenguaje': 15, 'matematica': 30,
     'ciencias o historia': 20, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 40.0, 'primer matriculado 2019': 596.05,
     'ultimo matriculado 2019': 472.0},
    {'codigo': 21043, 'nombre': 'Trabajo Social', 'nem': 20, 'ranking': 30, 'lenguaje': 20, 'matematica': 10,
     'ciencias o historia': 20, 'puntaje minimo entre lenguaje y matematica': 450,
     'puntaje minimo ponderado': "No tiene", 'vacantes': 95.0, 'primer matriculado 2019': 705.9,
     'ultimo matriculado 2019': 510.5}
]


"""
    FUNCION PARA MOSTRAR PUBLICAMENTE UNA CARRERA
"""


def make_public_carrera(carrera):
    new_carrera = {}
    for field in carrera:
        if field == 'codigo':
            new_carrera['url'] = url_for('get_carrera', carrera_codigo=carrera['codigo'],
                                         _external=True)
        else:
            new_carrera[field] = carrera[field]
    return new_carrera

"""
    RUTA PARA VER LA INFORMACION DE TODAS LAS CARRERAS
"""
@app.route('/carreras/', methods=['GET'])
@auth.login_required
def get_carreras():
    if (request.method == 'GET'):
        return jsonify({'carreras': [make_public_carrera(carrera) for carrera in carreras]}),200
    else:
        abort(405)
"""
    PRIMERA CONSULTA
    RUTA PARA VER LA INFORMACION ESPECIFICA DE UNA CARRERA
"""

@app.route('/carrera/<int:carrera_codigo>/', methods=['GET'])
@auth.login_required
def get_carrera(carrera_codigo):
    if (request.method == 'GET'):
        carrera = [carrera for carrera in carreras if carrera['codigo'] == carrera_codigo]
        if (len(carrera) == 0):
            abort(404)
        return jsonify({'carrera': make_public_carrera(carrera[0])}), 200
    else:
        abort(405)
"""
    SEGUNDA CONSULTA
    RUTA PARA VER LA INFORMACION DE LAS CARRERAS QUE CONTENGAN UNA PALABRA CLAVE
"""
@app.route('/carreras/<string:busq_carrera>/', methods = ['GET'])
@auth.login_required
def get_carrera_nom(busq_carrera):
    if (request.method == 'GET'):
        L = []
        busq_carrera = busq_carrera.lower() #convierte el query en minusculas
        for carrera in carreras[0:28]:
            nombre = carrera['nombre'] #guarda el nombre en una variable
            nombre = nombre.lower() #convierte el nombre en minuscula
            dividirnombre = nombre.split() #separa el nombre en un array por palabra
            for i in range(0, len(dividirnombre)):
                if (busq_carrera == dividirnombre[i]):
                    L.append(carrera)
        if not L:
            abort(404)
        return jsonify({'carrera': L}), 200
    else:
        abort(405)

"""
    TERCERA CONSULTA
"""

@app.route('/topcarreras', methods = ['POST'])
@auth.login_required
def topcarrera():
    if (request.method == 'POST'):
        if not request.json:
            abort(404)
        postulante = {
        "nem" : request.json['nem'],
        "ranking" : request.json['ranking'],
        "lenguaje" : request.json['lenguaje'],
        "matematica" : request.json['matematica'],
        "ciencias" : request.json['ciencias'],
        "historia" : request.json['historia']
        }
        for puntaje in postulante:
            ptje = postulante[puntaje]
            try:
                postulante[puntaje]=float(postulante[puntaje])
            except:
                abort(400)

        lenmat = (postulante['lenguaje']+postulante['matematica'])/2 #Evalua si el postulante cumple con el puntaje minimo
        if lenmat<450:
            return jsonify({'respuesta': 'No cumple puntaje minimo general'})
        #Elije entre ciencias o historia el puntaje mayor
        if postulante['ciencias'] >= postulante['historia']:
            postulante['ciencias o historia'] = postulante['ciencias']
        else:
            postulante['ciencias o historia'] = postulante['historia']

        # CAMBIOOOOOOOOOOOOOOOOOOOO
        L = []
        for carrera in carreras[0:28]:
            #se guardan los datos de salida en variables
            puntaje_postulacion = ((postulante['nem']*(carrera['nem']/100)) + (postulante['ranking']*(carrera['ranking']/100)) + 
            (postulante['lenguaje']*(carrera['lenguaje']/100)) + (postulante['matematica']*(carrera['matematica']/100)) + 
            (postulante['ciencias o historia']*(carrera['ciencias o historia']/100)))
            #se realiza la diferencia para lugar tentativo
            lugar_diferencia = (carrera['primer matriculado 2019'] - carrera['ultimo matriculado 2019'])/carrera['vacantes']
            if (puntaje_postulacion >= carrera['primer matriculado 2019']):
                lugar_tentativo = 1
                datos = {
                    'Codigo de la Carrera' : carrera['codigo'],
                    'Nombre de la Carrera' : carrera['nombre'],
                    'Puntaje de Postulacion' : puntaje_postulacion,
                    'Lugar tentativo' : lugar_tentativo
                }
                L.append(datos)
            else:
                lugar_tentativo = round(((carrera['primer matriculado 2019'])-puntaje_postulacion)/lugar_diferencia)
                datos = {
                    'Codigo de la Carrera' : carrera['codigo'],
                    'Nombre de la Carrera' : carrera['nombre'],
                    'Puntaje de Postulacion' : puntaje_postulacion,
                    'Lugar tentativo' : lugar_tentativo
                }
                L.append(datos)
        Lista_orden = sorted(L, key = lambda x: x['Lugar tentativo'], reverse = True)
        topdiez = []
        for carrera in Lista_orden[0:10]:
            topdiez.append(carrera)
        return jsonify({'carreras': topdiez}), 200
    else:
        abort(405)

""" 
	ejecucion del servidor
"""
if __name__ == '__main__':
    app.run(debug=True)