from flask import Flask, render_template, url_for 

def create_app():
    app = Flask(__name__)
    
    from flask import Blueprint
    from .views import view
    app.register_blueprint(view.bp)
    
    return app

