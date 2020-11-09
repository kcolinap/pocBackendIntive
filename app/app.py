from flask import jsonify, Flask, request
from contacs import contacts
from utils.Utils import check_data

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

    # Check contact data len
    if check_data(new_contact):
        # Check is the contact id already exist on app
        for contact in contacts:
            if contact['contact_id'] == new_contact['contact_id']:
                return jsonify(
                    {'message': 'Contact ID: ' + str(new_contact['contact_id']) + ' already exist on the app'})

        contacts.append(new_contact)
        return jsonify({'message': 'Contact added successfully'})
    else:
        return jsonify({'message': 'One or more data field has not the correct length'})


# PUT /contacts/<int:id>
@app.route('/contacts/<int:contact_id>', methods=['PUT'])
def edit_contact(contact_id):
    for contact in contacts:
        if contact['contact_id'] == contact_id:
            request_data = request.get_json()
            aux_contact = {
                'name': request_data['name'],
                'last_name': request_data['last_name'],
                'address': request_data['address'],
                'email': request_data['email'],
                'phone': request_data['phone']
            }

            if check_data(aux_contact):
                # setting the new data for the contact
                contact['name'] = aux_contact['name']
                contact['last_name'] = aux_contact['last_name']
                contact['address'] = aux_contact['address']
                contact['email'] = aux_contact['email']
                contact['phone'] = aux_contact['phone']

                return jsonify({"message": 'Contact updated successfully'})
            else:
                return jsonify({'message': 'One or more data field has not the correct length'})
    return jsonify({'message': 'Contact not found'})


# DELETE /contacts/<int:id>
@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    for contact in contacts:
        if contact['contact_id'] == contact_id:
            contacts.remove(contact)
            return jsonify({"message": 'Contact deleted successfully'})

    return jsonify({'message': 'Contact not found'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
