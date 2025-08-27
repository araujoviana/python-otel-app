import logging
from flask import Flask, jsonify

app = Flask(__name__)

# Configure logging for future SkyWalking agent collection
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('Root endpoint accessed')
    return 'Hello, World!'

@app.route('/json')
def json_endpoint():
    logger.info('JSON endpoint accessed')
    return jsonify(message='Hello, JSON')

@app.route('/html')
def html_endpoint():
    logger.info('HTML endpoint accessed')
    return '<h1>Hello, HTML</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
