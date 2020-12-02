from flask import Blueprint,request,redirect,url_for,jsonify,make_response
from ..computations.predict import convert_to_array, predict_image_class
import base64


api_bp=Blueprint('api',__name__)


@api_bp.route('/')
def hello():
    return make_response(jsonify(
        {"message":"Hello, welcome to the Xray classification API"}
    ))

@api_bp.route('/predict',methods=['POST'])
def predict_image():
    file_name=request.form.get('filename')
    if request.files:
        image=request.files['file_path']

        array =convert_to_array(image)
        image_class =predict_image_class(array)
        print(f"\n{image_class}")
    
    return "<h1>Report</h1><p>Predictions:{}</p><p>Image Class :{}</p>".format(image_class['score'],image_class['class'])