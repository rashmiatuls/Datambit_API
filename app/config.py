import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', 200 * 1024 * 1024))  # 200 MB by default
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'app/uploads')
