from flask import Blueprint,render_template,request,url_for
from ..utils.database import db

ui_bp=Blueprint('ui',__name__,template_folder='./templates')

@ui_bp.route('/')
def index():
    return render_template('index.html')


@ui_bp.route('/files')
def show_records():
    return render_template('files.html')