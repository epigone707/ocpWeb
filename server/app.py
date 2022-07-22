from pydoc import plain
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request
import os
from flask import flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory, render_template
from loadModel import load_cif

import os, sys
sys.path.append("/home/litianyi/ocp")

from ve450_predict import model_predict

# for testing
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]
# configuration
DEBUG = True


# instantiate the app
app = Flask(__name__)
app.secret_key = "super secret key"
app.config.from_object(__name__)


UPLOAD_FOLDER = 'server/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'cif','extxyz'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# for testing


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<path:path>')
def send_files(path):
    print("send_report!!!!!!!!!!!!!!!")
    return send_from_directory('uploads', path)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'cif_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['cif_file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected extxyz_file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # print("filename:",file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join('server/uploads/', filename))
            abs_path = os.path.abspath(os.path.join('server/uploads/', filename))
            # print("abs_path",abs_path)
            data = dict(request.form)
            print("post_data:",data)
            # run the pre-trained machine learning model

            res_energy, res_forces = model_predict(test_src = "/home/litianyi/ocp/test_data",test_src_name = abs_path, checkpoint_path = "/home/litianyi/ocp/checkpoints/gemnet_oc_base_s2ef_all.pt",base_yml = "/home/litianyi/ocp/configs/s2ef/all/base.yml", gemnet_yml = "/home/litianyi/ocp/configs/s2ef/all/gemnet/gemnet-oc.yml")
            plain_force = ""
            # for force in res_forces:
            #     plain_force +=  str(force) 

            context = {
                'status': 'success',
                'energy': res_energy,
                'force': res_forces,
                # 'plain_force': plain_force,
                # 'img_1': "http://localhost:5000/uploads/{}".format(visual_filename),
            }
            
            return jsonify(**context)
    else:
        return jsonify({
            'status': 'test',
            'energy': "TEST",
            'force':  "TEST",
            'MAE':  "TEST",
        })


if __name__ == '__main__':
    app.run()
