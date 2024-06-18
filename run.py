import os
from app import create_app
import logging

# Create the Flask application
app = create_app()

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

app.logger.info("Starting Flask server...")

if __name__ == '__main__':
    # Set environment variables for Flask development mode
    os.environ['FLASK_ENV'] = 'development'  # This ensures the server restarts on code changes
    
    # Run the Flask application in debug mode to enable auto-reloading
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
