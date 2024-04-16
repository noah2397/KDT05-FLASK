from flask import Flask, render_template



def create_app():
        app = Flask(__name__)
        from .views import root
        app.register_blueprint(root.bp)
        
        return app
