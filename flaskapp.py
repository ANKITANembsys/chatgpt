# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import os
import openai



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
@app.route('/essay/<string:text>/', methods = ['GET','POST'])
def disp(text):
  openai.api_key = os.environ['api']

  response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an esaay about "+str(text),
  temperature=0.3,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0)
  return response

@app.route('/txt2img/<string:text>/', methods = ['GET','POST'])
def img(text):
  openai.api_key = os.environ['api']

  response = openai.Image.create(
  prompt=text,
  n=1,
  size="1024x1024")
  image_url = response['data'][0]['url']
  return image_url

# driver function
if __name__ == '__main__':

	app.run()

