import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    try:
        max_content_length_str = os.getenv('MAX_CONTENT_LENGTH', str(200 * 1024 * 1024))  # 200 MB by default as string
        MAX_CONTENT_LENGTH = int(max_content_length_str)
    except ValueError:
        MAX_CONTENT_LENGTH = 200 * 1024 * 1024  # Fallback to default value
        print("Warning: Invalid MAX_CONTENT_LENGTH value. Using default 200 MB.")

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/uploads')
