from flask import Flask
from flask_fontawesome import FontAwesome
from .config import DevConfig,ProductionConfig,TestConfig
from .api.routes import api_bp
from .utils.database import db
from .ui.routes import ui_bp
from flask_dropzone import Dropzone
from .models.files import File




def create_app():
    app=Flask(__name__,static_folder='./static')
    app.config.from_object(DevConfig)

    db.init_app(app)
    fa=FontAwesome(app)
    dropzone=Dropzone(app)

    app.register_blueprint(api_bp,url_prefix='/api')

    app.register_blueprint(ui_bp,url_prefix='/')
    


    @app.shell_context_processor
    def make_shell_context():
        return {"app":app,
                "db":db,
                "File":File
                
                }

    return app