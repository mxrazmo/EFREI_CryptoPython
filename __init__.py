from cryptography.fernet import Fernet
from flask import Flask, jsonify

app = Flask(__name__)


key = Fernet.generate_key()  # Clé unique pour tous les utilisateurs
f = Fernet(key)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'API de chiffrement et déchiffrement."

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return jsonify({"Valeur encryptée (clé unique)": token.decode()})

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        decrypted_value = f.decrypt(token.encode()).decode()
        return jsonify({"Valeur décryptée (clé unique)": decrypted_value})
    except Exception as e:
        return jsonify({"Erreur": str(e)})
        
@app.route('/encrypt/<string:key>/<string:valeur>')
def encrypt_personal(key, valeur):
    try:
        f = Fernet(key.encode())  # Utilisation de la clé fournie
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return jsonify({"Valeur encryptée (clé personnelle)": token.decode()})
    except Exception as e:
        return jsonify({"Erreur": str(e)})

@app.route('/decrypt/<string:key>/<string:token>')
def decrypt_personal(key, token):
    try:
        f = Fernet(key.encode())  
        decrypted_value = f.decrypt(token.encode()).decode()
        return jsonify({"Valeur décryptée (clé personnelle)": decrypted_value})
    except Exception as e:
        return jsonify({"Erreur": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
