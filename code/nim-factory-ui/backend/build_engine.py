import json
import os
import subprocess

model_file_exists = os.path.exists("model_path.json")


def save_engine_model_path(has_trtllm_model: int, hf_or_quant_model: str):
    engine_name = "trtllm_" + hf_or_quant_model
    if has_trtllm_model == 0:
        with open("model_path.json", "r") as f:
            json_object = json.load(f)
            json_object["trtllm_engines"][engine_name] = "/models/" + engine_name

        with open("model_path.json", "w") as f:
            json.dump(json_object, f, indent=4)


def find_trtllm_engine_path(engine_name: str):
    with open("model_path.json", "r") as f:
        path = json.load(f)["trtllm_engines"][engine_name]
    return path


def start_building_engine(trtllm_param: dict):
    quant_model_name = trtllm_param["quant_model"]

    params = ""
    for key, value in trtllm_param["trtllm_params"].items():
        if value is not None and value != "":
            params += " " + key + "=" + str(value)

    if not model_file_exists:
        return None
    else:
        quant_model = subprocess.Popen([f'scripts/model_trtllm_build.bash {quant_model_name} {params}'],
                                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       executable="/bin/bash", shell=True, encoding="utf-8")

        for line in quant_model.stdout:
            status = quant_model.poll()
            if status is not None and status == 0:
                save_engine_model_path(status, quant_model_name)
            yield line
