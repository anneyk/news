import os

class Config:
  '''
  General configuration parent class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=a4f8556008db4415bc89dfcbd9fd06c4'
  NEWS_API_KEY = os.environ.get('a4f8556008db4415')

class ProdConfig(Config):
  pass

class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig
}

