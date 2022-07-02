from os import name
import pandas as pd
from PIL import Image, ImageDraw, ImageFont 
from fileinput import filename
import pyqrcode
import png
from pyqrcode import QRCode
import qrcode
import mysql.connector
import base64
from PIL import Image
import io 
from io import StringIO 

import email
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return  render_template('homepage.html')

@app.route('/reg', methods=["GET","POST"])
def reg():

      
    if request.method =="POST":
      
       prn = request.form.get("prn")
       full_name = request.form.get("fullname")
       email = request.form.get("email")
       phone = request.form.get("phone")
       dob = request.form.get("dob")
       address = request.form.get("address")
       city = request.form.get("city")
       dept = request.form.get("dept")
       year = request.form.get("year")
       join = request.form.get("join")
       passing = request.form.get("pass")
       print(prn,full_name,email,phone,dob,address,dept,year,join,passing)

       
       s = f'''
           COllege Name : Walchand College of Engineering      
           PRN          : {prn}
           FUll Name    : {full_name}
           email        : {email}
           Mobile No    : {phone}
           DOB          : {dob}
           Address      : {address}
           Department   : {dept}
           Year         : {year}
           Joining Year : {join}
           Passing Year : {passing}
       '''
       
       img = qrcode.make(s) 
       path = 'static/qr/'+prn+'.png'
       img.save(path)

       font = ImageFont.truetype(f"static/OpenSans-Semibold.ttf", size=24)
       
       
       template = Image.open(f"static/7.jpg")
       pic = Image.open(f"static/img/photos/84.jpg").resize((140, 193), Image.ANTIALIAS)
       template.paste(pic, (195, 129, 335, 322))
       draw = ImageDraw.Draw(template)
       draw.text((158, 344), str(prn), font=font, fill='black')
       draw.text((180, 390), full_name, font=font, fill='black')
       draw.text((204, 428), dept, font=font, fill='black')
       draw.text((162, 471), city, font=font, fill='black')
       draw.text((102, 516), "YEAR : "+prn, font=font, fill='black')
       pic = Image.open(f"static/qr/"+prn+".png").resize((180, 180), Image.ANTIALIAS)
       template.paste(pic, (339, 520, 519, 700))
       card = template
       card.save(f"static/"+prn+".jpg")

       path = "../static/"+prn+".jpg"
       return render_template('index.html',filename=path)
       
 
    return render_template('res.html')


@app.route("/home", methods=["GET"])
def home():
    return  render_template('homepage.html')


@app.route("/about", methods=["GET"])
def about():
    return  render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)

