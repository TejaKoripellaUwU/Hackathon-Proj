from urllib import request
from urllib.request import urlopen
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/DownloadSelect', methods=["GET","POST"])
def anotherFunc():
    if request.method == 'POST':
        gradeLevel = request.form.get("GetWorkbook")

    return render_template("DownloadSelect.html")
@views.route('/', methods=["GET","POST"])
def firstFunc():
    return render_template("Home.html")
