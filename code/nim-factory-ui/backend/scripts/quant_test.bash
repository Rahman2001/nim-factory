#!/bin/bash

inputs=("$@")

hf_model=${inputs[0]}
quant_format=${inputs[1]}
model_family=${inputs[2]}

unset inputs[0]
unset inputs[1]
unset inputs[2]

quant_cmd="python3 quantize.py ""${inputs[*]}"" --output_dir=quant_""${hf_model}""_""${quant_format}"

for ((i = 0; i <= 10; i++))
do
echo "$quant_cmd"
done
