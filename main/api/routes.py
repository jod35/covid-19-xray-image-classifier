from flask import Blueprint,request,redirect,url_for,jsonify,make_response
from ..computations.predict import convert_to_array, predict_image_class


api_bp=Blueprint('api',__name__)


@api_bp.route('/')
def hello():
    return make_response(jsonify(
        {"message":"Hello, welcome to the Xray classification API"}
    ))

@api_bp.route('/predict/<name>',methods=["POST"])
def greet(name):
    return jsonify({"message":name})