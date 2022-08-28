
from inspect import isfunction
import json
from flask import Blueprint, render_template,send_file, after_this_request
from flask import request,url_for,redirect
from Website.Grade1Workbook import *
from Website.Grade2Workbook import *
from Website.Grade4Workbook import *

views = Blueprint('views', __name__)

@views.route('/DownloadSelect', methods=["GET","POST"])
def anotherFunc():
    return render_template("DownloadSelect.html")

@views.route('/getTopics/', methods=["GET","POST"])
def getCustomize():
    if request.method == "POST":
        list = request.form.get("grade")
        if list == "Grade1Workbook.pdf":
            return g1Functions
        if list == "Grade2Workbook.pdf":
            return g2Functions
        if list == "Grade4Workbook.pdf":
            return g4Functions
        
        

@views.route('/customizationGate/', methods=["GET","POST"])
def customPDF():
    return render_template("Customize.html")

@views.route('/return-files/', methods=["GET","POST"])
def sendPDF():
    path = r"C:\Users\Dheeran\Documents\GitHub\Hackathon-Proj/"
    if request.method == "POST":
        pdf = request.form.get("GetWorkbook")
        print(pdf)
        if pdf == "Grade1Workbook.pdf":
            genG1Book()
        elif pdf == "Grade2Workbook.pdf":
            genG2Book()
        elif pdf == "Grade4Workbook.pdf":
            genG4Book()
        else:
            return "none was selected"
    return send_file(path+pdf)

@views.route('/', methods=["GET","POST"])
def firstFunc():
    return render_template("Home.html")
