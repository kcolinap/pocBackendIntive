from flask import request
from app.api import bp
from contacs import contacts
from utils import contact_service


# GET /contacts
@bp.route('/contacts')
def get_contacts():
    return contact_service.get_contacts()


# GET /contact/<int:id>
@bp.route('/contact/<int:id>')
def get_contact(id):
    return contact_service.get_contact(id)


# POST /contact
@bp.route('/contact', methods=['POST'])
def add_contact():
    request_data = request.get_json()

    # new contact structure
    new_contact = {
        'id': request_data['id'],
        'name': request_data['name'],
        'last_name': request_data['last_name'],
        'address': request_data['address'],
        'email': request_data['email'],
        'phone': request_data['phone']
    }

    return contact_service.add_contact(new_contact)


# PUT /contact/<int:id>
@bp.route('/contact/<int:id>', methods=['PUT'])
def update_contact(id):

    request_data = request.get_json()

    aux_contact = {
        'name': request_data['name'],
        'last_name': request_data['last_name'],
        'address': request_data['address'],
        'email': request_data['email'],
        'phone': request_data['phone']
    }

    return contact_service.edit_contact(aux_contact, id)


# DELETE /contacts/<int:id>
@bp.route('/contact/<int:id>', methods=['DELETE'])
def delete_contact(id):
    return contact_service.delete_contact(id)
