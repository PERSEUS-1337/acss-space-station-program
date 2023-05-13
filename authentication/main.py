from user import User

# Create a user
user = User('admin', 'password123')

# Authenticate the user
if user.authenticate('password123'):
    print('User authenticated successfully.')
else:
    print('Invalid username or password.')
