#!/bin/bash

cd "$PWD"
cd ../..

if [ -d "TensorRT-LLM" ]; then
  echo "INFO: TensorRT-LLM is already cloned in your project "
  else
    git clone https://github.com/NVIDIA/TensorRT-LLM.git --branch v0.14.0
    outcome=$?

    if [[ "$outcome" -eq 0 ]]; then
      cd TensorRT-LLM
      pip3 install -r requirements.txt
      echo " -------------------TensorRT-LLM successfully cloned-------------------------------- "
      else
        echo "Error: TensorRT-LLM failed to clone! "
        exit 128
    fi
fi