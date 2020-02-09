class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name"""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)

class EmailableContact(Contact, MailSender):
    pass

class Addresszholder:
    def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code
