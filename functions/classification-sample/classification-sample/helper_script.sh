#!/bin/bash

# Download and convert models
export MODEL_DIR="/models"
export MO_PATH="/usr/share/openvino/model-optimizer/mo.py"
export MODEL_NAME="resnet-50-int8-tf-0001"

# Download and convert models
model-downloader --name $MODEL_NAME -o $MODEL_DIR
model-converter --name $MODEL_NAME -d $MODEL_DIR -o $MODEL_DIR --mo $MO_PATH
