from flask import Flask, jsonify, request, render_template
from contacs import contacts

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def get_home():
    return render_template('index.html')


# GET /contacts
@app.route('/contacts')
def get_contacts():
    return jsonify("contacts", contacts)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
