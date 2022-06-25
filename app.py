from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys
app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        raise Exception("Testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys) 
        logging.info(housing.error_message)

    logging.info("Testing logging module")
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
