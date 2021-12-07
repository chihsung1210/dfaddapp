# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return '<h1>Hello World</h1>'


# create a route for webhook
@app.route('/webhook', methods=['POST'])

def webhook():
  req = request.get_json(silent=True, force=True)
  sum = 0
  query_result = req.get('queryResult')
  num1 = int(query_result.get('parameters').get('number'))
  num2 = int(query_result.get('parameters').get('number1'))
  sum = str(num1 + num2)
  print('here num1 = {0}'.format(num1))
  print('here num2 = {0}'.format(num2))
  return {
        "fulfillmentText": 'The sum of the two numbers is: '+sum,
        "source": "webhookdata"
    }
           
## run the app
if __name__ == '__main__':
   app.run()    ####