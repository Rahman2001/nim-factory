#!/bin/bash
# This file contains bash commands that will be executed at the end of the container build process,
# after all system packages and programming language specific package have been installed.
#
# Note: This file may be removed if you don't need to use it
sudo apt-get update && apt-get -y install python3.10 python3-pip
apt install unzip
apt-get wget
sudo apt-get update && apt-get -y install openmpi-bin libopenmpi-dev git git-lfs