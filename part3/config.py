#!/usr/bin/python3

import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}