#!/bin/bash

cd "$PWD"
echo "This is working directory ""$PWD"
cd ../../../models

inputs=("$@")

hf_model=${inputs[0]}
quant_format=${inputs[1]}
model_family=${inputs[2]}
model_dir="../../../.."${inputs[3]}

unset inputs[0]
unset inputs[1]
unset inputs[2]
unset inputs[3]

quant_cmd="python3 quantize.py --model_dir=""${model_dir}"" ""${inputs[*]}"" --output_dir=../../../../models/quant_""${hf_model}""_""${quant_format}"
echo "This is quantization command : ""$quant_cmd"

outcome=$(find ./quant_"${hf_model}"_"${quant_format}" -maxdepth 1 -mindepth 1 -type f)

if [[ -z "$outcome" ]]; then
  cd ../code/TensorRT-LLM/examples/"${model_family}"
  echo "$PWD"
  echo "INFO: Wait until ${model_family} requirements get installed ...  "
  pip3 install -r requirements.txt
  echo " ---------- ${model_family} requirements installed ----------------------- "

  cd ../quantization
  echo "INFO: Wait until quantization requirements get installed ... "
  pip3 install nvidia-modelopt[all]==0.17.0
  pip3 install "cython<3.0.0" wheel
  pip3 install "pyyaml==5.4.1" --no-build-isolation
  pip3 install -r requirements.txt
  echo " ---------- quantization requirements installed -------------------- "
  
  output=$(eval "$quant_cmd") #execute quantize.py

  if [[ "$output" -eq 0 ]]; then
    echo " ---------- Model successfully quantized! -------------------- "
    else
      echo "ERROR: Model quantization failed! "
      exit 128
  fi

  else
    echo "INFO: Quantized model already exists! "

fi