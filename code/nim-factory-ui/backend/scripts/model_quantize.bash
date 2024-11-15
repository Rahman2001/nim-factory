#!/bin/bash

cd "$PWD"
cd ../model

inputs=("$@")

hf_model=${inputs[0]}
quant_format=${inputs[1]}
model_family=${inputs[2]}

unset inputs[0]
unset inputs[1]
unset inputs[2]

quant_cmd="python3 quantize.py ""${inputs[*]}"" --output_dir=quant_""${hf_model}""_""${quant_format}"

outcome=$(find ./quant_"${hf_model}"_"${quant_format}" -maxdepth 1 -mindepth 1 -type d)

if [[ -z "$outcome" ]]; then
  cd ../TensorRT-LLM/examples/"${model_family}"
  echo "INFO: Wait until ${model_family} requirements get installed ...  "
  pip3 install -r requirements.txt
  echo " ---------- ${model_family} requirements installed ----------------------- "

  cd ../quantization
  echo "INFO: Wait until quantization requirements get installed ... "
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