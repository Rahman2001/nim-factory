#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it
git lfs install
pip3 install tensorrt_llm==0.14.0 -U --extra-index-url https://pypi.nvidia.com
pip3 install tensorrt-cu12-libs==10.4.0
pip3 install tensorrt-cu12-bindings==10.4.0
pip3 install "nvidia-modelopt[all]"==0.17.0