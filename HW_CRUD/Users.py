class Users(object):

    def __init__(self, email, name, password, phone):
        self.email = email
        self.name = name
        self.password = password
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_phone(self, phone):
        self.phone = phone

    def show_user(self):
        print(self.email, self.name, self.password, self.phone)
