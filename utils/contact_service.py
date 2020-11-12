from flask import jsonify
from contacs import contacts
from utils.Utils import check_data


def get_contacts():
    if len(contacts) == 0:
        return jsonify({'Message': 'Contacts list is empty'})

    return jsonify({'contacts': contacts})


def get_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return jsonify({'contact': contact})

    return jsonify({'message': 'Contact not found'})


def add_contact(new_contact):
    # Check contact data len
    if check_data(new_contact):
        # Check is the contact id already exist on app
        for contact in contacts:
            if contact['id'] == new_contact['id']:
                return jsonify(
                    {'message': 'Contact ID: ' + str(new_contact['id']) + ' already exist on the app'})

        contacts.append(new_contact)

        return jsonify({'message': 'Contact added successfully'})
    else:
        return jsonify({'message': 'One or more data field has not the correct length'})


def edit_contact(auxContact, id):
    for contact in contacts:
        if contact['id'] == id:
            aux_contact = {
                'name': auxContact['name'],
                'last_name': auxContact['last_name'],
                'address': auxContact['address'],
                'email': auxContact['email'],
                'phone': auxContact['phone']
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


def delete_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contacts.remove(contact)
            return jsonify({"message": 'Contact deleted successfully'})
    return jsonify({"message": "Contact not found"})
