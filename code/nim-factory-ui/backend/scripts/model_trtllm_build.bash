cd "$PWD"
cd ../../../models

inputs=("$@")
checkpoint_name="${inputs[0]}"
output_dir="trtllm_""${checkpoint_name}"
unset inputs[0]

outcome=$(find ./"${output_dir}" -maxdepth 1 -mindepth 1 -type d)
command="trtllm-build --checkpoint_dir=./""${checkpoint_name}"" ""${inputs[*]}"" --output_dir=./""${output_dir}"

if [[ -z "$outcome" ]]; then
  echo "${command}"
  outcome=$(eval "${command}")

  if [[ "$outcome" -eq 0 ]]; then
    echo "------------- TensorRT-LLM engine successfully built! ------------------------ "
    else
      echo "ERROR: Failed to build engine ... "
      exit 128
  fi

  else
    echo "INFO: TensorRT-LLM engine for that model already exists in that directory"
fi
