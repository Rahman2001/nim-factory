#!/bin/bash

cd "$PWD"
cd ../../..

mkdir -p models && cd models

outcome=$(find ./"$3" -maxdepth 1 -mindepth 1 -type d)

if [[ -z "$outcome" ]]; then
  export HF_TOKEN="$1" && git clone "$2"
  outcome=$?
  if [[ "$outcome" -eq 0 ]]; then
    echo " ---------------Model repository successfully downloaded-------------------- "
  else
    echo "Error: Model repository downloading is failed! "
    exit 128
  fi

  else
    echo "INFO: Model already exists in that directory! "
fi
