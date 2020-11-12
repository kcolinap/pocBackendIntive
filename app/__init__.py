from flask import Flask
app = Flask(__name__)

from app.api import bp as api_bp
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
