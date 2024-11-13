import json
import os.path
import subprocess

from EnvironmentRequestBody import EnvironmentRequestBody
# from Model import Model
from models import repo

model_file_exists = os.path.exists("model_path.json")
huggingface_dom = "https://huggingface.co/"


def get_hf_model(env: EnvironmentRequestBody):
    model = env.model
    hf_model = model.version
    if model.type is not None:
        hf_model = hf_model + "-" + model.type
    return hf_model


def get_huggingface_repo(env: EnvironmentRequestBody):
    repo_owner = repo[env.model.family]
    hf_model = get_hf_model(env)
    return huggingface_dom + repo_owner + "/" + hf_model


def save_model_path(has_model: int, hf_model: str):
    if has_model == 0:
        with open("model_path.json", "r") as f:
            json_object = json.load(f)
            json_object["base_model"]["gpt2"] = "/model/" + hf_model

        with open("model_path.json", "w") as f:
            json.dump(json_object, f, indent=4)


def find_base_model_path(hf_model: str):
    with open("model_path.json", "r") as f:
        path = json.load(f)["base_model"][hf_model]
    return path


def prepare_env(environment: EnvironmentRequestBody):
    hf_model = get_hf_model(environment)
    has_tensorrt_llm = subprocess.call("scripts/tensorrt_llm_download.bash", executable="/bin/bash", shell=True)

    if not model_file_exists:
        with open("model_path.json", "w") as f:
            base_model = {"base_model": {}}
            json.dump(base_model, f)

        hf_link = get_huggingface_repo(environment)
        hf_token = ""
        if environment.huggingface is not None:
            hf_token = environment.huggingface['token']

        has_model = subprocess.call(f'scripts/model_download.bash '
                                    f'{hf_token} {str(hf_link)} {str(hf_model)}',
                                    executable="/bin/bash", shell=True)
        save_model_path(has_model, hf_model)
    else:
        path = find_base_model_path(hf_model)
        has_model = 0 if path != "" and path is not None else 128

    return {"has_tensorrt_llm": has_tensorrt_llm, "has_model": has_model}

