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

# Export the app object at the top level for gunicorn (Render)
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
