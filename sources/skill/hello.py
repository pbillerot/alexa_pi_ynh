from flask import Flask, Blueprint, request, url_for, redirect, jsonify
import requests, json
import os
import configparser

config = configparser.ConfigParser()
currentDir = os.path.dirname(os.path.realpath(__file__))

main = Blueprint('main', __name__, url_prefix="/alexa")

@main.route('/')
def hello_world():
  print('Hello')
  return "Hello!!"

@main.route('/hello/<user>')
def hello_user(user):
  print(f'Hello {user}')
  return f'Hello {user}'

@main.route('/parole/<section>/<paragraphe>')
def hello_user(section, paragraphe):
  return config.read(currentDir + "/data/songs.ini").get(section, paragraphe)

@main.route('/post/<user>/<age>')
# curl http://localhost:5000/alexa/post/tata/14
def hello_get_to_post(user, age):
  dico = {"user": user, "age": int(age)}
  print(f'dico {dico}')
  # Transformation de la requête GET en POST
  response = requests.post('http://localhost:5000/alexa/json', json=dico)
  print(vars(response))
  dico2 = json.loads(response.text)
  dico2["age"] = dico2["age"] * 2 
  return dico2

@main.route('/json', methods=['POST'])
# https://developer.rhino3d.com/guides/rhinopython/python-xml-json/
# curl http://localhost:5000/alexa/json -X POST -d '{"user":"toto", "age": 22}'
def hello_json():
  oContent = request.get_json(force=True)
  # force=True, above, is necessary if another developer 
  # forgot to set the MIME type to 'application/json'
  print(f'oContent {oContent}')
  oContent["age"] = oContent["age"] * 2
  return oContent

if __name__ == '__main__':
  app = Flask(__name__)
  app.register_blueprint(main)
  app.run()
