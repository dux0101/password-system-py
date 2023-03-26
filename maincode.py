# login.py

# Define the username and password
USERNAME = 'myusername'
PASSWORD = 'mypassword'

def login():
    # Get the username and password from the user
    username = input('Enter username: ')
    password = input('Enter password: ')

    # Check if the username and password match the defined values
    if username == USERNAME and password == PASSWORD:
        # Redirect to the main page if login is successful
        print('Login successful!')
        # Add your code to redirect to main page here
    else:
        # Display an error message if the login fails
        print('Incorrect username or password.')

# Call the login function to start the login process
login()
