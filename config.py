from dotenv import load_dotenv
from datetime import timedelta
import os# AZUDONI VICTORY CHUWKUNEKU WORK


load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=3)
    DEBUG=False
     
    
    
class DevelopmentConfig(Config):
    DEBUG=True
    
class ProductionConfig(Config):
    DEBUG=False# AZUDONI VICTORY CHUWKUNEKU WORK