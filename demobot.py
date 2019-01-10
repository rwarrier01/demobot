# Import flask with request object
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)


# When people visit the home page '/' use the hello_world function
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ncss')
def ncss():
    return 'Welcome to NCSS'

# You can access demobot’s greet command via /greet
@app.route('/greet')
def greet_person():
    # Get the value of the 'name' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('name')
    # This bot says hi to every name it gets sent!
    return f'Hi {name}!'

@app.route('/weather')
def weather():
    temp = int(request.values.get('temp'))
    if temp > 30:
        return "It's so hot!"
    else:
        return f'The temperature is {temp}'

if __name__ == '__main__':
    # Start the web server! dd
    app.run()