from urllib.request import urlopen
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('', methods=["GET","POST"])
def firstFunc():
    return render_template("Home.html", request = "yes")
@views.route('DownloadSelect', methods=["GET","POST"])
def anotherFunc():
    return render_template("DownloadSelect.html")