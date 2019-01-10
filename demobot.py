# Import flask with request object
from flask import Flask, request

# Create your app (web server)
app = Flask(__name__)

# When people visit the home page '/' use the hello_world function
@app.route('/', methods=['GET','POST'])
def hello_world():
    return 'Hello, World!'

@app.route('/ncss', methods=['GET','POST'])
def ncss():
    return 'Welcome to NCSS'

# You can access demobot’s greet command via /greet
@app.route('/greet', methods=['GET','POST'])
def greet_person():
    # Get the value of the 'text' query parameter
    # request.values is a dictionary (cool!)
    text = request.values.get('text')
    # This bot says hi to every name it gets sent!
    return f'Hi {text}!'

@app.route('/weather', methods=['GET','POST'])
def weather():
    temp = int(request.values.get('text'))
    if temp > 30:
        return "It's so hot!"
    else:
        return f'The temperature is {text} degrees'

if __name__ == '__main__':
    # Start the web server! dd
    app.run()