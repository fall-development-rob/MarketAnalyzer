from flask import Flask
from api.routes import Routes

class Api():

    def __init__(self) -> None:
        self.app = Flask(__name__)

    def run(self, debug=True):
        """Register the Routes"""
        routes = Routes(self.app)

        routes.registerRoutes()
        
        """Run the Flask app."""
        self.app.run(debug=debug)