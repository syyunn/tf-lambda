try:
    import unzip_requirements
except ImportError:
    pass

import json
import os
import tarfile

import boto3
import tensorflow as tf

# FILE_DIR = "/tmp/"
# BUCKET = os.environ["BUCKET"]


def forward(event, _):
    # Parse incoming json
    # body = json.loads(event.get("body"))
    # predict_input = body["input"]
    # model_id = body["model"]
    #
    # # Download model from S3 and extract
    # s3_file_name = os.path.join(model_id, ".tar.gz")
    # download_path = FILE_DIR + model_id + ".tar.gz"
    #
    # boto3.Session().resource("s3").Bucket(BUCKET).download_file(
    #     s3_file_name, download_path
    # )
    #
    # tarfile.open(download_path, "r").extractall(FILE_DIR)
    #
    # # Load model
    # classifier = tf.estimator.LinearClassifier(model_dir=FILE_DIR + model_id)
    #
    # # Predict
    # predictions = classifier.predict(predict_input)
    #
    # # Respond
    # response = {
    #     "statusCode": 200,
    #     "body": json.dumps(predictions, default=lambda x: x.decode("utf-8")),
    # }
    #
    # return response
    return None
