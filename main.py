import os
from flask import Flask,request,render_template,make_response,jsonify
from werkzeug import secure_filename
from countStars import countStars

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            num = countStars(file)
            print (jsonify(num))
            return jsonify(num)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)