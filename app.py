import os

from flask import Flask, request
from werkzeug.utils import secure_filename

from api.util import file_utils as f

UPLOAD_FOLDER = 'uploads'
PERMITTED_FORMATS = set(['txt'])
# from database import db_session

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in PERMITTED_FORMATS


@app.route('/')
def index():
    return "MediaMath Financial Platform Code Challenge"


@app.route('/files/', methods=['POST'])
def upload_file():
    if 'ascii_file' not in request.files:
        return "There was no value with key 'ascii_file'"
    ascii_file = request.files['ascii_file']

    print type(ascii_file)
    if ascii_file.filename == '':
        return "Your file needs a filename"
    if file and allowed_file(ascii_file.filename):
        filename = secure_filename(ascii_file.filename)
        ascii_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    f.file_word_count(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return "File successfully saved"


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()


if __name__ == '__main__':
    app.run(debug=True)