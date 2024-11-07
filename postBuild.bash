#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it
git lfs install
tensorrt_llm -U --pre --extra-index-url https://pypi.nvidia.com