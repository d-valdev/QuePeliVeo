from flask import Flask, jsonify, request
from flask_cors import CORS

from recomendador.gemma.recomendador import formular
from recomendador.buscador import sacar_datos_pelis

app = Flask(__name__)
CORS(app, resources={r"/recomendador/*": {"origins": ["https://quepeliveo.es", "https://www.quepeliveo.es"]}})



@app.route('/recomendador', methods=['GET'])
def recomendar_peli():
    prompt = request.args.get('prompt')
    numero = request.args.get('numero')
    
    respuesta = formular(prompt, numero)

    print(respuesta)

    if respuesta == "":
        return jsonify({})
    else:
        pelis = []
        datos = []       
        resp_clean = respuesta.replace('"', '').replace("\n","").replace("'","")

        resp_clean = ' '.join(resp_clean.split())

        pelis = [item.strip() for item in resp_clean.split(',')]
        
        print(pelis)

        datos = sacar_datos_pelis(pelis)
        
        return jsonify(datos)

@app.route('/recomendador', methods=['OPTIONS'])
def handle_options():
    response = jsonify()
    response.status_code = 200
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)