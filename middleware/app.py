from flask import Flask, render_template, request, jsonify, redirect, make_response

import requests
import json


import firebase_admin
from firebase_admin import auth, credentials, firestore


app = Flask(__name__)


host_address = "192.168.141.181"


cred = credentials.Certificate(r"C:\Users\semo\Desktop\Extra Plate\middleware\secrete\config.json")
default_app = firebase_admin.initialize_app(cred)

db = firestore.client()


@app.route('/', methods = ['GET'])
def index():

    data = request.cookies.get("uid")

    if data:
        try:
            uid = auth.verify_id_token(data)

            return jsonify({'msg':'redirect'})
        except Exception as e:
            return jsonify({'msg':'error','error':str(e)})
    else:
        return render_template('index.html')
        # return jsonify({'msg':'index'})
        

@app.route('/home', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/create', methods = ['POST'])
def create():
    data = request.get_json()
    
    email = data['email']
    password = data['password']
    # longitude = data['longitude']    
    # latitude = data['latitude']

    try:
        user = auth.create_user(
            email=email,
            password=password,
        )


        # doc_ref = db.collection("location").document(user.uid)
        # doc_ref.set({"longitude": longitude, "latitude": latitude})


        # id_token = auth.create_custom_token(user.uid).decode('UTF-8')
        
        user2 = auth.get_user_by_email(email)
        id_token = user2.get_id_token()

        print("this is the token:", id_token)

        # response = make_response(jsonify({'msg':"success"}))
        # response.headers['Content-Type'] = 'application/json'
        # response.set_cookie('uid', id_token)  



        # return response
        return "hey there man"

    except auth.EmailAlreadyExistsError:
        return jsonify({"msg":"Email already exists"})

    except Exception as e:
        return jsonify({"msg":"Check your inputs and try again","error":str(e)})


@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    
    email = data['email']
    password = data['password']

    try:
        user = auth.get_user_by_email(email)

        print(vars(user))
        
        return jsonify({'msg':'success'})
    except Exception as e:
        return jsonify({'msg':str(e)})

if __name__ == "__main__":
    app.run(host = host_address, debug = True)