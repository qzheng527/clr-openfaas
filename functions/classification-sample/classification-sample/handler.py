#!/usr/bin/python3

import os
import glob
import urllib.request
from urllib.parse import urlparse
from os.path import splitext

ALLOWED_IMAGE_TYPE = [".bmp", ".BMP"]

def get_ext(url):
    parsed = urlparse(url)
    _, ext = splitext(parsed.path)
    return ext

def get_image_from_url(url):
    """get image and save to local path"""

    ext = get_ext(url)

    local_file_path = "./image" + ext
    urllib.request.urlretrieve(url, local_file_path)
    return local_file_path

def find_model_path():
    """ return model xml path """

    model_dir = os.getenv('MODEL_DIR', '/models')
    model_name = os.getenv('MODEL_NAME', 'resnet-50-int8-tf-0001') + ".xml"
    precision = os.getenv('MODEL_PRECISION', 'FP32')

    pattern = model_dir + '/**/' + precision + '/' + model_name
    paths = glob.glob(pattern, recursive=True)

    if not len(paths):
        print("No " + model_name + " found")
        return None

    return paths[0]

def do_classification(image, model_path):
    """ Use dldt sample classification_sample_async """

    cmd = "classification_sample_async -i %s -m %s" % (image, model_path)
    return os.system(cmd)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    if not len(req):
        print("Request body is missing.")
        return

    model_path = find_model_path()
    if model_path is None:
        return

    if get_ext(req) not in ALLOWED_IMAGE_TYPE:
        print("Only " + ALLOWED_IMAGE_TYPE + " images are allowed.")
        return

    file_path = get_image_from_url(req)
    do_classification(file_path, model_path)
