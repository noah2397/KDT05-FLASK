from flask import Blueprint, render_template, request 
from YouWEB.models import Question
from datetime import datetime
from YouWEB import db
bp = Blueprint('data', __name__, template_folder = 'templates',
                    url_prefix="/")

@bp.route('/', methods=['GET','POST'])
def index():
    req_dict = request.form.to_dict()
    
    subject = req_dict.get('subject')
    content = req_dict.get('content')
    q=Question(subject=subject, content=content, create_date=datetime.now())
    db.session.add(q)
    db.session.commit()
    
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question_list.html', question_list = question_list, req_dict = req_dict)


@bp.route('/load_data')
def load_data():
    return render_template('update.html')

    