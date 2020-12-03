from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    jsonify,
    make_response,
    current_app,
    send_from_directory
)


from ..computations.predict import convert_to_array, predict_image_class
from werkzeug.utils import secure_filename
import base64
import os


BASEDIR = os.path.dirname(os.path.realpath(__file__))


api_bp = Blueprint("api", __name__)


@api_bp.route("/")
def hello():
    return make_response(
        jsonify({"message": "Hello, welcome to the Xray classification API"})
    )


@api_bp.route("/predict", methods=["POST"])
def predict_image():
    file_name = request.form.get("filename")
    if request.files:
        image = request.files["file_path"]

        file_name = secure_filename(image.filename)

        image.save(os.path.join(current_app.config["UPLOADS_PATH"], file_name))

        return "File saved"

        # array =convert_to_array(image.filename)
        # image_class =predict_image_class(array)
        # print(f"\n{image_class}")

        # print("\n\n{}".format(image))

    return "<h1>Report</h1><p>Predictions:{}</p><p>Image Class :{}</p>"


@app.config('/uploads/<filename>')
def upload(filename):
    return send_from_directory(current_app.config['UPLOADS_PATH'])