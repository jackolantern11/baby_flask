import os
from app import create_app, db
from app.models import Federal_Data

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Federal_Data=Federal_Data)


@app.after_request
def add_x_content_type_options(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response
