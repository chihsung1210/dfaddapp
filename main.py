from flask import Flask,request
 
app = Flask(__name__)
 
@app.route("/")
def index():
        return "<h1>Hello Python using Flask</h1>"

#run the app
if __name__ == '__main__':
   app.run()            