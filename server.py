from flask import Flask, Blueprint
from flask_bcrypt import Bcrypt
from app.routes import auth_blueprint
import os

app = Flask(__name__)

# Carregar configuração com base no ambiente
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config.production')
    print('produção')
else:
    app.config.from_object('config.development')
    print('desenvolvimento')

bcrypt = Bcrypt(app)
app.register_blueprint(auth_blueprint)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1010, debug=app.config['DEBUG'])




