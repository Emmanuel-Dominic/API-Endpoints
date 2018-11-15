class User(object):
    """User class handles create and read ,signin and sign up for user"""
    users = [
        {'Matembu Emmanuel', 'HD2U9DHHHOW8', 'ematembu@gmail.com', 'pass'},
        {'Dominic Emmanuel', '9HEH9HH9OH2FKA', 'ematembu1@gmail.com', 'pass'}
        ]

    def __init__(self):
        pass


   def sign_up(self, name, email, card_Number, password, role='user'):
    """creates new user"""
        for person in self.users:
            if person['email'] != self.email:
                # create account
                user = {
                    'name':self.name,
                    'email':self.email,
                    'password':self.password,
                    'card_Number':self.card_Number,
                    'role':self.role
                    }
                self.users.append(user)
                return 'Created Account successfully'
            # username exists
            print('Missing input')
            return 'Email :{}  already in use'.format(self.email)


    def log_in(self, email, password):
        """logins in valid user"""
        for person in self.users:
            # validate email
            if person['email'] == email:
                # verify password
                if person['password'] == password:
                    self.status = True
                    return 'Welcome,{}'.format(person['name'])
            # either or both email and password is wrong
            return 'Invalid Credentials'


    def is_logged_in(self):
        """Checks whether user is logged in,return type: boolean"""
        return self.status


    def log_out(self):
        """logs out user"""
        self.status = False
        print("You're now logged out")




if __name__ == '__main__':
    # emma = User('Matembu Emmanuel', 'HD2U9DHHHOW8', 'ematembu@gmail.com', 'pass')
    # emma.sign_up()
    # jose = User()
    # jose.log_in('ematembu1@gmail.com', 'pass2')
    print(User.users)
    app.run(debug=True)