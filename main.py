from flask import Flask, render_template, request
from dataclasses import dataclass
import os

app = Flask(__name__)

# Set the template folder path to the root directory
app.template_folder = os.path.dirname(os.path.abspath(__file__))

app.config['DEBUG'] = True

# Data class representing a contact
@dataclass
class Contact:
    name: str
    address: str
    phone: str

# A list to store the contacts
contacts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'delete' in request.form:
            # Get the index of the contact to delete
            contact_index = int(request.form['delete'])
            if 0 <= contact_index < len(contacts):
                del contacts[contact_index]
        else:
            # Get the form data
            name = request.form.get('name')
            address = request.form.get('address')
            phone = request.form.get('phone')

            # Create a new Contact instance
            contact = Contact(name=name, address=address, phone=phone)

            # Add the contact to the address book
            contacts.append(contact)

    return render_template('index.html', contacts=contacts)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
