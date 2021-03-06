from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    jsonify,
    make_response,
    current_app,
    send_from_directory,
)


from main.models.files import File
from main.utils.database import db
from ..computations.predict import loadCovid19ImageFromName,loadRegularPneumoniaImageFromName
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
        image = request.files["file"]

        file_name = secure_filename(image.filename)

        image.save(os.path.join(current_app.config["UPLOADS_PATH"], file_name))

        file_path = os.path.join(current_app.config["UPLOADS_PATH"], file_name)

        pred=loadCovid19ImageFromName(file_path)

        new_file = File(
            name=file_name,
            covid_pred_score=pred["covid_result"]["Output"],
            pneu_pred_score=pred["pneumonia_result"]["Output"],
            covid_pred_class=pred["covid_result"]["class"],
            pneu_pred_class=pred["pneumonia_result"]["class"]
        )

        new_file.save()

        print(pred)

        # print("\n{}".format(type(image_class)))

    return make_response(jsonify({"message": pred}))


@api_bp.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(current_app.config["UPLOADS_PATH"])
