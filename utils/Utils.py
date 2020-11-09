from contacs import contacts


def check_data(contact):
    if len(contact['name']) > 50\
            or len(contact['last_name']) > 50 or len(contact['address']) > 100\
            or len(contact['email']) > 100 or len(contact['phone']) > 30:
        return False

    return True
