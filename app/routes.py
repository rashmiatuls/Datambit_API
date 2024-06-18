from flask import request, jsonify, current_app as app
from datetime import datetime
import os
from .utils import allowed_file
import logging

@app.route('/upload', methods=['POST'])
def upload_file():
    requested_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if 'file' not in request.files:
        app.logger.error("No file part in the request")
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    client_name = request.form.get('client_name')

    if not client_name:
        app.logger.error("No client name provided")
        return jsonify({'error': 'No client name provided'}), 400

    if file.filename == '':
        app.logger.error("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        response_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        app.logger.info(f"File {file.filename} uploaded by {client_name}")

        return jsonify({
            'message': 'File uploaded successfully',
            'client_name': client_name,
            'requested_time': requested_time,
            'response_time': response_time
        })

    app.logger.error("File type is not allowed")
    return jsonify({'error': 'File type is not allowed'}), 400

@app.errorhandler(413)
def request_entity_too_large(error):
    app.logger.error("File is too large")
    return jsonify({'error': 'File is too large'}), 413
