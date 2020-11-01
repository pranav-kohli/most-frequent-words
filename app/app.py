import os
from flask import Flask, flash, request, redirect, jsonify, render_template
from werkzeug.utils import secure_filename
import zipfile
import glob
from core import most_freq
import utils.util as util
from document_readers.document_reader_factory import DocumentReaderFactory
# import logging
#
# logger = logging.getLogger(__name__)
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'zip'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_SORT_KEYS'] = False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def delete_files(file_list: list):
    for file_path in file_list:
        os.remove(file_path)
    # remove zip file also
    zip_file = glob.glob(UPLOAD_FOLDER + '/*.zip')
    for file_path in zip_file:
        os.remove(file_path)


def extract_files(file):
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(file_path)
    file.save(file_path)
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(UPLOAD_FOLDER)


@app.route('/', methods=['GET', 'POST'])
def upload_image_view():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            print(file)
            extract_files(file)
            file_list = glob.glob(UPLOAD_FOLDER + '/*.txt')
            file_type = util.determine_file_type(UPLOAD_FOLDER)
            file_reader = DocumentReaderFactory().get_handler(file_type)
            reader = file_reader(file_list)
            text_dict = reader.parse_as_string()
            # logger.debug("file read", text_dict)
            # if blank is passed then by default take the 5 most common words
            most_common = int(request.form['most_common']) or 5
            freq_dist = most_freq(text_dict, most_common)
            print(freq_dist)
            delete_files(file_list)
            return jsonify(freq_dist)
    return render_template('file_upload.html',)


# @app.before_first_request
# def setup_logging():
#     # In production mode, add log handler to sys.stderr.
#     app.logger.addHandler(logging.StreamHandler())
#     app.logger.setLevel(logging.INFO)


if __name__ == '__main__':
    # run flask application
    app.run(debug=True, host='0.0.0.0')

