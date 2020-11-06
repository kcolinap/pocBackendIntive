from flask import jsonify, Flask, request
from contacs import contacts

app = Flask(__name__)


# GET /contacts
@app.route('/contacts')
def get_contacts():
    if len(contacts) == 0:
        return jsonify({'Message': 'Contacts list is empty'})

    return jsonify({'contacts': contacts})


# GET /contacts/<int:id>
@app.route('/contacts/<int:contact_id>')
def get_contact(contact_id):
    for contact in contacts:
        if contact['contact_id'] == contact_id:
            return jsonify({'contact': contact})

    return jsonify({'message': 'Contact not found'})


# POST /contacts
@app.route('/contacts', methods=['POST'])
def add_contact():
    request_data = request.get_json()

    # new contact structure
    new_contact = {
        'contact_id': request_data['contact_id'],
        'name': request_data['name'],
        'last_name': request_data['last_name'],
        'address': request_data['address'],
        'email': request_data['email'],
        'phone': request_data['phone']
    }

    # Check is the contact id already exist on app
    for contact in contacts:
        if contact['contact_id'] == new_contact['contact_id']:
            return jsonify({'message': 'Contact ID: ' + str(new_contact['contact_id']) + ' already exist on the app'})

    contacts.append(new_contact)
    return jsonify({'message': 'Contact added successfully'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
