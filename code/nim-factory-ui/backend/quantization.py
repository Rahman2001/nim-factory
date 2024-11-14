import json
import os
import subprocess
import time

# from models import models

model_file_exists = os.path.exists("model_path.json")


def save_quant_model_path(has_quant_model: int, hf_model: str, quant_format: str):
    quant_model_name = "quant_" + hf_model + "_" + quant_format
    if has_quant_model == 0:
        with open("model_path.json", "r") as f:
            json_object = json.load(f)
            json_object["quant_models"][quant_model_name] = "/model/" + quant_model_name

        with open("model_path.json", "w") as f:
            json.dump(json_object, f, indent=4)


def find_quant_model_path(quant_model_name: str):
    with open("model_path.json", "r") as f:
        path = json.load(f)["quant_models"][quant_model_name]
    return path


def start_quant(quant_param: dict):
    params = ""
    for key, value in quant_param.items():
        if value is not None and value != "":
            params += " " + key + "=" + str(value)

    if not model_file_exists:
        return None
    else:
        quant_model = subprocess.Popen([f'scripts/quant_test.bash gpt2 awq_4 gpt {params}'],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       executable="/bin/bash", shell=True, encoding="utf-8")
        for line in quant_model.stdout.readlines():
            yield line


# dic = {
#     "--model_dir": "alndslkan",
#     "--kv_cache": True,
#     "--workers": 1,
#     "--quant": "awq_4"
# }
