from email import message


def get_user_name():
    user_name = input("What's your name? ")
    return user_name.capitalize()

def get_hello_message(user_name):
    if user_name.isalpha():
        return f'Hello, {user_name}!'
    else:
        return 'Hello, World!'

def say_hello():
    user_name = get_user_name()
    message = get_hello_message(user_name)
    print(message)
say_hello()


