#import flask module from flask package. 
#It is used to create instances of web applications.
from flask import Flask

#creating instance of web application
app = Flask(__name__)

#define the route 
@app.route("/")
#define function that will be executed when we access the route above
def hello():
    return "Hello World!"

#run flask app when app.py starts
if __name__ == '__main__':
	#run app on port 8080
    app.run(port=8080)

#setting the debug to true will print out any python errors on the webpage
#app.run(debug=True)