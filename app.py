# app.py
import subprocess
import uuid
from flask import Flask, request, jsonify, send_file
import requests
from werkzeug.utils import secure_filename
import os
import ffmpeg


def create_app():
    app = Flask(__name__, static_folder='uploads', static_url_path='/uploads')
    app.config['UPLOAD_FOLDER'] = '/app/uploads/'
    upload_folder = app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    # Other setup code...
    return app


app = create_app()


@app.route('/', methods=['GET'])
def homepage():
    return "Homepage"


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello"

from flask import Flask, request
from moviepy.editor import VideoFileClip

app = Flask(__name__)

@app.route('/video/length', methods=['POST'])
def get_video_length():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return 'No file uploaded.'

    video_file = request.files['file']

    # Check if the file is a video
    if video_file and allowed_file(video_file.filename):
        # Save the video file temporarily
        video_path = '/path/to/temp/video.mp4'  # Replace with your desired path
        video_file.save(video_path)

        try:
            # Get the video duration using moviepy
            video = VideoFileClip(video_path)
            duration = video.duration
            video.close()

            return f'The video duration is {duration} seconds.'
        except:
            return 'Error occurred while processing the video.'

    return 'Invalid file format.'

def allowed_file(filename):
    # Add the allowed video file extensions here
    allowed_extensions = {'mp4', 'avi', 'mkv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    app.run()

