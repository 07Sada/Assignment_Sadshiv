from flask import Flask, render_template, request
import pandas as pd
from flask_wtf import FlaskForm 
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import pickle
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'
app.config['UPLOAD_FOLDER'] = './static/files'

model = pickle.load(open('artifacts/kmeans_model.pickle', 'rb'))
test_result_dict = pickle.load(open('artifacts/test_result_dict.pickle', 'rb'))
directory = "static/files"

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    message = None  # Initialize the message variable
    if form.validate_on_submit():
        _ = [os.remove(os.path.join(directory, file)) for file in os.listdir(directory)] # removing all files from the directory
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        message = "File uploaded successfully!"
        return render_template('index.html', form=form, message=message)
    return render_template('index.html', form=form)


@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    # If the user has not pressed the submit button, redirect them to the home page
    if request.method == 'GET':
        return redirect('/')

    # Load the uploaded file and perform prediction
    file_path = os.path.join(directory, os.listdir(directory)[0])
    df = pd.read_csv(file_path)

    # Make a prediction
    prediction_results = model.predict(df)[0]

    genre_of_music = test_result_dict[int(prediction_results)]

    form = UploadFileForm()  # Add this line to create an instance of the form

    # Render the template with the prediction
    return render_template('index.html', form=form, prediction_text=f'Genre of the music: {genre_of_music}')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)