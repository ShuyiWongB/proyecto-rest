#!flask/bin/python
import six
from flask import Flask, jsonify, abort, request, make_response, url_for
#from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, static_url_path="")
#auth = HTTPBasicAuth()


#@auth.get_password
#def get_password(username):
#    if username == 'miguel':
#        return 'python'
#    return None


#@auth.error_handler
#def unauthorized():
#    # return 403 instead of 401 to prevent browsers from displaying the default
#    # auth dialog
#    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Error de peticion'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'No encontrado'}), 404)


carreras = [
    {
        'codigo': 21089,
        'nombre': u'Administracion Publica',
        'nem': 15,
        'ranking': 20,
        'lenguaje': 30,
        'matematicas': 25,
        'ciencias o historia': 10,
        'puntaje minimo lenguaje y matematicas': 450,
        'puntaje minimo ponderado': "no tiene",
        'vacantes': 35,
        'primero 2019': 625.8,
        'ultimo 2019':513
    },
    {
        'codigo': 21002,
        'nombre': u'Bibliotecologia',
        'nem': 25,
        'ranking': 20,
        'lenguaje': 40,
        'matematicas': 10,
        'ciencias o historia': 10,
        'puntaje minimo lenguaje y matematicas': 450,
        'puntaje minimo ponderado': "no tiene",
        'vacantes': 35,
        'primero 2019': 675.3,
        'ultimo 2019': 453.6
    }
]

postulantes = [
    {
    }
]

def make_public_carrera(carrera):
    new_carrera = {}
    for field in carrera:
        if field == 'codigo':
            new_carrera['uri'] = url_for('get_carrera', carrera_codigo=carrera['codigo'],
                                      _external=True)
        else:
            new_carrera[field] = carrera[field]
    return new_carrera

def make_public_postulante(postulante):
    new_postulante = {}
    return new_postulante

@app.route('/mejores', methods=['POST'])
#@auth.login_required
def create_carrera():
    if not request.json or 'nem' not in request.json or 'ranking' not in request.json or 'lenguaje' not in request.json or 'matematicas' not in request.json or 'ciencia' not in request.json or 'historia' not in request.json or 'nem'==None or 'ranking'==None or 'lenguaje'==None or 'matematicas'==None or 'ciencia'==None or 'historia'==None:
        abort(400)

        nem = request.json['nem']
        ranking = request.json['ranking']
        lenguaje = request.json['lenguaje']
        matematicas = request.json['matematicas']
        ciencia = request.json['ciencia']
        historia = request.json['historia']
        postulante = [nem,ranking,lenguaje,matematicas,ciencia,historia]
        postulante.append(postulante)
    #lengmat = (lenguaje+matenaticas)/2
    #if (lengmat<450):
    #    json = {"mensaje":"No supera el promedio ponderado entre lenguaje y matematicas"}
    #    return jsonify(json)
    #if (ciencia>historia):
    #    postulante['historia']=ciencia
    #else:
    #        postulante['ciencia']=historia
    return jsonify(postulante), 201


@app.route('/carreras', methods=['GET'])
#@auth.login_required
def get_carreras():
    return jsonify({'carreras': [make_public_carrera(carrera) for carrera in carreras]})


@app.route('/carreras/<int:carrera_codigo>', methods=['GET']) #Entregar los datos de una carrera con su codigo
#@auth.login_required
def get_carrera(carrera_codigo):
    carrera = [carrera for carrera in carreras if carrera['codigo'] == carrera_codigo]
    if len(carrera) == 0:
        abort(404)
    return jsonify({'carrera': make_public_carrera(carrera[0])})


@app.route('/carreras/<string:carrera_nombre>', methods=['GET']) #Entregar los datos de una carrera con su nombre
#@auth.login_required
def get_carrera2(carrera_nombre):
    carrera = [carrera for carrera in carreras if carrera['nombre'] == carrera_nombre]
    if len(carrera) == 0:
        abort(404)
    return jsonify({'carrera': make_public_carrera(carrera[0])})


if __name__ == '__main__':
    app.run(debug=True)
