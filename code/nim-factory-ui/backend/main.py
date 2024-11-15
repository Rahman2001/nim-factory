import subprocess

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from prepare_env import prepare_env
from quantization import start_quant
from EnvironmentRequestBody import EnvironmentRequestBody

subprocess.run(['chmod', '-R', '+rwx', './scripts/'])
app = FastAPI()


@app.get("/")
def say_welcome():
    return "Welcome to backend! "


@app.post("/prepare-env")
def load_env(env: EnvironmentRequestBody):
    return prepare_env(env)


@app.post("/quantize-model")
def quantize(quant_param: dict):
    return StreamingResponse(start_quant(quant_param), media_type="text/plain")


@app.post("/build-engine")
def engine_build(engine_param: dict):
    return StreamingResponse(start_building_engine(engine_param), media_type="text/plain")
