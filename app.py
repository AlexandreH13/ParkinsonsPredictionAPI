import numpy as np
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


##Abrindo o modelo (Random Forest) exportado
model = pickle.load(open('model.pkl','rb'))

##Endpoints
@app.route("/")
def verify_api_conection():
	return "Connected!", 200

##Endpoint para predição
@app.route('/predict', methods=['POST'])
def predict():
	#Pega os dados via POST
	data = request.get_json(force=True)
	prediction = model.predict(np.array([list(data.values)]))
	result = prediction[0]

	res = {'PARKINSONS ': int(result)}
	return jsonify(res)

##Cria o Flask web server
if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)