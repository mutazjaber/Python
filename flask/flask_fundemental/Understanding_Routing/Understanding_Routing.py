from flask import Flask ,   render_template
import string
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!' 
@app.route('/<name>')
def hi(name):
    return 'HI' + name.title() + '!'
@app.route('/repeat/<num>/<str>')
def repeat(num,str):
    strs = ''
    for i in range (int(num)):
        strs +=f'\n{str.title()}'
    return strs
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run



    from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/<name>')
def dojo(name):
    return name.title() + '!'
@app.route('/say/<name>')
def say(name):
    return f'Hi {name} !'
@app.route('/repeat/<num>/<str>')
def repeat(num, str):
    strs = ''
    for i in range (int(num)):
        strs+=f'\n{str.title()}'
    return strs
if __name__=="__main__":
    app.run(debug=True)