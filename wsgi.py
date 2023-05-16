import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, 'main')
import config

from main import app

app.secret_key = config.SECRET_KEY 

if __name__ == '__main__':
    app.run()
