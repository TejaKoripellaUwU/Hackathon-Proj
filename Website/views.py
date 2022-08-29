
from inspect import isfunction
import json
from flask import Blueprint, render_template,send_file, after_this_request
from flask import request,url_for,redirect
from Website.Grade1Workbook import *
from Website.Grade2Workbook import *
from Website.Grade4Workbook import *
from Website.Grade9Workbook import *

views = Blueprint('views', __name__)

@views.route('/DownloadSelect', methods=["GET","POST"])
def anotherFunc():
    return render_template("DownloadSelect.html")

@views.route('/getTopics/', methods=["GET","POST"])
def getCustomize():
    if request.method == "POST":
        list = request.form.get("grade")
        global customBook
        customBook = g1Functions[:]
        customBook += g2Functions
        if list == "Grade1Workbook.pdf":
            return g1Functions
        elif list == "Grade2Workbook.pdf":
            return g2Functions
        elif list == "Grade4Workbook.pdf":
            return g4Functions
        elif list == "Grade9Workbook.pdf":
            return customBook
        

@views.route('/customizationGate/', methods=["GET","POST"])
def customPDF():
    return render_template("Customize.html")

@views.route('/return-files/', methods=["GET","POST"])
def sendPDF():
    path = r"C:\Users\Dheeran\Documents\GitHub\Hackathon-Proj/"
    if request.method == "POST":
        pdf = request.form.get("GetWorkbook")
        #print("THE PDF IS: "+str(pdf))

        if pdf == "Grade1Workbook.pdf":
            genG1Book(g1Functions,"Grade 1 Math Workbook",'Grade1Workbook')
        elif pdf == "Grade2Workbook.pdf":
            genG2Book()
        elif pdf == "Grade4Workbook.pdf":
            genG4Book()
        elif pdf == "Grade9Workbook.pdf":
            genA1Book()
    return send_file(path+pdf)

@views.route('/', methods=["GET","POST"])
def firstFunc():
    return render_template("Home.html")


allPDFs = g1Functions+g2Functions+g4Functions

@views.route('/return-gudPDF/', methods=["POST"])
def massiveL():
    path = r"C:\Users\Dheeran\Documents\GitHub\Hackathon-Proj/"
    if request.method == "POST":
        yes = request.form.get("inp")
        yes = yes.replace("[","",2)
        yes = yes.replace("]","",2)
        for m in range(0,len(yes)):
            yes = yes.replace('"',"")
        yes = yes.split(",")
        
        print(yes)
        desiredMethods = []
        for element in allPDFs:
            for item in yes:
                if element[0] == item:
                    desiredMethods.append(element)
        print(desiredMethods)
        genG1Book(desiredMethods,"Custom Math Workbook",'CustomBook')
        return send_file(path+"CustomBook.pdf")
        