from flask import Flask
from src.main.routes.document_routes import document_routes_bp

app = Flask(__name__)
app.register_blueprint(document_routes_bp)