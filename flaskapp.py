# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import os
import openai

openai.api_key = "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"

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/home/<str:text>', methods = ['GET'])
def disp(text):
  response = openai.Completion.create(
  model="text-davinci-003",
  prompt=text,
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)
  return response


# driver function
if __name__ == '__main__':

	app.run(debug = True)

