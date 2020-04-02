import os
import logging
import argparse

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

from htx import app, init_model_server
from image_classifier import FastaiImageClassifier, train_script
from settings import REDIS_HOST, REDIS_PORT, RQ_QUEUE_NAME, MODEL_DIR, IMAGE_DIR


init_model_server(
    create_model_func=FastaiImageClassifier,
    train_script=train_script,
    num_iter=10,
    image_dir=IMAGE_DIR,
    model_dir=MODEL_DIR,
    redis_queue=RQ_QUEUE_NAME,
    redis_host=REDIS_HOST,
    redis_port=REDIS_PORT,
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', dest='port', default='9090')
    args = parser.parse_args()
    app.run(host='localhost', port=args.port, debug=True)
