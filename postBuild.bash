#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it
pip3 install megatron-core
pip3 install git+https://github.com/NVIDIA/NeMo.git
pip3 install hydra-core
pip3 install pytorch-lightning
pip3 install braceexpand
pip3 install webdataset
pip3 install ijson
pip3 install matplotlib
pip3 install sacrebleu
pip3 install tensorrt_llm -U --pre --extra-index-url https://pypi.nvidia.com