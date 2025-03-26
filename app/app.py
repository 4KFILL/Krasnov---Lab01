from flask import Flask, jsonify
from datetime import date

app = Flask(__name__)
# класс Phone
class Phone:
    def __init__(self, TypeID: int, CountryCode: int, Operator: int, Number: int):
        self.TypeID = TypeID
        self.CountryCode = CountryCode
        self.Operator = Operator
        self.Number = Number

    def constructor(self):
        return {
            'TypeID': self.TypeID,
            'CountryCode': self.CountryCode,
            'Operator': self.Operator,
            'Number': self.Number
        }
# класс Contact
class Contact:
    def __init__(self, ID: int, Username: str, GivenName: str, FamilyName: str, Phone: Phone, Email: str, Birthdate: date):
        self.ID = ID
        self.Username = Username
        self.GivenName = GivenName
        self.FamilyName = FamilyName
        self.Phone = Phone
        self.Email = Email
        self.Birthdate = Birthdate
    
    def constructor(self):
        return {
            'ID': self.ID,
            'Username': self.Username,
            'GivenName': self.GivenName,
            'FamilyName': self.FamilyName,
            'Phone': self.Phone.constructor(),
            'Email': self.Email,
            'Birthdate': self.Birthdate
        }
    
# класс Group
class Group:
    def __init__(self, ID: int, Title: str, Description: str, Contacts: int):
        self.ID = ID
        self.Title = Title
        self.Description = Description
        self.Contacts = Contacts
    
    def constructor(self):
        return {
            'ID': self.ID,
            'Title': self.Title,
            'Description': self.Description,
            'Contacts': self.Contacts
        }

#Запросы Contact
@app.route('/api/v1/contact', methods=['POST'])
def create_contact():
    contact = Contact(1, 'test', 'test', 'test', Phone(1, 7, 9, 9), 'test', date(2022, 1, 1))
    return jsonify(contact.constructor())

@app.route('/api/v1/contact/', methods=['GET'])
def get_contact():
    contact = Contact(1, 'test', 'test', 'test', Phone(1, 7, 9, 9), 'test', date(2022, 1, 1))
    return jsonify(contact.constructor())

@app.route('/api/v1/contact/', methods=['PUT'])
def update_contact():
    contact = Contact(1, 'test', 'test', 'test', Phone(1, 7, 9, 9), 'test', date(2022, 1, 1))
    return jsonify(contact.constructor())

@app.route('/api/v1/contact/', methods=['DELETE'])
def delete_contact():
    contact = Contact(1, 'test', 'test', 'test', Phone(1, 7, 9, 9), 'test', date(2022, 1, 1))
    return jsonify(contact.constructor())

#Запросы Group
@app.route('/api/v1/group', methods=['POST'])
def create_group():
    group = Group(1, 'test', 'test', 1)
    return jsonify(group.constructor())

@app.route('/api/v1/group/', methods=['GET'])
def get_group():
    group = Group(1, 'test', 'test', 1)
    return jsonify(group.constructor())

@app.route('/api/v1/group/', methods=['PUT'])
def update_group():
    group = Group(1, 'test', 'test', 1)
    return jsonify(group.constructor())

@app.route('/api/v1/group/', methods=['DELETE'])
def delete_group():
    group = Group(1, 'test', 'test', 1)
    return jsonify(group.constructor())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6080)