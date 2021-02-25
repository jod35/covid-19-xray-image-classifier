from flask import Blueprint,render_template,request,url_for,send_from_directory,current_app
from ..utils.database import db
import os 
from main.models.files import File
from main.utils.database import db

ui_bp=Blueprint('ui',__name__,template_folder='./templates')
# image_folder=current_app.config['UPLOADS_PATH']


@ui_bp.route('/')
def index():
    curr_app=current_app
    return render_template('index.html')


@ui_bp.route('/files')
def show_records():
    files=File.query.order_by(File.id.desc()).all()
    return render_template('files.html',files=files)

@ui_bp.route('/upload_complete')
def upload_complete():
    return render_template('complete.html')

@ui_bp.route('/upload/<filename>')
def upload(filename):
    return send_from_directory(
        current_app.config['UPLOADS_PATH'],filename)

@ui_bp.route('/details/<int:id>')
def file_details(id):
    file_=File.query.get(id)

    return render_template('details.html',file_=file_)
