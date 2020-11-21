from flask import Flask
from .config import DevConfig,ProductionConfig,TestConfig
from .api.routes import api_bp
from .utils.database import db





def create_app():
    app=Flask(__name__)
    app.config.from_object(DevConfig)

    db.init_app(app)

    app.register_blueprint(api_bp,url_prefix='/api')
    


    @app.shell_context_processor
    def make_shell_context():
        return {"app":app,
                "db":db,
                
                }

    return app