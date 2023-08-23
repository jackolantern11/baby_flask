import os
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.after_request
def add_x_content_type_options(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response