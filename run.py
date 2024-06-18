from app import create_app
import logging
import os

if __name__ == '__main__':
    app = create_app()

    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    # Set up logging
    logging.basicConfig(filename='app.log', level=logging.INFO, 
                        format='%(asctime)s %(levelname)s: %(message)s')

    app.logger.info("Starting Flask server...")
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
