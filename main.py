
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/exemplo', methods=['POST'])
def exemplo():
    json = request.get_json()
    Pnome = json['first_name'].upper()
    Unome = json['last_name'].upper()
    time = json['time'].upper()
    role = json['role'].upper()
    return jsonify(Pnome=Pnome,Unome=Unome,time=time,role=role)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port,debug=True)