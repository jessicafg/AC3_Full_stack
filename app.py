import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('formulario.html')

@app.route('/api/jogo', methods=['POST'])
def jogo_jogo():

    json = request.get_json()
    first_name = json['first'].upper()
    last_name = json['last'].upper()
    time_nome = json['time'].upper()
    combo = json['combo'].upper()
    return jsonify(first=first_name, last=last_name, time=time_nome, combo=combo)


if __name__ == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)