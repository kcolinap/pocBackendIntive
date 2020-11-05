from flask import jsonify, Flask
from contacs import contacts

app = Flask(__name__)


# GET /contacts
@app.route('/contacts')
def get_contacts():
    return jsonify("contacts", contacts)


# GET /contacts/<int:id>
@app.route('/contact/<int:id>')
def get_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return jsonify(contact)

    return jsonify({'message': 'Contact not found'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
