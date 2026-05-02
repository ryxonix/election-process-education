from flask import Flask
from api.routes import api_bp

def create_app():
    """
    Application Factory for Voter Intelligence & Action System.
    """
    app = Flask(__name__, template_folder='ui/templates')
    
    # Register Modular Routing Blueprint
    app.register_blueprint(api_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
