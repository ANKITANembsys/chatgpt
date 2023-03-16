# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import os
import openai
from pytube import YouTube
import os
import random
from flask import send_file



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

@app.route('/ytd/', methods = ['GET','POST'])
def ytd():
  url = request.args.get('url')
  print("https://www.youtube.com/"+str(url))
  yt = YouTube("https://www.youtube.com/"+str(url))
    
  # extract only audio
  video = yt.streams.filter(only_audio=True).first()
    
  # check for destination to save file
  print("Enter the destination (leave blank for current directory)")
  destination = '.'
  print(destination) 
  # download the file
  out_file = video.download(output_path=destination)

  num = random.random()
  # save the file
  base, ext = os.path.splitext(out_file)
  new_file = base +  str(num)+'.mp3'
  os.rename(out_file, new_file)
  print(new_file)
    
  # result of success
  print(yt.title + " has been successfully downloaded.")
  return send_file(new_file, as_attachment=True) 
# driver function
if __name__ == '__main__':

	app.run()

