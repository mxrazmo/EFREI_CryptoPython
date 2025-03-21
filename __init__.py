from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Clé FIXE (remplace par ta clé générée)
SECRET_KEY = b'YNTZLe92f-kXunFatGEa9lIy1Pr7rcgSbeng956p8ZU='  
f = Fernet(SECRET_KEY)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()
    token = f.encrypt(valeur_bytes)
    return f"Valeur encryptée : {token.decode()}"

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        decrypted_value = f.decrypt(token.encode()).decode()
        return f"Valeur décryptée : {decrypted_value}"
    except Exception as e:
        return f"Erreur de déchiffrement : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
