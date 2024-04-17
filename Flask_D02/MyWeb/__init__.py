from flask import Flask, render_template, url_for 

def create_app():
    app = Flask(__name__) # Flask Server 인스턴스 생성
    
    
    @app.route('/')
    def root():
        return render_template('index.html')
    
    
    @app.route('/<name>')
    def name(name):
        return render_template('index.html', name=name)
    
    # Blueprint등록
    from flask import Blueprint
    from .views import data_view
    app.register_blueprint(data_view.data_BP)
    
    
    
    
    with app.test_request_context(): # 그냥 테스트용도
        print(url_for('static', filename = 'css/style_1.css'))
        print(url_for('static', filename = 'img/img.png'))
    
    return app