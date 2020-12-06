from flask import Blueprint,render_template,request,url_for,send_from_directory,current_app
from ..utils.database import db
import os 


ui_bp=Blueprint('ui',__name__,template_folder='./templates')
# image_folder=current_app.config['UPLOADS_PATH']


@ui_bp.route('/')
def index():
    curr_app=current_app
    return render_template('index.html')


@ui_bp.route('/files')
def show_records():
    files=os.listdir(current_app.config['UPLOADS_PATH'])
    return render_template('files.html',files=files)

@ui_bp.route('/upload_complete')
def upload_complete():
    return render_template('complete.html')

@ui_bp.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(
        current_app.config['UPLOADS_PATH'],filename)